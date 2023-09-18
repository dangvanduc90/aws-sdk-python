import time

import boto3
session = boto3.Session(profile_name='my-aws')
sqs = session.client('sqs', region_name='us-east-2')


queue_url = 'https://sqs.us-east-2.amazonaws.com/059713420548/DeadQueue'

while True:
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

    print("Received: %s" % message['Body'])
