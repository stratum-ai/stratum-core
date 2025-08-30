# Agents Overview: Where Development Happens

Stratum supports two complementary modes for agent development.

## Mode 1 — Bring-Your-Own Agent (Core)
- Development happens in your codebase (LangGraph, CrewAI, custom frameworks)
- You integrate Stratum via SDKs and `/describe`, `/find`, `/ask` APIs
- You own orchestration and hosting; Stratum provides the semantic layer, governance, and provenance

This is the default OSS path and should fit any stack.

## Mode 2 — Hosted Orchestrated Agents (Enterprise)
- Development happens in Stratum Enterprise’s visual builder and registry
- Drag-and-drop graph editor (retrieve → plan → verify → execute → tools)
- Managed orchestration (Temporal), policy simulation, versioning, and monitoring
- Export graphs to code (LangGraph/CrewAI) when you want to self-host

This path is for teams that want a managed runtime and UX.

## Decision Guide
- Choose Mode 1 if you already have an agent platform or need full control
- Choose Mode 2 if you want faster iteration, governance, and ops out of the box

Next:
- Core: see `agents/spec.md`, `agents/sdk-cli.md`
- Enterprise: see `../../enterprise/governance-capabilities.md`
