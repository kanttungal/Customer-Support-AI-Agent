from prompts import REFUND_PROMPT
from state import AgentState
from utils.helpers import generate_response
from utils.logger import logger


def refund_agent(state: AgentState):

    logger.info("Refund Agent Started")

    result = generate_response(
        REFUND_PROMPT,
        state
    )

    logger.info("Refund Agent Finished")

    return result