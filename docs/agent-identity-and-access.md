# Agent Identity & Access

> [Security](./security.md) covers keeping an agent from being *tricked* (injection, sandboxing). This page covers a different axis: **who the agent *is* and what it's allowed to do.** In 2026 the consensus is that agents are a distinct identity class needing their own credentials, scope, and audit trail — and that most orgs aren't ready for it.

## Agents are a new identity class

An AI agent is **neither a human nor a traditional service account.** Its authentication has a **delegation chain** neither category captures: it acts *on behalf of* a user or system, with an identity and credentials of its own, and — critically — **its scope changes per invocation.**

Traditional non-human identities (NHIs) — service accounts, API keys, bots — are *passive*. Agents are **active, autonomous credential operators**: they create and consume NHIs at high volume, velocity, and autonomy. That's the new risk: broad-privilege, low-oversight credentials multiplying at machine speed.

## Core principles

### 1. A unique identity per agent

Assign each agent its own identity — never let it borrow a human's or share one blanket service account. Every action must be attributable to *that* agent (this is what makes the [observability trace](./observability.md) and [accountability](./governance-and-metrics.md#human-in-the-loop-design) real).

### 2. Delegation, not impersonation

The recommended pattern: the agent is a **uniquely identified principal acting on a user's behalf**, carrying an auditable delegation chain — *not* impersonating the user by reusing their credentials. Impersonation destroys attribution and blast-radius control; delegation preserves both.

### 3. Scoped, short-lived credentials

Because scope changes per invocation, credentials should be **narrow and ephemeral** — issue a short-lived, minimally-scoped token for the task at hand, not a long-lived key with broad rights. This is [least privilege](./security.md#1-least-privilege) applied across *both* scope and time.

### 4. Secrets stay out of the model's context

The agent should hold **references**, not raw secrets; a broker/vault issues scoped tokens to the tool layer at call time. Never place long-lived credentials in the prompt or memory (see [context & memory](./context-and-memory.md#just-in-time-retrieval-over-pre-loading)).

### 5. Real-time visibility and revocation

You need live inventory of which agent identities exist, what they can access, and the ability to revoke fast. Unmanaged NHIs with broad privileges and near-zero oversight are the failure mode to avoid.

## The standards are immature — don't wait for them

Emerging efforts — SPIFFE, IETF RFCs, ID-JAG, Auth.md, AIUC-1 — are **works in progress, unfinalized, or less than a year old.** Don't block on a standard: apply the principles above now (unique identity, delegation, scoped/ephemeral creds, visibility), and adopt a standard as it stabilizes. Treat this like the [protocol layering](./protocols-mcp-a2a.md) story — converging, not settled.

## How this connects

- It's the **identity dimension of [security](./security.md)**: injection defense stops a hijacked agent from *deciding* to do harm; scoped identity limits what a hijacked agent *can* do.
- Scope every [MCP server/tool](./protocols-mcp-a2a.md) to the agent's least-privilege identity — a standard connector is not standing permission.
- Attribution feeds [governance](./governance-and-metrics.md) and [compliance](./compliance-and-regulation.md) (human-oversight and audit obligations).

## An identity & access checklist

- [ ] Every agent has its own unique identity (no shared/borrowed accounts).
- [ ] Agents **delegate** (act as themselves on a user's behalf), never impersonate.
- [ ] Credentials are scoped per-invocation and short-lived.
- [ ] The agent holds references; a vault/broker issues tokens to tools at call time.
- [ ] There's live inventory + fast revocation of agent identities.
- [ ] Every agent action is attributable to its identity in the audit trail.

## Sources

See [references.md](./references.md#agent-identity--access). The space is moving fast; verify current standards before building on them.
