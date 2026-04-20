# Task-1-AIChatBot 🤖

A simple rule-based AI chatbot built with Python. This project is designed as a beginner-friendly assignment for B.Tech AIML students.

## Features

- **Greetings** – Responds to hello, hi, hey, good morning, etc.
- **Predefined Q&A** – Answers questions about Python, AI, Machine Learning, and more.
- **Friendly conversation** – Handles "how are you", "thank you", and similar phrases.
- **Graceful exit** – Type `bye` to end the chat session.
- **Fallback responses** – Returns a helpful message when it doesn't understand the input.

## Project Structure

```
Task-1-AIChatBot/
├── chatbot.py          # Main chatbot script
├── requirements.txt    # Python dependencies (standard library only)
└── README.md           # Project documentation
```

## Prerequisites

- Python 3.7 or higher

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Shivam-jain-code/Task-1-AIChatBot.git
   cd Task-1-AIChatBot
   ```

2. **Create a virtual environment** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Linux/macOS
   venv\Scripts\activate           # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the chatbot**

   ```bash
   python chatbot.py
   ```

## Usage Example

```
==================================================
   Welcome to the AI ChatBot!
   Type 'bye' to exit the chat.
==================================================

You: hello
ChatBot: Hi there! What can I do for you?

You: what is AI?
ChatBot: Artificial Intelligence (AI) is a branch of computer science that aims
to create machines that can perform tasks that typically require human
intelligence, such as learning, reasoning, and problem-solving.

You: bye
ChatBot: Goodbye! Have a great day! 👋
```

## How It Works

The chatbot uses a **rule-based approach**:

1. User input is converted to lowercase and punctuation is removed.
2. The cleaned input is matched against predefined keyword sets and patterns.
3. A matching response is returned, or a fallback message is shown.

This approach is simple and easy to understand, making it ideal for learning the basics of chatbot development before moving on to NLP and ML-based chatbots.

## Future Improvements

- Add NLP using the **NLTK** library for better text understanding.
- Use **TF-IDF** and **cosine similarity** for smarter responses.
- Build a web interface using **Flask** or **Streamlit**.
- Integrate with an LLM API for more intelligent conversations.

## License

This project is open source and available for educational purposes.