/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
module.exports = {
  docs: [
    'intro',
    'vision',
    'mvp-scope',
    'architecture',
    'api',
    'roadmap',
    'glossary',
    {
      type: 'category',
      label: 'Design',
      items: [
        'design/product-prd',
        'design/ux-notes',
        'design/metrics-kpis',
      ],
      collapsed: false,
    },
  ],
};
