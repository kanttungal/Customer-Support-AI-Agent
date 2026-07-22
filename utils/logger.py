import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "customer_support.log")

logging.basicConfig(
    filename = LOG_FILE,
    level = logging.INFO,
    format = "%(asctime)s - %(Levelname)s - %(message)s"

)

logger = logging.getLogger("CustomerSupportAI")


