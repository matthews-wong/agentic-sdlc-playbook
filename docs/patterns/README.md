# Pattern Catalog

Minimal, framework-agnostic sketches of the agentic workflow patterns. Every sketch assumes one primitive:

```python
def llm(prompt: str, tools: list | None = None) -> str:
    """Call your model. Swap in the Claude API, an SDK, or anything else.
    Anthropic's point stands: most of these patterns are a few lines of code —
    you rarely need a framework to start."""
    ...
```

Read [../agentic-workflows.md](../agentic-workflows.md) first for the concepts; this folder is the "show me the code" companion. Patterns are ordered by increasing complexity — **use the least complex one that solves your problem.**

| Pattern | One-liner | File |
|---------|-----------|------|
| Prompt chaining | Fixed sequence of steps, gate between them | [prompt-chaining.md](./prompt-chaining.md) |
| Routing | Classify, then dispatch to a specialist | [routing.md](./routing.md) |
| Parallelization | Fan out independent work, aggregate | [parallelization.md](./parallelization.md) |
| Orchestrator-workers | Lead agent decomposes at runtime, delegates | [orchestrator-workers.md](./orchestrator-workers.md) |
| Evaluator-optimizer | Generate ↔ critique loop against criteria | [evaluator-optimizer.md](./evaluator-optimizer.md) |

The cognitive patterns — **reflection**, **tool use**, **planning**, **ReAct** — compose *inside* these workflows (e.g. evaluator-optimizer is reflection made structural; every worker here can use tools). They have their own deep-dive with code sketches: [cognitive-patterns.md](./cognitive-patterns.md).
