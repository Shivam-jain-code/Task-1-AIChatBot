# Task-1-AIChatBot

A simple AI chatbot built with Python and NLTK. The chatbot uses rule-based
logic with basic NLP (tokenization) to understand user input and respond
accordingly. It can handle greetings, answer common questions, tell jokes, and
more.

## Features

- Interactive terminal-based conversation
- Greeting detection and responses
- Keyword-based question answering (name, weather, age, jokes, Python, AI, …)
- Graceful exit when the user types **bye**
- Built with beginner-friendly Python code

## Project Structure

```
Task-1-AIChatBot/
├── chatbot.py          # Main chatbot script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Shivam-jain-code/Task-1-AIChatBot.git
   cd Task-1-AIChatBot
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Chatbot

```bash
python chatbot.py
```

Type your messages and press **Enter**. Type **bye** to exit.

### Example Conversation

```
ChatBot: Hi! I'm ChatBot. Type 'bye' to exit.
--------------------------------------------------
You: Hello
ChatBot: Hi there! How can I help you?
You: Tell me a joke
ChatBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: What is AI?
ChatBot: AI is a fascinating field! It includes machine learning, NLP, and much more.
You: bye
ChatBot: Goodbye! Have a great day!
```