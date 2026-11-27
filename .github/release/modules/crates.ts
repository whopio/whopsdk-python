import { registry } from '../module.ts';

/** crates.io, which the crates job publishes the crate to with trusted publishing (./crates.yml.liquid). */
export default registry({
  label: 'crates.io',
  page: ({ package: name, version }) => `https://crates.io/crates/${name}/${version}`,
  version: ({ package: name, version }) => `https://crates.io/api/v1/crates/${name}/${version}`,
  // crates.io refuses a request without a User-Agent that says who is asking.
  init: {
    headers: { 'User-Agent': 'whop-sdk-release (https://github.com/whopio/whop-monorepo/tree/main/sdks/release)' },
  },
  latest: {
    url: ({ package: name }) => `https://crates.io/api/v1/crates/${name}`,
    read: ({ crate }: { crate: { max_stable_version: string | null } }) => crate.max_stable_version,
  },
});
