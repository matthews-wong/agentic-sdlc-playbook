# Case Studies

Concrete illustrations of the [agentic SDLC](./agentic-sdlc.md) in practice, mapped back to the [patterns](./patterns/). Where a claim comes from a named product or report it is cited; where a description generalizes across sources it is labeled as a **reference architecture** (illustrative, not a single vendor's implementation).

---

## 1. GitHub Copilot coding agent — the issue-to-PR async worker

**Source:** GitHub (coding agent introduced 2025, general availability 2026; reportedly in use at ~90% of Fortune 100). See references below.

**What it does.** You assign a GitHub **Issue** to the agent. It works asynchronously in a **GitHub Actions–powered sandbox**: analyzes the issue and repo context, creates a branch, writes code, runs tests, iterates on errors, and opens a **pull request** — with no developer interaction during execution. You review the PR.

**Mapped to this playbook:**

| Element | Pattern / principle |
|---------|--------------------|
| Issue → branch → code → tests → PR | [Prompt chaining](./patterns/prompt-chaining.md) over the Build + Test stages |
| Iterating on test errors inside the sandbox | [ReAct](./agentic-workflows.md#react-reason--act) + [evaluator-optimizer](./patterns/evaluator-optimizer.md) (tests are the evaluator) |
| PR as the hand-off; human owns the merge | Human checkpoint at an irreversible/outward-facing step ([governance](./governance-and-metrics.md)) |
| Sandbox execution environment | Blast-radius containment — the agent can't touch prod directly |

**What to copy.** Anchor autonomy to existing delivery primitives (issues, branches, PRs, Actions). The agent doesn't invent a new control surface; it *slots into the one your team already reviews.* That is why it scales: the human checkpoint (PR review) was already there.

**What to watch.** Async volume can flood review. If the agent opens PRs faster than humans can meaningfully review them, the merge checkpoint degrades into rubber-stamping — exactly the failure [governance & metrics](./governance-and-metrics.md) warns about. Track **rework rate** and **human review load**, not PR count.

---

## 2. End-to-end agentic SDLC on Azure + GitHub — reference architecture

**Source basis:** Microsoft's "AI-led SDLC" writeup and Forrester's "orchestrated SDLC agents" framing (see references). Described here at the pattern level.

**Shape.** A chain of specialized agents spans the lifecycle, each gated by a human checkpoint:

```
intent ─▶ [Planner] ─▶ (approve plan)
                       ─▶ [Implementer] ─▶ PR
                                          ─▶ [Reviewer agent] ─▶ (human merge)
                                                                ─▶ [Deploy checklist agent] ─▶ (approve prod)
                                                                                              ─▶ [Operator] ─▶ telemetry ─▶ back to intent
```

**Mapped to this playbook:**
- The lifecycle chain is [orchestrator-workers](./patterns/orchestrator-workers.md) at the top, [prompt chaining](./patterns/prompt-chaining.md) within a task.
- Reviewer is a *different* agent than the implementer — [reflection across contexts](./patterns/evaluator-optimizer.md).
- Every irreversible step (merge, prod promotion) is a human gate.

**What to copy.** Coverage across **6+ stages** is where the compounding gains appear — not from making any single stage more autonomous, but from removing the manual serial hops *between* stages (see the "6+ threshold" in [agentic-sdlc.md](./agentic-sdlc.md#why-6-stages-is-the-threshold-that-matters)).

**What to watch.** Each hand-off is a place for context to be lost. Invest in the [observability trace](./governance-and-metrics.md#observability-you-cannot-govern-what-you-cannot-see) *before* extending the chain, or debugging a multi-agent failure becomes guesswork.

---

## 3. The narrow-adoption anti-case (composite)

**Shape.** A team adds a coding assistant, sees a real 30–40% lift in code output, and expects team throughput to follow. It rises **<10%**.

**Diagnosis.** Planning, testing, and release stayed manual. The bottleneck moved downstream of the one stage they automated. This is the single most common disappointing outcome reported across the 2026 sources.

**The fix isn't more coding autonomy** — it's instrumenting the delivery flow, finding the new bottleneck stage, and automating *that* (usually test/verify or review). See the "trap to avoid" in [governance & metrics](./governance-and-metrics.md#the-trap-to-avoid).

---

## References

See [references.md](./references.md) for full links. Directly relevant here:

- GitHub Copilot coding agent — [RockB guide (2026)](https://baeseokjae.github.io/posts/github-copilot-coding-agent-guide-2026/), [GitHub Actions launch coverage](https://alternativeto.net/news/2025/5/github-launches-new-copilot-agent-for-autonomous-task-management-with-github-actions/), [Copilot Desktop GA (June 17 2026)](https://windowsforum.com/windows-news.4/github-copilot-desktop-app-ga-2026-turns-ai-coding-into-a-supervised-agent-control-plane.427657/)
- Microsoft — [An AI-led SDLC with Azure and GitHub](https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896)
- Forrester — [From Code Assistants To Orchestrated SDLC Agents](https://www.forrester.com/blogs/agentic-software-development-takes-the-lead-from-code-assistants-to-orchestrated-sdlc-agents/)
