import { registry } from '../module.ts';
import type { ReleaseConfig } from '../module.ts';

// The SDK repo's own Maven repository, which GitHub Pages serves at https://<owner>.github.io/<repo>
// from its maven branch (./maven.yml.liquid pushes the branch and deploys it). It holds
// `group:artifact` at the group's path: a version is published when its POM is there, and
// maven-metadata.xml names the latest release.
const directory = ({ package: coordinate, repository }: ReleaseConfig) => {
  const [group, artifact, ...rest] = coordinate.split(':');
  if (!group || !artifact || rest.length > 0) throw new Error(`${coordinate} is not a Maven group:artifact`);
  const [owner, repo] = repository.split('/');
  return { url: `https://${owner}.github.io/${repo}/${group.replaceAll('.', '/')}/${artifact}`, artifact };
};

const pom = (config: ReleaseConfig) => {
  const { url, artifact } = directory(config);
  return `${url}/${config.version}/${artifact}-${config.version}.pom`;
};

/** The SDK repo's public Maven repository on GitHub Pages. */
export default registry({
  label: 'Maven',
  page: pom,
  version: pom,
  async latest(fetch, config) {
    const response = await fetch(`${directory(config).url}/maven-metadata.xml`);
    if (response.status === 404) return undefined;
    if (!response.ok) throw new Error(`Maven answered ${response.status} for ${config.package}'s maven-metadata.xml`);
    const metadata = await response.text();
    const latest = /<release>\s*([^<\s]+)\s*<\/release>/.exec(metadata) ?? /<latest>\s*([^<\s]+)\s*<\/latest>/.exec(metadata);
    if (!latest) throw new Error(`Maven's maven-metadata.xml for ${config.package} names neither a release nor a latest version`);
    return latest[1];
  },
});
