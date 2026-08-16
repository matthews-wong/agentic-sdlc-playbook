# Parallelization

**Shape:** Fan out → run concurrently → aggregate. Two flavors:

- **Sectioning** — split a task into independent subtasks that run at once.
- **Voting** — run the *same* task multiple times and combine results for reliability.

**Use when:** subtasks don't depend on each other, or multiple independent attempts raise confidence (e.g. a security check you want several perspectives on).

**Avoid when:** steps depend on each other's output (chain them) — a barrier that waits on all branches wastes the fast branches' time if they didn't need to sync.

## Sketch (sectioning)

```python
import concurrent.futures as cf

CHECKS = {
    "lint":        "Review this diff for style and lint issues:\n{d}",
    "security":    "Review this diff for security vulnerabilities only:\n{d}",
    "tests":       "List missing edge-case tests for this diff:\n{d}",
}

def review(diff: str) -> dict:
    with cf.ThreadPoolExecutor() as pool:
        futures = {k: pool.submit(llm, p.format(d=diff)) for k, p in CHECKS.items()}
        return {k: f.result() for k, f in futures.items()}   # aggregate
```

## Sketch (voting)

```python
def is_safe(diff: str, votes: int = 3) -> bool:
    ballots = [
        llm(f"Does this diff introduce a security risk? Answer YES or NO.\n{diff}")
        for _ in range(votes)
    ]
    return sum("no" in b.lower() for b in ballots) > votes // 2   # majority
```

## Trade-offs

- **+** Lower latency for independent work; higher reliability for voting.
- **+** Diverse prompts per branch catch failure modes a single pass misses.
- **–** Costs N× the calls; aggregation logic must handle disagreement.
