# QNA Bot

A simple AI chatbot built with **Python, Streamlit, LangChain, and Groq**.

You can ask questions and chat with the bot through a clean Streamlit interface. The conversation history is maintained during the session, so the bot can use previous messages while answering.

## Tech Used

* Python
* Streamlit
* LangChain
* Groq
* `openai/gpt-oss-120b`
* python-dotenv

## How to Run

Clone the repo:

```bash
git clone https://github.com/your-username/QNA-Bot.git
cd QNA-Bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run:

```bash
streamlit run app.py
```

## How it works

```text
User → Streamlit → LangChain → Groq LLM → Response
```

Chat history is stored using Streamlit's `session_state`.

## Future Improvements

* Add RAG for PDF/document Q&A
* Add streaming responses
* Add persistent chat history
* Build AI agents using LangGraph

## Author

**Raj**

Exploring **Generative AI, LangChain, LangGraph, RAG & AI Agents**.
