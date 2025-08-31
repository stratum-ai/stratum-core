import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/stratum-core/markdown-page',
    component: ComponentCreator('/stratum-core/markdown-page', 'c64'),
    exact: true
  },
  {
    path: '/stratum-core/docs',
    component: ComponentCreator('/stratum-core/docs', '8f6'),
    routes: [
      {
        path: '/stratum-core/docs',
        component: ComponentCreator('/stratum-core/docs', 'fb9'),
        routes: [
          {
            path: '/stratum-core/docs',
            component: ComponentCreator('/stratum-core/docs', 'cdb'),
            routes: [
              {
                path: '/stratum-core/docs/engineering/agents/overview',
                component: ComponentCreator('/stratum-core/docs/engineering/agents/overview', '834'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/agents/sdk-cli',
                component: ComponentCreator('/stratum-core/docs/engineering/agents/sdk-cli', '64e'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/agents/spec',
                component: ComponentCreator('/stratum-core/docs/engineering/agents/spec', '3dc'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/auth-oidc',
                component: ComponentCreator('/stratum-core/docs/engineering/auth-oidc', '2c6'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/guides/implementation-checklist',
                component: ComponentCreator('/stratum-core/docs/engineering/guides/implementation-checklist', 'fd9'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/guides/implementation-plan',
                component: ComponentCreator('/stratum-core/docs/engineering/guides/implementation-plan', '02e'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/guides/mvp-scope',
                component: ComponentCreator('/stratum-core/docs/engineering/guides/mvp-scope', 'e06'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/local-dev-setup',
                component: ComponentCreator('/stratum-core/docs/engineering/local-dev-setup', 'd6d'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/security-interfaces',
                component: ComponentCreator('/stratum-core/docs/engineering/security-interfaces', '6ee'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/security-strategy',
                component: ComponentCreator('/stratum-core/docs/engineering/security-strategy', 'dcf'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/trino-catalogs',
                component: ComponentCreator('/stratum-core/docs/engineering/trino-catalogs', 'f36'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/engineering/unstructured-data',
                component: ComponentCreator('/stratum-core/docs/engineering/unstructured-data', '027'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/enterprise/agent-orchestration',
                component: ComponentCreator('/stratum-core/docs/enterprise/agent-orchestration', '5fe'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/enterprise/governance-capabilities',
                component: ComponentCreator('/stratum-core/docs/enterprise/governance-capabilities', 'c6e'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/enterprise/overview',
                component: ComponentCreator('/stratum-core/docs/enterprise/overview', '707'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/enterprise/security-compliance',
                component: ComponentCreator('/stratum-core/docs/enterprise/security-compliance', '35d'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/buyer-faq',
                component: ComponentCreator('/stratum-core/docs/product/buyer-faq', 'd8a'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/faq',
                component: ComponentCreator('/stratum-core/docs/product/faq', '6f0'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/getting-started',
                component: ComponentCreator('/stratum-core/docs/product/getting-started', '01b'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/glossary',
                component: ComponentCreator('/stratum-core/docs/product/glossary', 'c02'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/intro',
                component: ComponentCreator('/stratum-core/docs/product/intro', '436'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/mission-statement',
                component: ComponentCreator('/stratum-core/docs/product/mission-statement', 'ba2'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/roadmap',
                component: ComponentCreator('/stratum-core/docs/product/roadmap', 'd90'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/security-overview',
                component: ComponentCreator('/stratum-core/docs/product/security-overview', '2a6'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/product/vision',
                component: ComponentCreator('/stratum-core/docs/product/vision', 'a05'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/reference/api',
                component: ComponentCreator('/stratum-core/docs/reference/api', '86d'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/reference/architecture',
                component: ComponentCreator('/stratum-core/docs/reference/architecture', '5d5'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/reference/execution-policy',
                component: ComponentCreator('/stratum-core/docs/reference/execution-policy', '5ae'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/reference/tech-stack',
                component: ComponentCreator('/stratum-core/docs/reference/tech-stack', '672'),
                exact: true,
                sidebar: "docs"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/stratum-core/',
    component: ComponentCreator('/stratum-core/', '68b'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
