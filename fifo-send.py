import time

import boto3

session = boto3.Session(profile_name='my-aws')
sqs = session.client('sqs', region_name='us-east-2')

queue_url = 'https://sqs.us-east-2.amazonaws.com/059713420548/DeadQueue.fifo'

message_count = 0

while True:
    print('sending message #' + str(message_count))
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='message #' + str(message_count),
        MessageGroupId='groupId1'
    )
    print(response)
    message_count += 1
    time.sleep(1)
    if message_count == 10:
        break
