// The release modules by name: what a language's `delivery.modules` names, and the release CLI's
// `--module` arguments.

import crates from './modules/crates.ts';
import github from './modules/github.ts';
import maven from './modules/maven.ts';
import npm from './modules/npm.ts';
import pypi from './modules/pypi.ts';
import rubygems from './modules/rubygems.ts';
import type { Release } from './module.ts';

export const MODULES = { pypi, npm, rubygems, crates, maven, github };

export type ModuleName = keyof typeof MODULES;

/**
 * The release `names` make: known modules in order, each once, ending with github, which tags the
 * version the modules before it published. The build checks a language's `delivery.modules` with it,
 * and the CLI makes the release from its `--module` arguments with it.
 */
export function releaseOf(names: readonly string[]): Release {
  if (names.length === 0) throw new Error('a release names at least one module');
  const unknown = names.filter((name) => !Object.hasOwn(MODULES, name));
  if (unknown.length > 0) throw new Error(`a release names ${unknown.join(', ')}, which no module is: ${Object.keys(MODULES).join(', ')}`);
  const repeated = names.filter((name, index) => names.indexOf(name) !== index);
  if (repeated.length > 0) throw new Error(`a release names ${[...new Set(repeated)].join(', ')} more than once`);
  if (names.at(-1) !== 'github') throw new Error('a release ends with github: it tags the version the modules before it published');
  return names.map((name) => MODULES[name as ModuleName]);
}
