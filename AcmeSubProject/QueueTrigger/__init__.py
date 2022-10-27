import json
import logging
import uuid

import azure.functions as func


def main(msg: func.QueueMessage, message, messageOut: func.Out[str]) -> None:

    messageForTranslation = json.loads(message)
    queueMessage = json.loads(msg.get_body().decode('utf-8'))

    logging.info(f"Table Entity: {messageForTranslation}")
    logging.info(f"Queue Message: {queueMessage}")

    rowKey = str(uuid.uuid4())
    sourceRowKey = queueMessage['RowKey']
    subtitle = messageForTranslation['Translation']
    language = queueMessage['Language']

    tableData = {
        "Translated": subtitle.upper(),
        "Language": language,
        "PartitionKey": "message",
        "RowKey": rowKey,
        "SourceRowKey": sourceRowKey
    }

    messageOut.set(json.dumps(tableData))



