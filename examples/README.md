# Examples

Runnable, framework-free agents that put the [pattern catalog](../docs/patterns/) into working code. Each is ~100 lines, has tests, and runs with **no API key** by default.

| Example | Patterns shown | Tests |
|---------|----------------|-------|
| [release-notes-agent](./release-notes-agent/) | [prompt chaining](../docs/patterns/prompt-chaining.md) + a gate + [evaluator-optimizer](../docs/patterns/evaluator-optimizer.md) | 3 |
| [ticket-triage-agent](./ticket-triage-agent/) | [routing](../docs/patterns/routing.md) + [parallelization](../docs/patterns/parallelization.md) | 4 |

## The shared design

Every example talks to the model through **one seam**:

```python
def call_model(prompt: str) -> str: ...
```

- **Default backend is a deterministic mock** — so the example and its tests run offline, and CI exercises the *orchestration logic* at zero model cost. This is the [testability lesson](../docs/evaluating-agents.md#regression-testing-under-non-determinism) made concrete: keep a seam so you can test the workflow independently of live model calls.
- **Set `AGENT_BACKEND=anthropic`** (plus `ANTHROPIC_API_KEY`, `pip install anthropic`) to run against a real Claude model.

## Run them

```bash
cd examples/<name>
python agent.py       # demo
python -m pytest -q   # tests (mock backend, no network)
```

CI runs every example's tests on each push (the `example-tests` job).

## Adding an example

1. Create `examples/<your-agent>/` with `agent.py`, `test_agent.py`, and a `README.md`.
2. Keep the single `call_model` seam and a mock backend so tests stay hermetic.
3. Map it to the [pattern(s)](../docs/patterns/) it demonstrates.
4. The `example-tests` CI job picks up any `examples/*/` directory automatically.
