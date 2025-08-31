/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Product',
      collapsed: false,
      items: [
        'product/intro',
        'product/getting-started',
        'product/mission-statement',
        'product/vision',
        'product/glossary',
        'product/roadmap',
        'product/security-overview',
        'product/faq',
        'product/buyer-faq',
        // Product Design is private; no public items
        {
          type: 'category',
          label: 'Enterprise',
          items: [
            'enterprise/overview',
            'enterprise/security-compliance',
            'enterprise/governance-capabilities',
            'enterprise/agent-orchestration',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: 'Engineering',
      collapsed: false,
      items: [
        'engineering/guides/mvp-scope',
        'engineering/guides/implementation-plan',
        'engineering/guides/implementation-checklist',
        {
          type: 'category',
          label: 'Setup Guides',
          items: [
            'engineering/local-dev-setup',
            'engineering/trino-catalogs',
            'engineering/auth-oidc',
          ],
        },
        {
          type: 'category',
          label: 'Security',
          items: [
            'engineering/security-strategy',
            'engineering/security-interfaces',
          ],
        },
        {
          type: 'category',
          label: 'Agents',
          items: [
            'engineering/agents/overview',
            'engineering/agents/spec',
            'engineering/agents/sdk-cli',
          ],
        },
        'engineering/unstructured-data',
        'reference/tech-stack',
        'reference/architecture',
        'reference/execution-policy',
        'reference/api',
        // metrics/kpis are private now
      ],
    },
  ],
};
