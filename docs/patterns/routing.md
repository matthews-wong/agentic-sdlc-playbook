# Routing

**Shape:** Classify the input → dispatch to a specialized handler. Separating classification from handling lets each handler be tuned (prompt, model, tools) for its category.

**Use when:** inputs fall into distinct categories that are genuinely better served separately — e.g. bug vs. feature vs. question.

**Avoid when:** there's only one kind of input (just handle it) or categories blur into each other (misroutes cost more than a single general handler).

## Sketch

```python
HANDLERS = {
    "bug":     lambda t: llm(f"Reproduce, locate, and propose a fix for this bug:\n{t}"),
    "feature": lambda t: llm(f"Draft a spec and acceptance criteria for:\n{t}"),
    "question":lambda t: llm(f"Answer using the docs tool:\n{t}", tools=["docs_search"]),
}

def route(ticket: str) -> str:
    category = llm(
        f"Classify this ticket as exactly one of {list(HANDLERS)}. "
        f"Reply with only the label.\n{ticket}"
    ).strip().lower()
    handler = HANDLERS.get(category, HANDLERS["question"])  # safe default
    return handler(ticket)
```

## Trade-offs
- **+** Each handler stays simple and specialized; easy to add a category.
- **+** Lets you send cheap inputs to a cheap model and hard ones to a strong one.
- **–** A wrong classification sends work down the wrong path — always define a safe default and log misroutes.
