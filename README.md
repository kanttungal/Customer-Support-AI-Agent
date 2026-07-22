# 🤖 Customer Support AI Agent

An Industry-Level Multi-Agent AI Customer Support System built using LangGraph, FastAPI, Streamlit, RAG, FAISS, and OpenRouter.

---

## 🚀 Features

- Multi-Agent Architecture
- Supervisor Agent
- Refund Agent
- Billing Agent
- Order Agent
- Technical Support Agent
- Escalation Agent
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- PDF Knowledge Base
- FastAPI REST API
- Streamlit Chat UI
- Session Memory
- Docker Support
- Logging
- Source Citation

---

## 🛠️ Tech Stack

- Python
- LangGraph
- LangChain
- FastAPI
- Streamlit
- FAISS
- HuggingFace Embeddings
- OpenRouter
- Docker

---

## 📂 Project Structure

Customer Support AI Agent/
│
├── agents/
│   ├── supervisor.py
│   ├── refund.py
│   ├── billing.py
│   ├── order.py
│   ├── technical.py
│   └── escalation.py
│
├── api/
│   ├── main.py
│   └── models.py
│
├── database/
│   └── orders.json
│
├── Documents/
│   ├── refund_policy.pdf
│   └── ...
│
├── db/
│   └── (FAISS index)
│
├── memory/
│   ├── chat_memory.py
│   └── session_memory.py
│
├── tools/
│   ├── rag_search.py
│   ├── order_lookup.py
│   └── ...
│
├── utils/
│   ├── helpers.py
│   └── logger.py
│
├── app.py
├── graph.py
├── config.py
├── prompts.py
├── state.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repo>
cd Customer-Support-AI-Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
```

---

## ▶️ Run FastAPI

```bash
uvicorn api.main:api --reload
```

---

## ▶️ Run Streamlit

```bash
streamlit run app.py
```

---

## 🐳 Run with Docker

```bash
docker compose build
docker compose up
```

---

## 📡 API Endpoint

### POST `/chat`

Example request:

```json
{
  "query": "What is your refund policy?"
}
```

Example response:

```json
{
  "answer": "...",
  "category": "refund",
  "session_id": "..."
}
```

---

## 🔮 Future Improvements

- Redis Session Memory
- PostgreSQL Integration
- Authentication
- Ticket Management
- Live Order Tracking API

---

## 👨‍💻 Author

**VishnuKant**

MCA Student | AI/ML Engineer | GenAI Enthusiast