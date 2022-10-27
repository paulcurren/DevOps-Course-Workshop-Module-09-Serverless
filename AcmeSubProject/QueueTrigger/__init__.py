import json
import logging

import azure.functions as func


def main(msg: func.QueueMessage, message) -> None:
    logging.info(f"Table Entity: {json.loads(message)}")
    logging.info(f"Queue Message: {msg.get_body().decode('utf-8')}")


