from langgraph.graph import StateGraph,END
from state import AgentState
from agents.supervisor import supervisor_agent
from agents.refund import refund_agent
from agents.billing import billing_agent
from agents.order import order_agent
from agents.technical import technical_agent
from agents.escalation import escalation_agent

# Create Workflow
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("supervisor", supervisor_agent)
workflow.add_node("refund", refund_agent)
workflow.add_node("billing", billing_agent)
workflow.add_node("order", order_agent)
workflow.add_node("technical", technical_agent)
workflow.add_node("escalation", escalation_agent)

#  Entry Point
workflow.set_entry_point("supervisor")

# Routing Function
def route(state:AgentState):
    category = state.get("category","").strip().lower()

    valid = {
        "refund",
        "order",
        "billing",
        "technical",
        "escalation"
    }
    if category not in valid:
        category = "escalation"

    return category

# Conditional Routing
workflow.add_conditional_edges(
    "supervisor",
    route,
    {
        "refund":"refund",
        "order":"order",
        "technical":"technical",
        "billing":"billing",
        "escalation":"escalation",

    },
)

# End Nodes
workflow.add_edge("refund", END)
workflow.add_edge("order", END)
workflow.add_edge("technical", END)
workflow.add_edge("billing", END)
workflow.add_edge("escalation", END)

# Compile Graph
app = workflow.compile()




