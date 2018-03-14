#!/bin/bash

# pubsub11.bash

# Ref:
#


# fail, use web: gcloud pubsub topics create topic11 sub11 --project pubsub-197323
gcloud pubsub topics publish topic11 --message "hello0" --project pubsub-197323
gcloud pubsub topics publish topic11 --message "hello1" --project pubsub-197323
gcloud pubsub topics publish topic11 --message "hello2" --project pubsub-197323
gcloud pubsub subscriptions pull --auto-ack sub11       --project pubsub-197323
exit
