"""A tiny triage agent: classify an incoming ticket, then dispatch to a handler.

Demonstrates two patterns from the playbook, framework-free:

  * routing          (classify -> specialized handler)   docs/patterns/routing.md
  * parallelization  (a bug fans out into concurrent checks, then aggregates)
                                                          docs/patterns/parallelization.md

Like the release-notes example, the only primitive is `call_model(prompt) -> str`,
and it defaults to a deterministic MOCK so it runs and tests offline. Set
AGENT_BACKEND=anthropic (+ ANTHROPIC_API_KEY) to run it for real.
"""

from __future__ import annotations

import concurrent.futures as cf
import os

DEFAULT_MODEL = "claude-sonnet-5"  # illustrative; see the claude-api docs for current ids

CATEGORIES = ("bug", "feature", "question")


def call_model(prompt: str) -> str:
    """Single seam between agent logic and any provider (see release-notes example)."""
    if os.environ.get("AGENT_BACKEND") == "anthropic":
        return _call_anthropic(prompt)
    return _call_mock(prompt)


def _call_anthropic(prompt: str) -> str:
    import anthropic

    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=os.environ.get("AGENT_MODEL", DEFAULT_MODEL),
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def _call_mock(prompt: str) -> str:
    text = prompt.lower()
    if "classify this ticket" in text:
        if any(w in text for w in ("crash", "error", "broken", "fails", "500")):
            return "bug"
        if any(w in text for w in ("add", "support", "would like", "feature request")):
            return "feature"
        return "question"
    if "assess severity" in text:
        return "high" if "500" in text or "crash" in text else "medium"
    if "identify the likely component" in text:
        return "api" if "api" in text or "500" in text else "unknown"
    if "draft a spec" in text:
        return "Spec: <one-paragraph spec>\nAcceptance criteria: <list>"
    if "answer using the docs" in text:
        return "See the docs section relevant to the question."
    return ""


def _handle_bug(ticket: str) -> dict:
    """Fan out independent assessments concurrently, then aggregate (parallelization)."""
    checks = {
        "severity": f"Assess severity (high/medium/low) of this bug:\n{ticket}",
        "component": f"Identify the likely component for this bug:\n{ticket}",
    }
    with cf.ThreadPoolExecutor() as pool:
        futures = {k: pool.submit(call_model, p) for k, p in checks.items()}
        result = {k: f.result().strip() for k, f in futures.items()}
    result["type"] = "bug"
    return result


def _handle_feature(ticket: str) -> dict:
    return {"type": "feature", "spec": call_model(f"Draft a spec and acceptance criteria for:\n{ticket}")}


def _handle_question(ticket: str) -> dict:
    return {"type": "question", "answer": call_model(f"Answer using the docs tool:\n{ticket}")}


HANDLERS = {"bug": _handle_bug, "feature": _handle_feature, "question": _handle_question}


def triage(ticket: str) -> dict:
    """Route the ticket to a specialized handler; default safely to 'question'."""
    category = call_model(
        f"Classify this ticket as exactly one of {list(CATEGORIES)}; reply with only the label.\n{ticket}"
    ).strip().lower()
    handler = HANDLERS.get(category, HANDLERS["question"])  # safe default on misroute
    return handler(ticket)


if __name__ == "__main__":
    examples = [
        "The API returns a 500 error when I paginate past page 3.",
        "It would be great to add dark mode support.",
        "How do I rotate my API key?",
    ]
    for t in examples:
        print(f"- {t}\n  -> {triage(t)}")
