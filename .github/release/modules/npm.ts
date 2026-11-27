import { registry } from '../module.ts';

// npm's URL for a package: a scoped name keeps its @ and encodes its /.
const npmName = (name: string) => name.replace('/', '%2F');

/** npm, which the npm job uploads to with trusted publishing (./npm.yml.liquid). */
export default registry({
  label: 'npm',
  page: ({ package: name, version }) => `https://www.npmjs.com/package/${name}/v/${version}`,
  version: ({ package: name, version }) => `https://registry.npmjs.org/${npmName(name)}/${version}`,
  latest: {
    url: ({ package: name }) => `https://registry.npmjs.org/${npmName(name)}/latest`,
    read: ({ version }: { version: string }) => version,
  },
});
