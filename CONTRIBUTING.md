# Contributing

This is a **living, source-backed playbook** on the agentic SDLC and agentic workflows. Contributions that make it more accurate, clearer, or better-sourced are welcome.

## Principles

1. **Cite claims.** Anything factual — especially a number (2× release frequency, 96% defect reduction, etc.) — needs a source in [`docs/references.md`](./docs/references.md). Directional benchmarks must be labeled as such, not stated as guarantees.
2. **Least complexity.** The playbook preaches "use the simplest thing that works" — hold the docs to the same standard. Prefer clarity over completeness; link rather than repeat.
3. **Document the *why*.** Explain trade-offs and when *not* to do something, not just the happy path.
4. **Keep cross-links live.** Sections reference each other by relative link; if you move or rename something, fix the links.

## How to contribute

- **Fix or clarify** — open a PR directly for typos, broken links, or clearer wording.
- **Add or correct a claim** — include the source; if you're correcting a figure, say what the old one got wrong.
- **Propose new content** — open a "content suggestion" issue first so we can agree on scope and where it fits.

## Local checks before you open a PR

Docs are linted in CI (see [`.github/workflows/docs-lint.yml`](./.github/workflows/docs-lint.yml)). To catch issues locally:

```bash
# Markdown style
npx markdownlint-cli2 "**/*.md"

# Link check (relative + external)
npx lychee --no-progress "**/*.md"

# Internal #anchor links (validates cross-references resolve to real headings)
python scripts/check_links.py
```

## Style

- Markdown, sentence-case headings, relative links between docs.
- Code sketches stay framework-agnostic and minimal (see [`docs/patterns/`](./docs/patterns/)) — they illustrate a pattern, not a production implementation.
- One idea per section; if a section needs "and" to describe it, split it.

## Progress tracking

Iterative build progress and the backlog live in [`.agentic-repo-progress.md`](./.agentic-repo-progress.md). If you complete a backlog item, note it there.
