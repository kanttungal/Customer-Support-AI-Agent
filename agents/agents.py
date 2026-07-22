from . import state
from prompts import SUPERVISOR_PROMPT
from state import AgentState
from config import llm


def supervisor_agent(state:AgentState):
    prompt = f"""
    {SUPERVISOR_PROMPT}

    user_query:
    {state["query"]}
    """
    response = llm.invoke(prompt)
    category  = response.content.strip()
    return{
        "category":category
    }