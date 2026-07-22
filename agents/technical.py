from prompts import TECHNICAL_PROMPT
from state import AgentState
from utils.helpers import generate_response
from utils.logger import logger


def technical_agent(state: AgentState):

    logger.info("Technical Agent Started")

    result = generate_response(
        TECHNICAL_PROMPT,
        state
    )

    logger.info("Technical Agent Finished")

    return result