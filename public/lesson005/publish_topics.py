# coding utf-8
"""
publish_topics.py

This script should publish many topics to pubsub.

Ref:
http://willcrichton.net/notes/gcp-job-queue/
https://github.com/willcrichton/gcp-job-queue

Demo:
python publish_topics.py
"""

from google.cloud import pubsub
from tqdm import tqdm

PROJECT = 'pubsub-197323'
TOPIC   = 'topic10'

def main():
    publisher  = pubsub.PublisherClient()
    topic_s    = 'projects/{}/topics/{}'.format(PROJECT, TOPIC)
    worksize_i = 10
    for id in tqdm(list(range(worksize_i))):
        publisher.publish(topic_s, str(id))

if __name__ == '__main__':
    main()
