"""
Simple AI Chatbot - Rule-Based
A beginner-friendly chatbot project suitable for B.Tech AIML students.
The chatbot responds to user input using predefined rules and patterns.
"""

import random
import string


def get_response(user_input):
    """Return a response based on the user's input using rule-based logic."""

    # Normalize the input: lowercase and strip punctuation
    cleaned = user_input.lower().strip()
    cleaned = cleaned.translate(str.maketrans("", "", string.punctuation))

    # --- Greetings ---
    greetings_input = {"hello", "hi", "hey", "good morning", "good evening", "howdy"}
    greetings_response = [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Hey! Nice to meet you. How can I assist you?",
    ]
    if cleaned in greetings_input:
        return random.choice(greetings_response)

    # --- How are you ---
    how_are_you = {"how are you", "how do you do", "how are you doing"}
    if cleaned in how_are_you:
        return "I'm just a program, but I'm doing great! Thanks for asking. 😊"

    # --- Name ---
    if "your name" in cleaned or "who are you" in cleaned:
        return "I am a simple AI chatbot created as a student project. You can call me ChatBot!"

    # --- Purpose / What can you do ---
    if "what can you do" in cleaned or "help" in cleaned:
        return (
            "I can answer basic questions, greet you, and have a simple conversation. "
            "Try asking me about Python, AI, or just say hi!"
        )

    # --- Python-related questions ---
    if "what is python" in cleaned:
        return (
            "Python is a popular, high-level programming language known for its "
            "simplicity and readability. It is widely used in AI, web development, "
            "data science, and more."
        )

    # --- AI-related questions ---
    if "what is ai" in cleaned or "what is artificial intelligence" in cleaned:
        return (
            "Artificial Intelligence (AI) is a branch of computer science that aims "
            "to create machines that can perform tasks that typically require human "
            "intelligence, such as learning, reasoning, and problem-solving."
        )

    # --- Machine Learning ---
    if "what is machine learning" in cleaned or "what is ml" in cleaned:
        return (
            "Machine Learning is a subset of AI that enables systems to learn and "
            "improve from experience without being explicitly programmed."
        )

    # --- Creator ---
    if "who made you" in cleaned or "who created you" in cleaned:
        return "I was created by a B.Tech AIML student as a learning project!"

    # --- Thanks ---
    thanks_input = {"thank you", "thanks", "thank you so much"}
    if cleaned in thanks_input:
        return "You're welcome! Happy to help. 😊"

    # --- Goodbye ---
    if cleaned == "bye":
        return None  # Signal to main loop to exit

    # --- Default fallback ---
    fallback_responses = [
        "I'm sorry, I didn't understand that. Could you rephrase?",
        "Hmm, I'm not sure about that. Try asking something else!",
        "I don't have an answer for that yet. I'm still learning!",
    ]
    return random.choice(fallback_responses)


def main():
    """Run the chatbot in the terminal."""
    print("=" * 50)
    print("   Welcome to the AI ChatBot!")
    print("   Type 'bye' to exit the chat.")
    print("=" * 50)
    print()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("ChatBot: Please type something!\n")
            continue

        response = get_response(user_input)

        if response is None:
            print("ChatBot: Goodbye! Have a great day! 👋\n")
            break

        print(f"ChatBot: {response}\n")


if __name__ == "__main__":
    main()
