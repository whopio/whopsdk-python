import { registry } from '../module.ts';

/** PyPI, which the pypi job uploads to with trusted publishing (./pypi.yml.liquid). */
export default registry({
  label: 'PyPI',
  page: ({ package: name, version }) => `https://pypi.org/project/${name}/${version}/`,
  version: ({ package: name, version }) => `https://pypi.org/pypi/${name}/${version}/json`,
  latest: {
    url: ({ package: name }) => `https://pypi.org/pypi/${name}/json`,
    read: ({ info }: { info: { version: string } }) => info.version,
  },
});
