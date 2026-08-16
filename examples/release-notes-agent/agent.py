"""A tiny, framework-free agent that turns raw commit messages into release notes.

It demonstrates three patterns from the playbook composed together, in a few
lines of plain Python — no agent framework required:

  * prompt chaining      (extract -> group -> render)          docs/patterns/prompt-chaining.md
  * a gate               (bail early if nothing is releasable)
  * evaluator-optimizer  (a reviewer critiques until APPROVED)  docs/patterns/evaluator-optimizer.md

The only primitive is `call_model(prompt) -> str`. By default it runs a
deterministic MOCK so the example (and its tests) work offline with no API key.
Set AGENT_BACKEND=anthropic (and ANTHROPIC_API_KEY) to run it for real.
"""

from __future__ import annotations

import os
import re

# A recent, capable default. Override with AGENT_MODEL. See the claude-api docs
# for current model ids; this is illustrative, not pinned advice.
DEFAULT_MODEL = "claude-sonnet-5"


def call_model(prompt: str) -> str:
    """Single seam between the agent logic and any model provider.

    Swap the backend without touching the workflow below — the whole point of
    keeping patterns as 'a few lines against one primitive'.
    """
    backend = os.environ.get("AGENT_BACKEND", "mock")
    if backend == "anthropic":
        return _call_anthropic(prompt)
    return _call_mock(prompt)


def _call_anthropic(prompt: str) -> str:
    import anthropic  # imported lazily so the mock path needs no dependency

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the env
    message = client.messages.create(
        model=os.environ.get("AGENT_MODEL", DEFAULT_MODEL),
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def _call_mock(prompt: str) -> str:
    """Deterministic stand-in so the example runs anywhere.

    It recognizes each step of the chain by a marker in the prompt and returns
    a plausible, fixed response. This is what makes the tests hermetic.
    """
    if "Extract only user-facing" in prompt:
        commits = prompt.split("COMMITS:\n", 1)[-1]
        user_facing = [
            line for line in commits.splitlines()
            if re.match(r"^(feat|fix|perf)(\(|:)", line.strip())
        ]
        return "\n".join(user_facing) if user_facing else "No user-facing changes."
    if "Group these changes" in prompt:
        body = prompt.split("CHANGES:\n", 1)[-1]
        added = [l for l in body.splitlines() if l.startswith("feat")]
        fixed = [l for l in body.splitlines() if l.startswith(("fix", "perf"))]
        out = []
        if added:
            out.append("Added:\n" + "\n".join(f"- {l}" for l in added))
        if fixed:
            out.append("Fixed:\n" + "\n".join(f"- {l}" for l in fixed))
        return "\n\n".join(out)
    if "strict reviewer" in prompt:
        # The mock reviewer approves any draft that has at least one section.
        return "APPROVED" if ("Added:" in prompt or "Fixed:" in prompt) else "Add at least one section."
    if "Render" in prompt:
        body = prompt.split("GROUPED:\n", 1)[-1]
        return f"## Release notes\n\n{body.strip()}\n"
    if "Revise" in prompt:
        return prompt.split("DRAFT:\n", 1)[-1]
    return ""


def generate_release_notes(commits: str, max_review_rounds: int = 3) -> str:
    """Chain: extract -> (gate) -> group -> render -> review loop."""
    # Step 1 — extract user-facing changes
    changes = call_model(
        "Extract only user-facing changes from these commits, one per line.\n"
        f"COMMITS:\n{commits}"
    )

    # Gate — fail fast and cheap
    if "no user-facing changes" in changes.lower():
        return "No release notes needed."

    # Step 2 — group and rank
    grouped = call_model(
        "Group these changes into Added/Fixed sections and rank by impact.\n"
        f"CHANGES:\n{changes}"
    )

    # Step 3 — render
    draft = call_model(
        "Render concise Keep-a-Changelog release notes from the grouped changes.\n"
        f"GROUPED:\n{grouped}"
    )

    # Step 4 — evaluator-optimizer loop (reflection by a separate 'reviewer')
    for _ in range(max_review_rounds):
        verdict = call_model(
            "You are a strict reviewer. If the draft is clear and complete, reply "
            "exactly 'APPROVED'. Otherwise give one concrete fix.\n"
            f"DRAFT:\n{draft}"
        )
        if verdict.strip() == "APPROVED":
            break
        draft = call_model(f"Revise the draft to address: {verdict}\nDRAFT:\n{draft}")

    return draft


if __name__ == "__main__":
    sample = (
        "feat(auth): add passkey login\n"
        "fix(api): correct off-by-one in pagination\n"
        "chore: bump dev dependencies\n"
        "perf(db): cache hot query results\n"
        "docs: tweak README wording\n"
    )
    print(generate_release_notes(sample))
