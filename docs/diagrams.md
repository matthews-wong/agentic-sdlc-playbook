# Diagrams

Visual companions to the guides. GitHub renders Mermaid in Markdown natively, so these display inline on the repo.

## The agentic SDLC loop

Agents execute; humans hold the gates (◆). Operational findings feed back into the next plan.

```mermaid
flowchart LR
    intent([Human intent]) --> plan[Planner agent]
    plan --> g1{{Approve plan}}
    g1 --> build[Implementer agent]
    build --> review[Reviewer agent]
    review --> g2{{Human merge}}
    g2 --> verify[Verifier agent]
    verify --> g3{{Approve prod}}
    g3 --> deploy[Deploy agent]
    deploy --> operate[Operator agent]
    operate -. telemetry .-> intent
    classDef gate fill:#fde68a,stroke:#b45309,color:#111;
    class g1,g2,g3 gate;
```

## The five orchestration workflows

Ordered by increasing complexity — use the least complex one that solves your problem. See the [pattern catalog](./patterns/) for code.

### 1. Prompt chaining
```mermaid
flowchart LR
    in([Input]) --> s1[Step 1] --> gate{{Gate?}} --> s2[Step 2] --> s3[Step 3] --> out([Output])
```

### 2. Routing
```mermaid
flowchart LR
    in([Input]) --> c{Classify}
    c -->|bug| h1[Bug handler]
    c -->|feature| h2[Feature handler]
    c -->|question| h3[Q&A handler]
```

### 3. Parallelization
```mermaid
flowchart LR
    in([Input]) --> f((fan out))
    f --> a[Worker A]
    f --> b[Worker B]
    f --> c[Worker C]
    a --> agg((aggregate))
    b --> agg
    c --> agg
    agg --> out([Output])
```

### 4. Orchestrator-workers
```mermaid
flowchart TD
    in([Goal]) --> orch[Orchestrator<br/>decomposes at runtime]
    orch --> w1[Worker]
    orch --> w2[Worker]
    orch --> w3[Worker]
    w1 --> syn[Synthesize]
    w2 --> syn
    w3 --> syn
    syn --> out([Output])
```

### 5. Evaluator-optimizer
```mermaid
flowchart LR
    in([Task]) --> gen[Generator]
    gen --> ev{Evaluator:<br/>meets criteria?}
    ev -->|no, with feedback| gen
    ev -->|APPROVED| out([Output])
```

## Guardrails by blast radius

```mermaid
flowchart TD
    act[Agent wants to act] --> q1{Reversible?}
    q1 -->|yes| q2{Outward-facing?}
    q1 -->|no| gate[Human checkpoint]
    q2 -->|no| auto[Proceed autonomously]
    q2 -->|yes| logd[Proceed, log + easy undo]
    classDef gatec fill:#fecaca,stroke:#b91c1c,color:#111;
    class gate gatec;
```

See [governance & metrics](./governance-and-metrics.md#guardrails-design-for-the-blast-radius).
