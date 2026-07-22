import re
from prompts import ORDER_PROMPT
from state import AgentState
from utils.helpers import generate_response
from utils.logger import logger
from tools.order_lookup import get_order_details
from tools.customer_lookup import get_customer


def extract_order_id(query:str):

    match = re.search(r"\b\d{4,10}\b",query)

    if match: 
        return match.group()
    
    return None

def order_agent(state: AgentState):
    
    logger.info("Order Agent Started")

    order_id = extract_order_id(state["query"])

    if not order_id:


        state["context"] = (
            "Customer did not provide an order ID."
            "Ask the Customer Politely to provide their order ID"

        )

        state["sources"] = []
        
        return generate_response(
            ORDER_PROMPT,
            state
        )
    
    order = get_order_details(order_id)

    if order is None:

        state["context"] = (
            f"No order exists with order ID {order_id}."

        )

        state["sources"] = []

        return generate_response(
            ORDER_PROMPT,
            state
        )
    
    customer = get_customer(order["customer_id"])
    
    if customer is None:


       state["context"] = (
       "Order exist but customer record is missing."
       )
       state["sources"] = []

       return generate_response(
           ORDER_PROMPT,
           state
       )
    
    state["session"]["last_order_id"] = order["order_id"]
    state["session"]["last_customer_id"] = customer["customer_id"]
    state["session"]["last_agent"] = "order"
    
    state["context"] = f"""

Customer Information.

Name: {customer["name"]}

Membership:{customer["membership"]}

Email: {customer["email"]}

Order Information.

Order ID: {order["order_id"]}

Product: {order["product"]}

Status: {order["status"]}

Expected Delivery:{order["delivery_date"]}
"""
    state["sources"] = []

    result = generate_response(
        ORDER_PROMPT,
        state
    )

    logger.info("Order Agent Finished")

    return result


