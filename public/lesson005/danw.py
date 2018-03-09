# coding utf-8
"""
danw.py
This script should help me with pubsub demo.
Ref:
http://willcrichton.net/notes/gcp-job-queue/
https://github.com/willcrichton/gcp-job-queue
Demo:
ssh worker
python danw.py
"""

from google.cloud import pubsub
from google.cloud import monitoring
import subprocess as sp
import time

PROJECT = 'pubsub-197323'
TOPIC   = 'topic10'

SUBSCRIPTION = 'sub10'
BUCKET       = 'pubsub611'

def queue_empty(client):
    result = client.query(
        'pubsub.googleapis.com/subscription/num_undelivered_messages',
        minutes=1).as_dataframe()
    return result['pubsub_subscription'][PROJECT][SUBSCRIPTION][0] == 0

def dothis(id):
    sp.check_call(
        'touch {id}.txt'
        .format(id=id),
        shell=True)

def copy_to_gcs(id):
    sp.check_call(
        'gsutil mv {}.txt gs://{}/'
        .format(id, BUCKET),
        shell=True)

def handle_message(message):
    id = message.data
    dothis(id)
    copy_to_gcs(id)
    message.ack()

def main():
    print('main() is busy...')
    client       = monitoring.Client(project=PROJECT)
    subscriber   = pubsub.SubscriberClient()
    print('main() done.')
    
if __name__ == '__main__':
    main()

    
'bye'
