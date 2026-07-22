from prompts import ESCALATION_PROMPT
from state import AgentState
from utils.logger import logger
from tools.ticket_generator import create_ticket
from utils.helpers import generate_response


def escalation_agent(state: AgentState):

    logger.info("Escalation Agent Started")

    ticket = create_ticket(
        state["query"]
    )

    logger.info(
        f"Ticket Created:{ticket["ticket_id"]}"
    )

    state["session"]["last_ticket_id"] = ticket["ticket_id"]
    state["session"]["last_agent"] = "escalation"

    state["context"] = f"""

Support Ticket Created

Ticket ID: {ticket["ticket_id"]}

status: {ticket["status"]}

Priority: {ticket["priority"]}

Created at: {ticket["created_at"]}
"""

    state["sources"] = []
    result = generate_response(
        ESCALATION_PROMPT,
        state
    )

    logger.info("Escalation Agent Finished")
    return result
