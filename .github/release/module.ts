// What a release module is: one place a version is published.

/** What release.json holds: what the modules read. */
export interface ReleaseConfig {
  package: string;
  version: string;
  tag: string;
  /** The SDK repo, `owner/repo`. */
  repository: string;
  /** false ships the repo dark (`delivery.releases` in whop-monorepo's define.ts). */
  releases: boolean;
}

export type Fetch = typeof fetch;

/** What every module reads beyond release.json: the network. */
export interface ModuleContext {
  fetch: Fetch;
}

/** One place a release publishes the version: what plan asks it, and what its job's confirm waits for. */
export interface ReleaseModule {
  label: string;
  page: (config: ReleaseConfig) => string;
  has: (config: ReleaseConfig, context: ModuleContext) => Promise<boolean>;
  /** The newest version published here, if any: main never releases a version behind it. */
  latest: (config: ReleaseConfig, context: ModuleContext) => Promise<string | undefined>;
}

export type Release = readonly ReleaseModule[];

/** Thrown when a registry cannot say whether a version is published. */
class ModuleError extends Error {
  readonly status: number;

  constructor(message: string, status: number) {
    super(message);
    this.status = status;
  }
}

/** `a`, `a and b`, `a, b and c`. */
export function labels(names: string[]): string {
  return names.length <= 1 ? (names[0] ?? '') : `${names.slice(0, -1).join(', ')} and ${names.at(-1)}`;
}

export function compareVersions(a: string, b: string): number {
  const parts = (version: string) => {
    const match = /^(\d+)\.(\d+)\.(\d+)/.exec(version);
    if (!match) throw new Error(`cannot compare ${version} with a version`);
    return match.slice(1).map(Number);
  };
  const [left, right] = [parts(a), parts(b)];
  return left.map((part, index) => part - right[index]).find((difference) => difference !== 0) ?? 0;
}

/** The newest stable version among `versions`, a leading v or not. */
export function highest(versions: string[]): string | undefined {
  return versions
    .map((version) => version.replace(/^v/, ''))
    .filter((version) => /^\d+\.\d+\.\d+$/.test(version))
    .sort(compareVersions)
    .at(-1);
}

/** Whether `url` is there: 200 is, 404 or 410 is not, and anything else is not a guess to make. */
export async function exists(url: string, what: string, fetch: Fetch, init?: RequestInit): Promise<boolean> {
  const response = await fetch(url, init);
  if (response.status === 200) return true;
  if (response.status === 404 || response.status === 410) return false;
  throw new ModuleError(`${url} answered ${response.status}; refusing to guess whether ${what} is published`, response.status);
}

/** A registry's latest version as JSON at `url`, which answers 404 for a package it never published. */
interface LatestJson {
  url: (config: ReleaseConfig) => string;
  read: (body: never) => string | null | undefined;
}

/**
 * A registry the module's job uploads to: its version URL answers 200 when it holds the version and
 * 404 (or 410) when it does not.
 */
export function registry({
  label,
  page,
  version,
  latest,
  init,
}: {
  label: string;
  page: (config: ReleaseConfig) => string;
  version: (config: ReleaseConfig) => string;
  latest: ((fetch: Fetch, config: ReleaseConfig) => Promise<string | undefined>) | LatestJson;
  /** What every request to the registry carries. */
  init?: RequestInit;
}): ReleaseModule {
  return {
    label,
    page,
    has: (config, { fetch }) => exists(version(config), `${config.package} ${config.version}`, fetch, init),
    async latest(config, { fetch }) {
      if (typeof latest === 'function') return latest(fetch, config);
      const response = await fetch(latest.url(config), init);
      if (response.status === 404) return undefined;
      if (!response.ok) throw new Error(`${label} answered ${response.status} for ${config.package}'s latest version`);
      return latest.read((await response.json()) as never) ?? undefined;
    },
  };
}

/**
 * Waits until `module` has the version its job just published: a registry's read API can trail the
 * upload it accepted by a minute or so, and can blip (a 5xx or 429 is not an answer yet).
 */
export async function confirm(
  module: ReleaseModule,
  config: ReleaseConfig,
  { fetch, attempts, wait }: ModuleContext & { attempts: number; wait: (ms: number) => Promise<unknown> },
): Promise<void> {
  for (let attempt = 1; !(await hasOrUnsure(module, config, fetch)); attempt++) {
    if (attempt >= attempts) throw new Error(`${module.label} does not have ${config.package} ${config.version}`);
    await wait(10_000);
  }
}

async function hasOrUnsure(module: ReleaseModule, config: ReleaseConfig, fetch: Fetch): Promise<boolean> {
  try {
    return await module.has(config, { fetch });
  } catch (error) {
    if (error instanceof ModuleError && (error.status >= 500 || error.status === 429)) return false;
    throw error;
  }
}
