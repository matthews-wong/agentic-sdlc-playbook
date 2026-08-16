# Interoperability Protocols: MCP & A2A

> Without standards, every agent-to-tool and agent-to-agent link is a bespoke integration — an N×M mess. In 2026 the field converged on a **two-layer stack**: **MCP** for how agents reach tools and context (vertical), **A2A** for how agents coordinate with each other (horizontal). This is the interoperability companion to [agentic workflows](./agentic-workflows.md).

## The two layers

| Layer | Protocol | Standardizes | Playbook analogue |
|-------|----------|--------------|-------------------|
| **Vertical** (agent ↔ world) | **MCP** (Model Context Protocol) | How an agent discovers and invokes external tools/data through authenticated, schema-based interfaces | [Tool use](./patterns/cognitive-patterns.md#tool-use), standardized |
| **Horizontal** (agent ↔ agent) | **A2A** (Agent-to-Agent) | How agents communicate, delegate capabilities, and pursue shared goals | [Multi-agent orchestration](./patterns/orchestrator-workers.md), standardized |

They're **complementary, not competing**: MCP gives an agent contextual understanding and data connectivity; A2A gives a group of agents a coordination layer. The two-layer stack — MCP for vertical tool integration, A2A for horizontal coordination — is becoming the default for enterprise agent deployments.

## MCP — agent-to-tool connectivity

- Anthropic's protocol; the **de facto standard for agent-to-tool connectivity**, with 18,000+ community-indexed servers as of 2026.
- An agent connects to an MCP server and gets a **schema-described, authenticated** set of tools/resources it can call — instead of you hand-wiring each integration.
- In playbook terms: it's the [tool use pattern](./patterns/cognitive-patterns.md#tool-use) turned into a portable interface. Write a tool once as an MCP server; any MCP-speaking agent can use it.

## A2A — agent-to-agent coordination

- Google's protocol; the leading standard for **inter-agent coordination**, with broad enterprise participation.
- Lets one agent discover another's capabilities and **delegate** work — the coordination substrate under [orchestrator-workers](./patterns/orchestrator-workers.md) and multi-agent systems, made interoperable across vendors.

## The wider landscape

- A third protocol, **ACP** (IBM / AGNTCY), also sits in production conversations.
- MCP, A2A, and ACP now sit under **Linux Foundation** oversight — the "protocol wars" gave way to **complementary layering**. Bet on the stack, not on one winner.

## Governance & security caveats

Protocols standardize *connectivity*, not *safety*. Research flags **governance gaps** — things MCP/A2A/ACP cannot themselves express (fine-grained permissions, trust constraints). So the playbook's other rules still apply on top of any protocol:

- Treat MCP tool output as **untrusted input** — the same [prompt-injection risk](./security.md#the-headline-threat-prompt-injection) rides in over a standard protocol just as easily.
- Scope each MCP server to [least privilege](./security.md#1-least-privilege); a standard interface doesn't grant standard *permission*.
- Gate high-impact A2A delegations behind the [blast-radius checkpoints](./governance-and-metrics.md#guardrails-design-for-the-blast-radius).

## What to do with this

- Building a tool your agents (or others') will reuse? Expose it as an **MCP server**.
- Coordinating multiple specialized agents, possibly across teams/vendors? Speak **A2A** rather than a private RPC.
- Either way, layer this repo's [security](./security.md) and [governance](./governance-and-metrics.md) controls on top — the protocol is the plumbing, not the policy.

## Sources

See [references.md](./references.md#interoperability-protocols). Adoption figures are directional 2026 reporting.
