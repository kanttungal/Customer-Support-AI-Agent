import json

CUSTOMER_DB = "database/customers.json"

def get_customer(customer_id:str):
    with open(CUSTOMER_DB,"r") as f:

        customers = json.load(f)

    for customer in customers:

        if customer["customer_id"] == customer_id:

            return customer
    return None

        