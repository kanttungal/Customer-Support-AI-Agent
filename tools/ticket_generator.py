import json
import uuid
from datetime import datetime


TICKET_DB = "database/tickets.json"

def create_ticket(customer_query:str):

    """
    Create a new support ticket.
    """

    try:
        with open(TICKET_DB,"r") as f:
            tickets = json.load(f)
    
    except Exception:
        tickets = []

    ticket = {

        "ticket_id": str(uuid.uuid4())[:8].upper(),

        "query": customer_query,

        "status": "OPEN",

        "priority": "MEDIUM",

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }
    tickets.append(ticket)
    with open(TICKET_DB,"w") as f:
        json.dump(
            tickets,
            f,
            indent = 4
        )
    return ticket