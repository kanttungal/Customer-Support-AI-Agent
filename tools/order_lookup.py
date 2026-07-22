import json
from utils.logger import logger


def get_order_details(order_id: str):

    logger.info(f"Searching Order : {order_id}")

    with open("database/orders.json", "r") as file:
        orders = json.load(file)

    for order in orders:

        if order["order_id"] == order_id:

            logger.info("Order Found")

            return order

    logger.warning("Order Not Found")

    return None