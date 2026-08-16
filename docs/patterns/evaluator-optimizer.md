# Evaluator-Optimizer

**Shape:** A generator produces a result; an evaluator critiques it against explicit criteria; the generator revises. Loop until the evaluator is satisfied or a budget is hit. This is **reflection made structural** — and it works best when the evaluator is a *different* context than the generator.

**Use when:** you have clear evaluation criteria *and* iteration measurably improves the output — e.g. code that must pass tests, a translation that must preserve tone.

**Avoid when:** you can't articulate what "better" means. Without an evaluation signal, the loop has nothing to optimize against and just burns tokens.

## Sketch

```python
def generate_until_good(task: str, max_rounds: int = 3) -> str:
    draft = llm(f"Complete this task:\n{task}")
    for _ in range(max_rounds):
        verdict = llm(
            "You are a strict reviewer. Evaluate the draft against the task. "
            "If it fully meets the criteria, reply exactly 'APPROVED'. "
            f"Otherwise list concrete, actionable fixes.\n\nTASK:\n{task}\n\nDRAFT:\n{draft}"
        )
        if verdict.strip() == "APPROVED":
            break
        draft = llm(f"Revise the draft to address this feedback:\n{verdict}\n\nDRAFT:\n{draft}")
    return draft
```

## Trade-offs

- **+** Large quality gains on tasks with a checkable target; catches first-draft errors cheaply.
- **+** A separate-context evaluator is far less likely to rubber-stamp than self-review.
- **–** Needs a hard round/budget cap or it can loop indefinitely.
- **–** Only as good as the criteria — a vague evaluator produces vague improvement.
