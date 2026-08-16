# Prompting & Instruction Design

> [Context & memory](./context-and-memory.md) governs the *lifecycle* of what's in the window. This page is narrower and complementary: how to write the **instructions themselves** — system prompts, tool descriptions, output formats — so an agent behaves predictably. In multi-agent systems, coordination failures are almost always **prompt** failures.

## The system prompt is a runtime spec

Treat the system prompt as a **specification that dictates behavior, logic, and safety** — not a vibe. The most effective ones in 2026 are **concise, structured, and strictly enforced.** Structured instructions aren't cosmetic: reporting suggests agents given them complete tasks materially faster and at higher quality than agents handed open-ended prompts.

## Structure it like an operations runbook

An agent prompt defines a decision system: **what tools exist, when to use each, when to stop, and what to do when the right action is unclear.** Lay it out accordingly:

1. **Goal** — the outcome, unambiguously.
2. **Numbered steps with decision points** — so the agent executes methodically instead of improvising.
3. **Tool policy** — which tool for which situation.
4. **Stop conditions** — when the task is done, and when to give up / escalate ([reliability](./reliability-and-recovery.md#when-to-stop-and-escalate-to-a-human)).
5. **Constraints & safety invariants** — pinned so [compaction can't quietly drop them](./context-and-memory.md#compaction-necessary-and-quietly-dangerous).

## Ask for reasoning before action

Instruct the agent to emit a **reasoning/plan block before its tool-call or answer block.** This triggers chain-of-thought and measurably improves decisions — and it doubles as [observability](./observability.md): you can see *why* it chose an action, not just what it did. This is the [ReAct](./patterns/cognitive-patterns.md#react-reason--act) format made a house rule.

## Structured output

Define the **exact** output shape — ideally a JSON schema or a strict template — so downstream code can parse and integrate it reliably. Free-form prose is fine for humans; anything a program consumes should be schema-constrained. (This is also what makes deterministic [evals](./evaluating-agents.md) on the output possible.)

## Tool descriptions are prompts too

An agent decides whether to call a tool almost entirely from its **description and schema**. So:

- Write tool descriptions for a reader who has never seen the tool: what it does, when to use it, when *not* to.
- Name parameters for intent; document units and constraints.
- **Iterate from observed behavior** — if the agent skips a tool or misuses it, the fix is usually the description, not the model. (Anthropic's guidance: write, then improve, tools *using* agents.)

## Segment the context regions

Keep **system prompt / user input / tool output** in distinguishable regions rather than concatenated into one trusted blob. This is both a clarity win and a [security control](./security.md#3-tool-use-governance) — it's how the model can down-weight untrusted tool/retrieved content instead of treating it as instruction.

## Multi-agent: write the handoffs explicitly

Coordination failures are prompt failures. If agents don't know **how to hand off work and how to resolve conflicts, they improvise.** For each agent, specify what it receives, what it returns, whom it hands to, and what to do on disagreement — the prompt-level complement to [A2A](./protocols-mcp-a2a.md) coordination.

## A prompting checklist

- [ ] The system prompt reads like a runbook: goal → steps → tool policy → stop conditions → constraints.
- [ ] The agent emits reasoning before acting.
- [ ] Machine-consumed output is schema/template-constrained.
- [ ] Tool descriptions say when to use *and not use* each tool; iterated from real traces.
- [ ] System / user / tool context are segmented, not merged.
- [ ] Safety invariants are pinned and restated after compaction.
- [ ] Multi-agent handoffs and conflict rules are written down, not assumed.

## Sources

See [references.md](./references.md#prompting--instruction-design). Prefer Anthropic's primary tool-writing guidance for anything you build on.
