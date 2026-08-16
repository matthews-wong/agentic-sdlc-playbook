# RAG & Grounding

> An agent that reasons over *retrieved* facts beats one reasoning from memory alone — but only if retrieval is good. [Context & memory](./context-and-memory.md) covered *when* to pull content (just-in-time); this page covers *how to make what you pull trustworthy*, and how retrieval becomes agentic.

## Why grounding matters

Grounding responses in retrieved evidence is the main lever against hallucination — RAG alone reportedly cuts hallucination by **~40–71%**, and RAG plus guardrails more in well-engineered stacks. But there's a catch worth internalizing:

> RAG doesn't remove failure — it **moves failure to the retrieval layer.** Poor chunking, weak embeddings, stale documents, or irrelevant results become the new bug surface.

So "we added RAG" is not "we fixed accuracy." You've traded a generation problem for a retrieval problem you must now engineer.

## The four levers (where the quality wins are)

### 1. Chunking
Chunk by **semantics — sections and headings — not by raw size.** Size-based chunking fragments evidence across boundaries so the right fact is never wholly in one chunk.

### 2. Hybrid retrieval
Combine **dense vector search with keyword/BM25** retrieval. Dense catches meaning; keyword catches exact terms, IDs, and rare tokens. Together they recall more than either alone.

### 3. Reranking
Run a reranker (e.g. Cohere Rerank, BGE-Reranker) over candidates so the **best chunk lands first** in the prompt — reported to cut hallucination by up to ~20% on its own. Cheap, high-leverage; also fights [context rot](./context-and-memory.md#context-rot-more-context-is-not-better) by letting you pass fewer, better chunks.

### 4. Long-context vs. RAG
Stuffing everything into a long context is not a substitute for retrieval — it's slower, costlier, and [degrades with size](./context-and-memory.md#context-rot-more-context-is-not-better). Retrieve the *relevant* slice; reserve long context for when relevance genuinely can't be narrowed.

## Grounding with citations

Require **per-claim citations** back to retrieved sources. Mandatory citations force the model to ground each assertion in evidence, make answers **verifiable**, and measurably reduce hallucination. Citations are also your [evidence-not-assertion](./governance-and-metrics.md#human-in-the-loop-design) artifact and what a human (or an [eval](./evaluating-agents.md)) checks.

## Agentic RAG

Classic RAG retrieves once, then generates. **Agentic RAG** lets the agent **plan and iterate its own searches** — essential for multi-hop questions:

1. Decompose into sub-goals ([planning](./patterns/cognitive-patterns.md#planning)).
2. Route each to the right source/tool ([routing](./patterns/routing.md)).
3. Execute retrieval (a [ReAct](./patterns/cognitive-patterns.md#react-reason--act) loop).
4. **Verify coverage** and resolve conflicting sources.
5. **Stop within a budget** ([reliability](./reliability-and-recovery.md#retry-strategy-that-doesnt-make-things-worse)).
6. Return an answer with **per-claim citations and an auditable path.**

This is [orchestrator-workers](./patterns/orchestrator-workers.md) applied to retrieval — and it inherits the same caution: log the plan and cap the loop.

## Don't forget: retrieved content is untrusted

Everything RAG pulls in is **input, not instruction.** A retrieved doc can carry an [indirect prompt injection](./security.md#the-headline-threat-prompt-injection). Keep retrieved content in a distinguishable context region and never let it silently redirect the agent.

## A RAG checklist

- [ ] Chunking is semantic (sections/headings), not fixed-size.
- [ ] Retrieval is hybrid (dense + keyword/BM25).
- [ ] A reranker puts the best chunk first; you pass few, high-quality chunks.
- [ ] Answers carry per-claim citations to sources.
- [ ] Retrieval quality is **evaluated** (it's the new failure layer) — see [evaluating agents](./evaluating-agents.md).
- [ ] Retrieved content is treated as untrusted input.
- [ ] Agentic multi-hop retrieval logs its plan and stops within a budget.

## Sources

See [references.md](./references.md#rag--grounding). Percentages are directional; measure on your corpus.
