#!/usr/bin/env node
// Releases a Whop SDK repo's version. The SDK pipeline in whop-monorepo (sdks/pipeline) delivers this
// file into every SDK repo at .github/release/, with the modules (module.ts, modules.ts, modules/) and
// release.json beside it (the package, the version the delivery carries, its tag and the repo). The
// repo's release workflow runs it with the modules the version is published to, in order, as
// `--module` arguments (the language's delivery.modules). Its source is sdks/release/cli.ts in
// whop-monorepo.

import fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';

import { compareVersions, confirm, labels } from './module.ts';
import type { Fetch, ModuleContext, Release, ReleaseConfig } from './module.ts';
import { MODULES, releaseOf } from './modules.ts';
import github from './modules/github.ts';
import type { ReleaseContext } from './modules/github.ts';

const USAGE = `Usage: node .github/release/cli.ts <plan|confirm|release> --module <name>...

  --module  A module the version is published to, in order (pypi, npm, rubygems, crates, maven,
            github): the workflow passes the language's delivery.modules

  plan      Whether any of the release's modules lacks the version release.json names, so the
            workflow builds it (build), and whether it then publishes it (publish: build, unless
            release.json turns releases off); outputs version, tag, page, build, publish and
            rehearse, and fails on a version behind the newest any module has, or one a module has
            while a module after it lacks it (GITHUB_TOKEN for GitHub's API). REHEARSE=true builds
            the version whatever the modules have and publishes nothing
  confirm   Waits until the one module given has the version its job just uploaded
  release   Gives the version its GitHub release (github, the last module), naming where the modules
            before it published it (GITHUB_SHA and GITHUB_TOKEN; PUBLISHED=true in the run that
            decided to publish, the only run that may tag a new commit); with releases off or
            REHEARSE=true, says what it would do and writes nothing
`;

const DARK = `Releases are off for this repo (delivery.releases in whop-monorepo's sdks/<language>/language.ts).`;
const REHEARSAL = 'This run is a rehearsal (the dispatch asked for one): it builds and checks the version and publishes, tags and releases nothing.';

/**
 * Whether the workflow builds the version as a release (a module lacks it) and whether it then
 * publishes it (not with releases off). A version every module has needs no build, even when its
 * GitHub release is missing, which `release` gives it.
 */
export async function plan(
  release: Release,
  config: ReleaseConfig,
  context: ModuleContext,
): Promise<{ build: boolean; publish: boolean; lacking: string[] }> {
  requireStable(config);
  const held: boolean[] = [];
  for (const module of release) held.push(await module.has(config, context));
  const lacking = release.filter((_, index) => !held[index]).map(({ label }) => label);
  if (lacking.length === 0) return { build: false, publish: false, lacking };

  // The modules publish in order, so a module that has the version before one that lacks it means the
  // run that published it stopped partway, and only that run's commit may carry the rest.
  const stopped = release.findIndex((_, index) => !held[index] && held.slice(0, index).some(Boolean));
  if (stopped !== -1) {
    const had = release.filter((_, index) => index < stopped && held[index]).map(({ label }) => label);
    throw new Error(
      `${labels(had)} ${had.length > 1 ? 'have' : 'has'} ${config.package} ${config.version} but ${release[stopped].label} does not: the run that published it stopped partway; re-run that run's failed jobs`,
    );
  }

  for (const module of release) {
    const newest = await module.latest(config, context);
    if (newest && compareVersions(config.version, newest) < 0) {
      throw new Error(
        `main is at ${config.version} but ${module.label} already has ${newest}; raise sdks/fern/sdk-version.txt in whop-monorepo past it`,
      );
    }
  }
  return { build: true, publish: config.releases, lacking };
}

function requireStable({ version }: ReleaseConfig) {
  if (!/^\d+\.\d+\.\d+$/.test(version)) throw new Error(`${version} is not a stable version; main releases only stable versions`);
}

/** A rehearsal's plan: build the version whatever the modules have, and publish nothing. */
export function rehearsal(config: ReleaseConfig): { build: true; publish: false; lacking: string[] } {
  requireStable(config);
  return { build: true, publish: false, lacking: [] };
}

export async function release(
  modules: Release,
  config: ReleaseConfig,
  context: Omit<ReleaseContext, 'before'>,
): Promise<{ url: string; created: boolean }> {
  if (modules.at(-1) !== github) throw new Error('release needs github as the last module');
  const before = modules.slice(0, -1).map((module) => ({ label: module.label, page: module.page(config) }));
  return github.release(config, { ...context, before });
}

export async function main(
  argv: string[],
  {
    env = process.env,
    fetch: send = globalThis.fetch,
    configPath = fileURLToPath(new URL('./release.json', import.meta.url)),
    modules,
    wait = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms)),
  }: {
    env?: NodeJS.ProcessEnv;
    fetch?: Fetch;
    configPath?: string;
    modules?: Release;
    wait?: (ms: number) => Promise<unknown>;
  } = {},
): Promise<number> {
  // GitHub's API limits anonymous reads per runner address, so its reads carry the run's token.
  const fetch: Fetch = (input, init) =>
    env.GITHUB_TOKEN && String(input).startsWith('https://api.github.com/')
      ? send(input, {
          ...init,
          headers: { 'User-Agent': 'whop-sdk-release', ...init?.headers, Authorization: `Bearer ${env.GITHUB_TOKEN}` },
        })
      : send(input, init);
  let parsed: ReturnType<typeof argumentsOf>;
  try {
    parsed = argumentsOf(argv);
  } catch {
    console.error(USAGE);
    return 2;
  }
  const [command, ...extra] = parsed.positionals;
  const names = parsed.values.module;
  const commands = ['plan', 'confirm', 'release'];
  if (extra.length > 0 || !commands.includes(command) || (!modules && names.length === 0) || (command === 'confirm' && names.length > 1)) {
    console.error(USAGE);
    return 2;
  }
  const config: ReleaseConfig = JSON.parse(fs.readFileSync(configPath, 'utf8'));
  try {
    const context: ModuleContext = { fetch };
    if (command === 'confirm') {
      const [name] = names;
      if (!modules && !Object.hasOwn(MODULES, name)) throw new Error(`${name} is no module: ${Object.keys(MODULES).join(', ')}`);
      const [module] = modules ?? [MODULES[name as keyof typeof MODULES]];
      await confirm(module, config, { ...context, attempts: 30, wait });
      console.log(`${module.label} has ${config.package} ${config.version}: ${module.page(config)}`);
      return 0;
    }
    modules ??= releaseOf(names);
    const page = modules[0].page(config);
    const rehearse = env.REHEARSE === 'true';
    if (command === 'plan') {
      const { build, publish, lacking } = rehearse ? rehearsal(config) : await plan(modules, config, context);
      const outputs = `version=${config.version}\ntag=${config.tag}\npage=${page}\nbuild=${build}\npublish=${publish}\nrehearse=${rehearse}\n`;
      if (env.GITHUB_OUTPUT) fs.appendFileSync(env.GITHUB_OUTPUT, outputs);
      if (rehearse) {
        console.log(`${REHEARSAL} Building ${config.package} ${config.version}.`);
        return 0;
      }
      const everywhere = labels(modules.map(({ label }) => label));
      console.log(
        !build
          ? `${everywhere} already ${modules.length > 1 ? 'have' : 'has'} ${config.package} ${config.version}; nothing to publish.`
          : publish
            ? `Publishing ${config.package} ${config.version}: ${labels(lacking)} ${lacking.length > 1 ? 'do' : 'does'} not have it yet.`
            : `${DARK} Building ${config.package} ${config.version} as a release would, without publishing it to ${everywhere} at ${config.tag} (${page}).`,
      );
      return 0;
    }
    if (rehearse) {
      console.log(`${REHEARSAL} Would make sure ${config.tag} has a GitHub release; writing nothing.`);
      return 0;
    }
    if (!config.releases) {
      console.log(
        `${DARK} Would make sure ${config.tag} has a GitHub release for ${config.package} ${config.version} (${github.page(config)}); writing nothing.`,
      );
      return 0;
    }
    const sha = env.GITHUB_SHA;
    if (!sha || !env.GITHUB_TOKEN) throw new Error('release needs GITHUB_SHA and GITHUB_TOKEN');
    const { url, created } = await release(modules, config, { ...context, sha, publishedHere: env.PUBLISHED === 'true' });
    console.log(created ? `Released ${config.tag}: ${url}` : `${config.tag} is released: ${url}`);
    return 0;
  } catch (error) {
    if (!(error instanceof Error)) throw error;
    console.error(`::error::${error.message}`);
    return 1;
  }
}

function argumentsOf(argv: string[]) {
  return parseArgs({ args: argv, allowPositionals: true, options: { module: { type: 'string', multiple: true, default: [] } } });
}

if (process.argv[1] && fileURLToPath(import.meta.url) === fs.realpathSync(process.argv[1])) {
  process.exitCode = await main(process.argv.slice(2));
}
