"""Tests for chatbot.py helper functions."""

from chatbot import generate_response, get_tokens, normalize


def test_normalize_lowercases():
    assert normalize("Hello World") == "hello world"


def test_normalize_strips_punctuation():
    assert normalize("Hello, World!") == "hello world"


def test_get_tokens_returns_set():
    tokens = get_tokens("hello world")
    assert isinstance(tokens, set)
    assert "hello" in tokens
    assert "world" in tokens


def test_greeting_response():
    for word in ("hello", "hi", "hey"):
        resp = generate_response(word)
        assert resp is not None
        assert isinstance(resp, str)


def test_name_response():
    resp = generate_response("what is your name")
    assert "ChatBot" in resp


def test_how_are_you_response():
    resp = generate_response("how are you")
    assert resp in [
        "I'm doing great, thank you for asking!",
        "I'm fine! How about you?",
    ]


def test_age_response():
    resp = generate_response("how old are you")
    assert "age" in resp.lower() or "don't have" in resp.lower()


def test_joke_response():
    resp = generate_response("tell me a joke")
    assert "programmers" in resp.lower() or "python" in resp.lower()


def test_ai_response():
    resp = generate_response("what is AI")
    assert "ai" in resp.lower() or "artificial" in resp.lower()


def test_default_response():
    resp = generate_response("xyzzy foobar")
    assert resp is not None
    assert isinstance(resp, str)


def test_bye_not_handled_by_generate_response():
    """generate_response does not handle 'bye'; that is done in the main loop."""
    resp = generate_response("bye")
    assert resp is not None
