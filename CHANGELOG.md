# Changelog

All notable changes to this playbook are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This is a living
document; entries are grouped by the date they landed.

## [Unreleased]

### Added
- `docs/evaluating-agents.md` — evaluating agents: three eval layers, LLM-as-judge limits, regression testing under non-determinism, benchmarks vs. custom datasets.
- `docs/security.md` — securing agentic systems: prompt injection, least privilege, sandboxing, tool-use governance, and a checklist.
- `docs/adoption-roadmap.md` — a pragmatic 30/60/90-day rollout plan with exit criteria.
- `docs/further-reading.md` — curated reading path with why-to-read notes.
- `examples/ticket-triage-agent/` — runnable routing + parallelization agent with a mock backend and 4 tests.
- `docs/patterns/cognitive-patterns.md` — reflection, tool use, planning, ReAct with code sketches.
- `docs/glossary.md` and `docs/faq.md`.
- `examples/release-notes-agent/` — runnable prompt-chaining + evaluator-optimizer agent with a mock backend and 3 tests.
- `docs/diagrams.md` — Mermaid diagrams for the SDLC loop, orchestration workflows, and the guardrail decision tree.
- `docs/anti-patterns.md` — 10 recurring agentic failure modes.
- `docs/tooling-landscape.md` — agent-building frameworks vs. SDLC agent products, with selection criteria.
- `docs/case-studies.md` — GitHub Copilot coding agent + reference architecture, mapped to the patterns.
- `docs/patterns/` — catalog with code sketches for the five orchestration workflows.
- `CONTRIBUTING.md`, issue/PR templates, and a `docs-lint` + `example-tests` CI workflow.

### Notes
- All commits omit AI co-author trailers (per project preference).
- Quantitative figures throughout are directional benchmarks from cited industry sources, not guarantees.

## [0.1.0] - 2026-08-16

### Added
- Initial playbook: `README`, `LICENSE` (MIT), and the core guides —
  `docs/agentic-sdlc.md`, `docs/agentic-workflows.md`,
  `docs/governance-and-metrics.md`, and `docs/references.md`.
