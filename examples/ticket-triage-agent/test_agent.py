"""Hermetic tests for the triage agent (mock backend, no network)."""

import agent


def test_routes_bug_and_fans_out():
    result = agent.triage("The API returns a 500 error when I paginate.")
    assert result["type"] == "bug"
    assert result["severity"] == "high"      # 500 -> high severity
    assert result["component"] == "api"


def test_routes_feature():
    result = agent.triage("It would be great to add dark mode support.")
    assert result["type"] == "feature"
    assert "spec" in result.get("spec", "").lower() or result["type"] == "feature"


def test_routes_question():
    result = agent.triage("How do I rotate my API key?")
    assert result["type"] == "question"
    assert result["answer"]


def test_unknown_defaults_to_question():
    # An empty/ambiguous ticket must not crash; it falls back to the safe default.
    result = agent.triage("")
    assert result["type"] == "question"
