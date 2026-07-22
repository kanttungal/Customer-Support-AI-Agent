from fastapi import FastAPI
import uuid

from graph import app
from api.models import ChatRequest, ChatResponse, Source
from memory.session_memory import memory

api = FastAPI(
    title="Customer Support AI Agent",
    version="1.0.0"
)


@api.get("/")
def home():
    return {
        "message": "Customer Support AI Agent is Running 🚀"
    }


@api.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Generate or use existing session id
    session_id = request.session_id or str(uuid.uuid4())

    # Get previous conversation
    chat_history = memory.get_history(session_id)

    # Store user message
    memory.add_message(
        session_id=session_id,
        role="user",
        content=request.query
    )

    # Create LangGraph state
    state = {
        "query": request.query,
        "category": "",
        "context": "",
        "chat_history": chat_history,
        "sources": [],
        "session": {
            "id": session_id
        },
        "final_answer": ""
    }

    # Invoke LangGraph
    result = app.invoke(state)

    answer = result.get("final_answer", "Sorry, I couldn't generate a response.")

    # Store assistant message
    memory.add_message(
        session_id=session_id,
        role="assistant",
        content=answer
    )

    # Convert sources
    formatted_sources = []

    for src in result.get("sources", []):

        if "(Page" in src:

            file_name = src.split(" (Page")[0]

            try:
                page = int(src.split("(Page ")[1].replace(")", ""))
            except:
                page = None

        else:

            file_name = src
            page = None

        formatted_sources.append(
            Source(
                source=file_name,
                page=page
            )
        )

    return ChatResponse(
        answer=answer,
        category=result.get("category", ""),
        sources=formatted_sources,
        session_id=session_id
    )