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
    component: ComponentCreator('/stratum-core/docs', '1cf'),
    routes: [
      {
        path: '/stratum-core/docs',
        component: ComponentCreator('/stratum-core/docs', '820'),
        routes: [
          {
            path: '/stratum-core/docs',
            component: ComponentCreator('/stratum-core/docs', '4bc'),
            routes: [
              {
                path: '/stratum-core/docs/api',
                component: ComponentCreator('/stratum-core/docs/api', '74b'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/architecture',
                component: ComponentCreator('/stratum-core/docs/architecture', '75a'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/buyer-faq',
                component: ComponentCreator('/stratum-core/docs/buyer-faq', 'adf'),
                exact: true,
                sidebar: "docs"
              },
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
                path: '/stratum-core/docs/execution-policy',
                component: ComponentCreator('/stratum-core/docs/execution-policy', '0f6'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/faq',
                component: ComponentCreator('/stratum-core/docs/faq', '314'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/getting-started',
                component: ComponentCreator('/stratum-core/docs/getting-started', '1a9'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/glossary',
                component: ComponentCreator('/stratum-core/docs/glossary', 'e54'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/implementation-checklist',
                component: ComponentCreator('/stratum-core/docs/implementation-checklist', '122'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/implementation-plan',
                component: ComponentCreator('/stratum-core/docs/implementation-plan', '097'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/intro',
                component: ComponentCreator('/stratum-core/docs/intro', '114'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/mission-statement',
                component: ComponentCreator('/stratum-core/docs/mission-statement', '607'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/mvp-scope',
                component: ComponentCreator('/stratum-core/docs/mvp-scope', '7f3'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/roadmap',
                component: ComponentCreator('/stratum-core/docs/roadmap', '317'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/security-overview',
                component: ComponentCreator('/stratum-core/docs/security-overview', 'a51'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/tech-stack',
                component: ComponentCreator('/stratum-core/docs/tech-stack', 'ba9'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/vision',
                component: ComponentCreator('/stratum-core/docs/vision', 'cb1'),
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
