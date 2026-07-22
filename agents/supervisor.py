from utils.logger import logger
from config import llm
from prompts import SUPERVISOR_PROMPT
from state import AgentState


VALID_CATEGORIES = [
    "refund",
    "order",
    "billing",
    "technical",
    "escalation",
]

def supervisor_agent(state):
    logger.info("Supervisor Agent Started")
    
    prompt = f"""
{SUPERVISOR_PROMPT}

Customer Query:
{state["query"]}

Category:

"""
    try:
        response = llm.invoke(prompt)

        category = response.content.strip().lower()

        # Remove spaces/newlines
        category = category.replace("\n", "").strip()

        # Validate category
        if category not in VALID_CATEGORIES:
            logger.warning(
                f"Invalid category returned by LLM: {category}"
            )
            category = "escalation"

        logger.info(
            f"Supervisor routed query to '{category}' agent."
        )

        return {
            "category": category
        }

    except Exception as e:

        logger.error(f"Supervisor Error: {str(e)}")

        return {
            "category": "escalation"
        }


