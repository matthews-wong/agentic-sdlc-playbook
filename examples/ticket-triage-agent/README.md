# Example: ticket-triage agent

A small agent that classifies an incoming ticket and dispatches it to a specialized handler — the runnable companion to [routing](../../docs/patterns/routing.md) and [parallelization](../../docs/patterns/parallelization.md).

## What it demonstrates

| Step | Pattern |
|------|---------|
| classify → dispatch to bug/feature/question handler | [Routing](../../docs/patterns/routing.md) (with a safe default on misroute) |
| a bug fans out into concurrent severity + component checks | [Parallelization](../../docs/patterns/parallelization.md) (sectioning) |

## Run it

No API key needed — defaults to a deterministic mock backend:

```bash
cd examples/ticket-triage-agent
python agent.py          # triages three sample tickets
python -m pytest -q      # 4 hermetic tests, no network
```

Run it for real against Claude:

```bash
export AGENT_BACKEND=anthropic
export ANTHROPIC_API_KEY=sk-ant-...
pip install anthropic
python agent.py
```

## Notes

- The router always has a **safe default** (`question`) so a misclassification never crashes — see the routing anti-note.
- The bug handler runs its checks in a thread pool and aggregates; each check is blind to the others, which is exactly when parallelization is appropriate.
- Same `call_model` seam as the [release-notes example](../release-notes-agent/), so the orchestration is testable without a live model.
