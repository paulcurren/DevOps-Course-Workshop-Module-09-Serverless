import json
import logging
import time
import uuid
import typing
import azure.functions as func


def main(req: func.HttpRequest, message: func.Out[str], msg: func.Out[typing.List[str]]) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')
    start = time.time()

    req_body = req.get_json()
    subtitle = req_body.get("subtitle")
    languages = req_body.get("languages")

    rowKey = str(uuid.uuid4())

    tableData = {
        "Translation": subtitle,
        "PartitionKey": "message",
        "RowKey": rowKey
    }

    message.set(json.dumps(tableData))
    logging.info(tableData)

    queueData = []
    for language in languages:

        queueData.append(json.dumps({
            "RowKey": rowKey,
            "Language" : language,       
        }))

    msg.set(json.dumps(queueData))
    logging.info(queueData)

    


    ## time.sleep(5) # Simulating 5 seconds of cpu-intensive processing
    end = time.time()
    processingTime = end - start

    return func.HttpResponse(
        f"Processing took {str(processingTime)} seconds. Translation is: {subtitle}",
        status_code=200
    )
