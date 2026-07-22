from langchain.tools import Tool

from tools.order_lookup import get_order_details
from tools.rag_search import search_documents


def order_tool(order_id):
    return get_order_details(order_id)


def rag_tool(query):
    docs = search_documents(query)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


TOOLS = [

    Tool(
        name="Order Lookup",
        func=order_tool,
        description="""
Use this tool whenever the customer asks about:

- order status
- order tracking
- delivery date
- order details

Input should be an Order ID.
"""
    ),

    Tool(
        name="Company Policy Search",
        func=rag_tool,
        description="""
Use this tool whenever the customer asks about:

- refund policy
- return policy
- shipping policy
- company rules

Input should be the customer's question.
"""
    )

]