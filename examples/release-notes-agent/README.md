# Example: release-notes agent

A ~100-line, framework-free agent that turns raw commit messages into release notes — the "show me it running" companion to the [pattern catalog](../../docs/patterns/).

## What it demonstrates

| Step | Pattern |
|------|---------|
| extract → group → render | [Prompt chaining](../../docs/patterns/prompt-chaining.md) |
| bail if nothing is releasable | A gate |
| a reviewer critiques until `APPROVED` | [Evaluator-optimizer](../../docs/patterns/evaluator-optimizer.md) (reflection by a separate reviewer) |

The whole agent talks to the model through **one** primitive — `call_model(prompt) -> str`. That's the playbook's point made concrete: these patterns are a few lines of code, not a framework.

## Run it

No API key needed — it defaults to a deterministic **mock** backend:

```bash
cd examples/release-notes-agent
python agent.py          # prints release notes from a sample commit list
python -m pytest -q      # 3 hermetic tests, no network
```

Run it for real against Claude:

```bash
export AGENT_BACKEND=anthropic
export ANTHROPIC_API_KEY=sk-ant-...
export AGENT_MODEL=claude-sonnet-5   # optional; see the claude-api docs for current ids
pip install anthropic
python agent.py
```

## Why a mock backend?

So the example is **runnable and testable anywhere**, and so CI can exercise the *workflow logic* without a live model. It's also a small lesson from [governance & metrics](../../docs/governance-and-metrics.md): keep a deterministic seam so you can test agent orchestration independently of model calls.
