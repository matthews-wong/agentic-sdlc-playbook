# Securing Agentic Systems

> When an agent with tool access processes untrusted content, a single injected sentence can behave like **remote code execution**. Security is not a layer you add later — in agentic systems it's a property of the architecture. This page is the security companion to [governance & metrics](./governance-and-metrics.md).

## Why agents are a distinct security problem

Three properties make the agentic attack surface unlike a normal app:

1. **Dynamic surface** — agents discover and invoke tools at runtime, so the set of actions isn't fixed at review time.
2. **Complex trust model** — instructions arrive from *many* sources: the system prompt, the user, the orchestrator, tool outputs, and retrieved data. The model doesn't natively know which to trust.
3. **High blast radius** — agents hold real permissions, persistent state, and external communication channels.

## The headline threat: prompt injection

Prompt injection is OWASP's **#1 LLM risk and still unsolved in 2026.** Two forms:

- **Direct** — the user tells the agent to ignore its instructions.
- **Indirect** — malicious instructions hide in content the agent *processes*: a retrieved document, a webpage, a code comment, an issue description. No malware, no stolen credentials.

The danger scales with capability: **an LLM agent with shell / fetch / filesystem / API tools + indirect injection ≈ remote code execution.** Treat every byte the agent reads as potentially adversarial input, not just the user's message.

## The defense stack

No single control solves injection; defense is layered. The three that consistently work in production:

### 1. Least privilege

Give the agent only the tools, data, and permissions its specific task needs — nothing more. This is the highest-leverage control: reporting suggests organizations enforcing least-privilege agent access saw far lower incident rates than those without it (directional — see the caveat below).

### 2. Sandboxing

Run tool execution — code, filesystem, network — in **isolated containers with restricted access**. The key property: the sandbox enforces limits at the *infrastructure* level, so they hold **regardless of what the agent was instructed to do.** Don't rely on the model choosing to comply; make non-compliance impossible.

### 3. Tool-use governance

- **Validate tool output before it re-enters context** — treat it as untrusted data, not trusted instruction.
- **Human confirmation for high-impact operations** — delete, send, deploy, transfer, spend. This is exactly the [blast-radius gate](./governance-and-metrics.md#guardrails-design-for-the-blast-radius) from the governance page, applied to security.
- **Segment context regions** — keep system prompt, user input, and tool/retrieved output in distinguishable regions so the model can weight them differently.

## A security checklist for agentic SDLC

- [ ] Every tool is scoped to least privilege; no "god-mode" credentials.
- [ ] Code/file/network actions run in a sandbox that constrains them independently of the prompt.
- [ ] Retrieved/tool content is treated as untrusted; it cannot silently become an instruction.
- [ ] High-impact actions (delete/send/deploy/transfer/spend) require explicit human confirmation.
- [ ] System / user / tool context are segmented, not concatenated into one trusted blob.
- [ ] Secrets are never placed in the model's context; tools hold credentials, the agent holds references.
- [ ] The [observability trace](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see) records every tool call and its arguments — your audit trail after an incident.

## Relationship to the anti-patterns

Security failures and the [anti-patterns](./anti-patterns.md) share a root: trusting the agent where you should constrain it. [Blast-radius blindness](./anti-patterns.md#8-blast-radius-blindness--same-trust-for-read-file-and-deploy-prod) *is* the security failure — uniform trust across actions of wildly different consequence.

## Sources & caveat

See [references.md](./references.md#agentic-security). Quantitative figures (e.g. least-privilege incident-rate reductions) come from industry reporting and are **directional, not guarantees** — validate against your own environment. Prefer primary sources (OWASP LLM Top 10, your model provider's safety docs) for anything you build controls on.
