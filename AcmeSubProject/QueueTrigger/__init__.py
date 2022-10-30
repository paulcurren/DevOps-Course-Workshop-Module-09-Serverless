import requests, uuid, json, logging

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


    location = "uksouth"
    key = "c448482b754647dba48af83e5560ae5a"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': [language]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': subtitle
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    logging.info(f"Translation Response: {json.dumps(response)}")

    for item in response:
        for translation in item['translations']:

            # save transation to 'translated' table
            tableData = {
                "Translated": translation['text'],
                "Language": language,
                "PartitionKey": "message",
                "RowKey": rowKey,
                "SourceRowKey": sourceRowKey
            }

            messageOut.set(json.dumps(tableData))



