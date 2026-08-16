# Orchestrator-Workers

**Shape:** A lead (orchestrator) agent decomposes the task **at runtime** and delegates subtasks to worker agents, then synthesizes their results. Unlike [parallelization](./parallelization.md), the subtasks are *not* known in advance — the orchestrator decides them.

**Use when:** the shape of the work depends on the input and can't be hard-coded — e.g. "implement this feature" fans out into files that only become clear after the orchestrator inspects the codebase.

**Avoid when:** you already know the subtasks (use parallelization or a prompt chain — cheaper and more predictable).

## Sketch

```python
import json, concurrent.futures as cf

def orchestrate(goal: str) -> str:
    # Orchestrator decides the subtasks dynamically
    plan = llm(
        f"Break this goal into 2-5 independent worker subtasks. "
        f'Reply as JSON list of strings.\nGoal: {goal}'
    )
    subtasks = json.loads(plan)

    # Workers execute in parallel, each with tools
    with cf.ThreadPoolExecutor() as pool:
        results = list(pool.map(
            lambda t: llm(f"Complete this subtask:\n{t}", tools=["read_file", "run_tests"]),
            subtasks,
        ))

    # Orchestrator synthesizes
    return llm(f"Synthesize these worker results into one coherent output:\n{results}")
```

## Trade-offs

- **+** Adapts to inputs whose decomposition can't be known up front.
- **+** Workers stay narrow and specialized; easy to give each the right tools.
- **–** The orchestrator now owns a control-flow decision — less predictable; log the plan it chose so runs stay debuggable.
- **–** A bad decomposition poisons everything downstream; consider an [evaluator](./evaluator-optimizer.md) on the plan itself.
