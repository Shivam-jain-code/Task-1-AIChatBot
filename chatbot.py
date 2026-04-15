"""
Simple AI Chatbot using Python and NLTK.

This chatbot uses rule-based logic with basic NLP (tokenization) to
understand user input and provide relevant responses. It can handle
greetings, answer basic questions, and exit when the user types "bye".
"""

import random
import string

import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK data (only needed on first run)
nltk.download("punkt_tab", quiet=True)

# ── Response data ────────────────────────────────────────────────────────────

GREETING_INPUTS = {"hello", "hi", "hey", "greetings", "sup", "howdy"}

GREETING_RESPONSES = [
    "Hi there! How can I help you?",
    "Hello! What can I do for you today?",
    "Hey! Nice to chat with you.",
    "Hi! Feel free to ask me anything.",
]

# Keyword-based responses: each entry maps a set of trigger keywords to a list
# of possible replies.  The chatbot picks the first matching rule.
KEYWORD_RESPONSES = [
    {
        "keywords": {"name"},
        "responses": [
            "I'm ChatBot, your friendly AI assistant!",
            "You can call me ChatBot.",
        ],
    },
    {
        "keywords": {"old"},
        "responses": [
            "I don't have an age — I'm just a humble Python script!",
            "Age is just a number, and I don't have one!",
        ],
    },
    {
        "keywords": {"age"},
        "responses": [
            "I don't have an age — I'm just a humble Python script!",
            "Age is just a number, and I don't have one!",
        ],
    },
    {
        "keywords": {"how", "are", "you"},
        "responses": [
            "I'm doing great, thank you for asking!",
            "I'm fine! How about you?",
        ],
    },
    {
        "keywords": {"weather"},
        "responses": [
            "I'm not connected to a weather service, but I hope it's sunny where you are!",
            "I can't check the weather right now, but I hope you're having a nice day!",
        ],
    },
    {
        "keywords": {"help"},
        "responses": [
            "Sure! I can chat with you, answer basic questions, and keep you company.",
            "I'm here to help! Ask me anything.",
        ],
    },
    {
        "keywords": {"thank"},
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "No problem at all!",
        ],
    },
    {
        "keywords": {"joke"},
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the Python programmer need glasses? Because they couldn't C!",
        ],
    },
    {
        "keywords": {"python"},
        "responses": [
            "Python is a great programming language! It's beginner-friendly and very powerful.",
            "I love Python! It's the language I'm built with.",
        ],
    },
    {
        "keywords": {"ai"},
        "responses": [
            "AI is a fascinating field! It includes machine learning, NLP, and much more.",
            "Artificial Intelligence is transforming the world. Exciting times!",
        ],
    },
    {
        "keywords": {"artificial", "intelligence"},
        "responses": [
            "AI is a fascinating field! It includes machine learning, NLP, and much more.",
            "Artificial Intelligence is transforming the world. Exciting times!",
        ],
    },
]

DEFAULT_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "That's interesting! Tell me more.",
    "I don't have an answer for that yet, but I'm learning!",
    "Hmm, I'm not sure about that. Can you ask me something else?",
]

# ── Helper functions ─────────────────────────────────────────────────────────


def normalize(text):
    """Lower-case the text and strip punctuation."""
    return text.lower().translate(str.maketrans("", "", string.punctuation))


def get_tokens(text):
    """Tokenize the normalized input text into a set of words."""
    return set(word_tokenize(normalize(text)))


def generate_greeting(tokens):
    """Return a greeting response if the input contains a greeting word."""
    if tokens & GREETING_INPUTS:
        return random.choice(GREETING_RESPONSES)
    return None


def generate_response(user_input):
    """
    Produce a response for the given user input.

    The function first checks for greetings, then scans keyword-based rules,
    and falls back to a default response if nothing matches.
    """
    tokens = get_tokens(user_input)

    # Check for a greeting
    greeting = generate_greeting(tokens)
    if greeting:
        return greeting

    # Check keyword-based rules
    for rule in KEYWORD_RESPONSES:
        if rule["keywords"].issubset(tokens):
            return random.choice(rule["responses"])

    # Fallback
    return random.choice(DEFAULT_RESPONSES)


# ── Main loop ────────────────────────────────────────────────────────────────


def main():
    """Run the chatbot in an interactive terminal loop."""
    print("ChatBot: Hi! I'm ChatBot. Type 'bye' to exit.")
    print("-" * 50)

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatBot: Goodbye! Have a great day!")
            break

        if not user_input:
            continue

        if normalize(user_input) == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break

        response = generate_response(user_input)
        print(f"ChatBot: {response}")


if __name__ == "__main__":
    main()
