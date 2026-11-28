import { compareVersions, exists, highest } from '../module.ts';
import type { Fetch, ModuleContext, ReleaseConfig, ReleaseModule } from '../module.ts';

/** What giving the version its GitHub release reads, in the run of the SDK repo's release workflow. */
export interface ReleaseContext extends ModuleContext {
  /** The commit this run releases (GITHUB_SHA). */
  sha: string;
  /** Whether this run decided to publish the version: only its commit may be tagged with it. */
  publishedHere: boolean;
  /** Where the modules before github published the version, in order. */
  before: Array<{ label: string; page: string }>;
}

const API = 'https://api.github.com';

async function tags(fetch: Fetch, repository: string): Promise<string[]> {
  const names: string[] = [];
  let url: string | undefined = `${API}/repos/${repository}/tags?per_page=100`;
  while (url) {
    const response: Response = await fetch(url);
    if (response.status === 404) return [];
    if (!response.ok) throw new Error(`GitHub answered ${response.status} for ${repository}'s tags`);
    names.push(...((await response.json()) as Array<{ name: string }>).map(({ name }) => name));
    url = /<([^>]+)>;\s*rel="next"/.exec(response.headers.get('link') ?? '')?.[1];
  }
  return names;
}

const page = ({ repository, tag }: ReleaseConfig) => `https://github.com/${repository}/releases/tag/${tag}`;

/** The repo's newest stable tag before the version (a leading v or not, as the repo tags), if any. */
async function previousTag(fetch: Fetch, { repository, version }: ReleaseConfig): Promise<string | undefined> {
  return (await tags(fetch, repository))
    .filter((name) => /^v?\d+\.\d+\.\d+$/.test(name) && compareVersions(name.replace(/^v/, ''), version) < 0)
    .sort((a, b) => compareVersions(a.replace(/^v/, ''), b.replace(/^v/, '')))
    .at(-1);
}

/**
 * The SDK repo's own tag and GitHub release for the version, the last module of every release. The
 * version is here once its tag is, which is all a Go module or a Swift package needs to be published:
 * their tools resolve a version by its tag. `release` gives the tag a GitHub release, at this run's
 * commit only in the run that decided to publish it, and at the tag for a version tagged before its
 * release (as Fern's deliveries were).
 */
const github: ReleaseModule & {
  release: (config: ReleaseConfig, context: ReleaseContext) => Promise<{ url: string; created: boolean }>;
} = {
  label: 'GitHub',
  page,
  has: ({ repository, tag }, { fetch }) =>
    exists(`${API}/repos/${repository}/git/ref/tags/${encodeURIComponent(tag)}`, `${repository}'s tag ${tag}`, fetch),
  async latest({ repository }, { fetch }) {
    return highest(await tags(fetch, repository));
  },
  async release(config, { sha, publishedHere, fetch, before }) {
    const request = async (route: string, init: RequestInit = {}) =>
      fetch(`${API}/repos/${config.repository}${route}`, {
        ...init,
        headers: { Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' },
      });
    const answer = async <T>(response: Response, what: string, status = 200): Promise<T> => {
      if (response.status !== status) throw new Error(`${what} answered ${response.status}: ${await response.text()}`);
      return (await response.json()) as T;
    };

    const existing = await request(`/releases/tags/${encodeURIComponent(config.tag)}`);
    if (existing.status !== 404) {
      return { url: (await answer<{ html_url: string }>(existing, `GitHub's ${config.tag} release`)).html_url, created: false };
    }
    const tagged = await request(`/git/ref/tags/${encodeURIComponent(config.tag)}`);
    if (tagged.status !== 404) await answer(tagged, `GitHub's ${config.tag} tag`);
    if (tagged.status === 404 && !publishedHere) {
      throw new Error(
        `${config.tag} is neither released nor tagged, and this run did not decide to publish ${config.package} ${config.version}: re-run the failed jobs of the run that did`,
      );
    }
    const at = tagged.status === 404 ? sha : config.tag;
    const { commit } = await answer<{ commit: { message: string } }>(await request(`/commits/${at}`), `GitHub's commit ${at}`);
    // A delivery's message names its monorepo commit as `whop-monorepo@<sha>` (older deliveries: the
    // commit's URL). The monorepo is private, so the body names it in plain text.
    const source = /whop-monorepo(?:@|\/commit\/)([0-9a-f]{40})/.exec(commit.message)?.[1];
    const previous = await previousTag(fetch, config);
    const where = before.length > 0 ? before : [{ label: '', page: page(config) }];
    const body = [
      ...where.map(({ label, page: url }) => `${config.package} ${config.version}${label ? ` on ${label}` : ''}: ${url}`),
      ...(previous ? [`Changes since ${previous}: https://github.com/${config.repository}/compare/${previous}...${config.tag}`] : []),
      ...(source ? [`Built from whop-monorepo@${source.slice(0, 12)}.`] : []),
    ].join('\n\n');
    const created = await answer<{ html_url: string }>(
      await request('/releases', {
        method: 'POST',
        body: JSON.stringify({ tag_name: config.tag, target_commitish: sha, name: config.tag, body, make_latest: 'legacy' }),
      }),
      `Creating the ${config.tag} release`,
      201,
    );
    return { url: created.html_url, created: true };
  },
};

export default github;
