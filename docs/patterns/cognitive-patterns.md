# Cognitive Patterns

The five files in this catalog describe *orchestration* — how you wire calls together. This file describes the four *cognitive* patterns that run **inside** those calls: reflection, tool use, planning, and ReAct. They compose freely; the strongest agents stack several.

> A multi-agent system where each sub-agent uses reflection and tool use is orders of magnitude more capable than any single pattern alone.

## Reflection

**Idea:** the agent critiques its own output and revises before finalizing. Highest value per unit of complexity — and best when the critic is a *different* context than the author (see [self-review blindness](../anti-patterns.md#5-self-review-blindness)).

```python
def with_reflection(task: str) -> str:
    draft = llm(f"Do this task:\n{task}")
    critique = llm(f"List concrete flaws in this answer to the task.\nTASK:{task}\nANSWER:{draft}")
    return llm(f"Rewrite the answer, fixing every flaw.\nFLAWS:{critique}\nANSWER:{draft}")
```

Structural form: [evaluator-optimizer](./evaluator-optimizer.md).

## Tool use

**Idea:** the agent calls external systems — files, APIs, code execution, search — through structured invocations, so it acts on real state instead of guessing. With reflection, the most mature and predictable pattern.

```python
def answer_with_tools(question: str, tools: dict) -> str:
    # The model decides which tool to call; your code executes it and feeds the result back.
    call = llm(f"Question: {question}\nAvailable tools: {list(tools)}\n"
               "Reply with 'TOOL <name> <arg>' or 'ANSWER <text>'.")
    if call.startswith("TOOL"):
        _, name, arg = call.split(maxsplit=2)
        result = tools[name](arg)              # your code runs the tool
        return llm(f"Question: {question}\nTool {name} returned: {result}\nNow answer.")
    return call.removeprefix("ANSWER ").strip()
```

Design rule: validate tool arguments at the boundary — treat model-chosen args as untrusted input.

## Planning

**Idea:** decompose a goal into ordered subgoals, then execute and refine (Plan-Act, Plan-Act-Reflect). Powerful, but the **least mature and least predictable** cognitive pattern — gate it and log the plan it chose.

```python
def plan_and_execute(goal: str) -> list[str]:
    plan = llm(f"Break this goal into an ordered list of concrete steps.\nGOAL:{goal}")
    steps = [s for s in plan.splitlines() if s.strip()]
    results = []
    for step in steps:
        results.append(llm(f"Do this step, given prior results {results}:\n{step}"))
    return results
```

Because planning drifts, pair it with a checkpoint or an [evaluator](./evaluator-optimizer.md) on the plan itself before executing.

## ReAct (Reason + Act)

**Idea:** interleave a reasoning step and an action step in a loop, so each action is informed by the last observation. A strong default control loop for tool-using agents.

```python
def react(goal: str, tools: dict, max_steps: int = 6) -> str:
    scratchpad = ""
    for _ in range(max_steps):
        step = llm(f"GOAL:{goal}\nSCRATCHPAD:{scratchpad}\n"
                   "Think one step, then output 'ACT <tool> <arg>' or 'DONE <answer>'.")
        if step.startswith("DONE"):
            return step.removeprefix("DONE ").strip()
        _, name, arg = step.split(maxsplit=2)
        observation = tools[name](arg)
        scratchpad += f"\nThought+Act: {step}\nObs: {observation}"
    return "Gave up: step budget exhausted."   # never loop unbounded (anti-pattern #7)
```

## How they compose with orchestration

| You're building… | Reach for |
|------------------|-----------|
| A single higher-quality answer | reflection |
| An agent that must touch real systems | tool use (+ ReAct as the loop) |
| A task needing runtime decomposition | planning → [orchestrator-workers](./orchestrator-workers.md) |
| A checkable output you can iterate on | reflection → [evaluator-optimizer](./evaluator-optimizer.md) |

Every sketch here caps its loops and validates inputs — the two habits that keep cognitive patterns from becoming [anti-patterns](../anti-patterns.md).
