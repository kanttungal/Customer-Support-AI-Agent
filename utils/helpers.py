from utils.logger import logger
from config import llm
from state import AgentState


def format_chat_history(chat_history):
    """Convert chat history into readable text."""

    if not chat_history:
        return "No previous conversation."

    history = ""

    for message in chat_history:
        role = message["role"].capitalize()
        content = message["content"]
        history += f"{role}: {content}\n"

    return history


def generate_response(system_prompt: str, state: AgentState):

    logger.info("Agent Prompt Started")

    context = state.get("context", "")
    chat_history = format_chat_history(
        state.get("chat_history", [])
    )

    prompt = f"""
{system_prompt}

Conversation History:
{chat_history}

Relevant Context:
{context}

Current Customer Question:
{state["query"]}

Answer professionally and clearly.
"""

    response = llm.invoke(prompt)

    logger.info("LLM Response Generated Successfully")

    final_answer = response.content

    # Append document sources if available
    if state.get("sources"):

        final_answer += "\n\n### Sources\n"

        for src in state["sources"]:
            final_answer += f"- {src}\n"

    return {
        "final_answer": final_answer
    }