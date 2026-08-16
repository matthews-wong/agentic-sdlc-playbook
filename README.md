# Agentic SDLC Playbook

> A practical, source-backed guide to running the software development lifecycle with AI agents — and to designing the agentic workflows that power it.

[![Docs](https://img.shields.io/badge/docs-playbook-blue)](./docs)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/status-living%20document-brightgreen)](./.agentic-repo-progress.md)

This repository is a **living knowledge base** for two tightly-related ideas:

1. **Agentic SDLC** — what changes when AI agents do real work across planning, coding, review, deployment, and operations, under human oversight.
2. **Agentic workflows** — the design patterns (reflection, tool use, planning, ReAct, and multi-agent orchestration) that make those agents reliable enough to trust.

It is written for engineering leaders and hands-on builders who want more than hype: concrete definitions, patterns with trade-offs, a governance model, and metrics that tell you whether any of it is actually working.

## Why this exists

Coding assistants improved raw code output by 30–40%, yet most teams saw overall productivity rise **less than 10%** — because planning, testing, and release stayed manual. The leverage is not in autocompleting functions; it is in re-shaping the *whole* lifecycle around agents with clear guardrails. This playbook is about that shift.

## Contents

| Guide | What it covers |
|-------|----------------|
| [Agentic SDLC](./docs/agentic-sdlc.md) | The lifecycle stage by stage, agent roles, human review checkpoints, and how it differs from AI-assisted coding |
| [Agentic Workflows](./docs/agentic-workflows.md) | The core pattern catalog: reflection, tool use, planning, ReAct, and the five orchestration workflows; when *not* to build an agent |
| [Governance & Metrics](./docs/governance-and-metrics.md) | Guardrails, observability, human-in-the-loop design, and the metrics that prove value |
| [Pattern Catalog](./docs/patterns/) | Each orchestration workflow with a minimal, framework-agnostic code sketch |
| [Case Studies](./docs/case-studies.md) | Real & reference-architecture examples (GitHub Copilot coding agent, end-to-end Azure+GitHub SDLC) mapped to the patterns |
| [Tooling Landscape](./docs/tooling-landscape.md) | Agent-building frameworks vs. SDLC agent products, and criteria for choosing between them |
| [References](./docs/references.md) | Every source cited across the playbook |

## The one-paragraph version

An **agentic workflow** orchestrates an LLM and tools through code paths *you* define — it is deterministic and predictable. An **agent** dynamically directs its own steps and tool use — more capable, less predictable. The **agentic SDLC** is what you get when you compose these across the delivery lifecycle: agents pursue multi-step goals between defined human checkpoints, while you set intent and review results. Start with the simplest thing that works, add autonomy only when a measured need appears, and invest early in governance and observability — because the production failures of 2024–2026 were overwhelmingly *architectural*, not model-quality, failures.

## How this repo is maintained

This is an iteratively-built playbook. Progress and the next planned additions are tracked in [`.agentic-repo-progress.md`](./.agentic-repo-progress.md). Each pass deepens a section or adds a new one; corrections and PRs are welcome.

## License

[MIT](./LICENSE)
