import { registry } from '../module.ts';

/** RubyGems, which the rubygems job pushes the gem to with trusted publishing (./rubygems.yml.liquid). */
export default registry({
  label: 'RubyGems',
  page: ({ package: name, version }) => `https://rubygems.org/gems/${name}/versions/${version}`,
  version: ({ package: name, version }) => `https://rubygems.org/api/v2/rubygems/${name}/versions/${version}.json`,
  async latest(fetch, { package: name }) {
    // A gem RubyGems has never published answers 200 with the version "unknown".
    const response = await fetch(`https://rubygems.org/api/v1/versions/${name}/latest.json`);
    if (!response.ok) throw new Error(`RubyGems answered ${response.status} for ${name}'s latest version`);
    const { version } = (await response.json()) as { version: string };
    return version === 'unknown' ? undefined : version;
  },
});
