# Prompt Chaining

**Shape:** Task → step → step → step. Decompose a task into a fixed sequence of subtasks; each step's output feeds the next, with optional gates between them.

**Use when:** the decomposition is known in advance and stable, and you can check the intermediate result before spending the next step.

**Avoid when:** the steps aren't knowable up front (use [orchestrator-workers](./orchestrator-workers.md)) or inputs vary by category (use [routing](./routing.md)).

## Sketch

```python
def write_release_notes(commits: str) -> str:
    # Step 1: extract user-facing changes
    changes = llm(f"Extract only user-facing changes from these commits:\n{commits}")

    # Gate: bail early if there's nothing worth releasing
    if "no user-facing changes" in changes.lower():
        return "No release notes needed."

    # Step 2: group and rank
    grouped = llm(f"Group these changes into Added/Changed/Fixed and rank by impact:\n{changes}")

    # Step 3: render
    return llm(f"Write concise Keep-a-Changelog release notes from:\n{grouped}")
```

## Trade-offs
- **+** Most reliable and debuggable pattern; each step is inspectable.
- **+** Gates let you fail fast and cheap.
- **–** Rigid: a fixed chain can't adapt to unexpected input shapes.
