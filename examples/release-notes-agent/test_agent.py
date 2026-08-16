"""Hermetic tests for the release-notes agent (mock backend, no network)."""

import agent


def test_happy_path_produces_sections():
    commits = (
        "feat(auth): add passkey login\n"
        "fix(api): correct off-by-one in pagination\n"
        "chore: bump dev dependencies\n"
    )
    notes = agent.generate_release_notes(commits)
    assert "Release notes" in notes
    assert "passkey login" in notes
    assert "pagination" in notes
    # Non-user-facing commit is filtered out by the extract step.
    assert "bump dev dependencies" not in notes


def test_gate_short_circuits_when_nothing_user_facing():
    commits = "chore: bump deps\ndocs: fix typo\n"
    assert agent.generate_release_notes(commits) == "No release notes needed."


def test_backend_defaults_to_mock(monkeypatch):
    monkeypatch.delenv("AGENT_BACKEND", raising=False)
    # Should not raise (no anthropic import, no API key needed).
    assert agent.call_model("Extract only user-facing changes\nCOMMITS:\nfeat: x") != ""
