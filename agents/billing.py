from prompts import BILLING_PROMPT
from state import AgentState
from utils.helpers import generate_response
from utils.logger import logger


def billing_agent(state: AgentState):

    logger.info("Billing Agent Started")

    result = generate_response(
        BILLING_PROMPT,
        state
    )

    logger.info("Billing Agent Finished")

    return result