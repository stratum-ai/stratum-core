import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/stratum-core/__docusaurus/debug',
    component: ComponentCreator('/stratum-core/__docusaurus/debug', 'a65'),
    exact: true
  },
  {
    path: '/stratum-core/__docusaurus/debug/config',
    component: ComponentCreator('/stratum-core/__docusaurus/debug/config', '5aa'),
    exact: true
  },
  {
    path: '/stratum-core/__docusaurus/debug/content',
    component: ComponentCreator('/stratum-core/__docusaurus/debug/content', 'acf'),
    exact: true
  },
  {
    path: '/stratum-core/__docusaurus/debug/globalData',
    component: ComponentCreator('/stratum-core/__docusaurus/debug/globalData', '51e'),
    exact: true
  },
  {
    path: '/stratum-core/__docusaurus/debug/metadata',
    component: ComponentCreator('/stratum-core/__docusaurus/debug/metadata', 'df9'),
    exact: true
  },
  {
    path: '/stratum-core/__docusaurus/debug/registry',
    component: ComponentCreator('/stratum-core/__docusaurus/debug/registry', '7c0'),
    exact: true
  },
  {
    path: '/stratum-core/__docusaurus/debug/routes',
    component: ComponentCreator('/stratum-core/__docusaurus/debug/routes', '90d'),
    exact: true
  },
  {
    path: '/stratum-core/markdown-page',
    component: ComponentCreator('/stratum-core/markdown-page', 'c64'),
    exact: true
  },
  {
    path: '/stratum-core/docs',
    component: ComponentCreator('/stratum-core/docs', '3d2'),
    routes: [
      {
        path: '/stratum-core/docs',
        component: ComponentCreator('/stratum-core/docs', 'ab6'),
        routes: [
          {
            path: '/stratum-core/docs',
            component: ComponentCreator('/stratum-core/docs', '782'),
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
                path: '/stratum-core/docs/design/metrics-kpis',
                component: ComponentCreator('/stratum-core/docs/design/metrics-kpis', '13b'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/design/product-prd',
                component: ComponentCreator('/stratum-core/docs/design/product-prd', '947'),
                exact: true,
                sidebar: "docs"
              },
              {
                path: '/stratum-core/docs/design/ux-notes',
                component: ComponentCreator('/stratum-core/docs/design/ux-notes', '8ca'),
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
                path: '/stratum-core/docs/intro',
                component: ComponentCreator('/stratum-core/docs/intro', '114'),
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
