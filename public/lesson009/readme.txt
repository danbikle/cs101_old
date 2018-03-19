~/cs101/public/lesson009/readme.txt

This file describes my walkthrough of a docker tutorial.

part-1: GCP Kubernetes Create Cluster of 1 Node

I started by asking GCP to create a VM with Docker installed for me.

I did this by creating a kubernetes cluster of 1 host.

I started at this URL:

https://console.cloud.google.com/kubernetes

I clicked blue-button: "Create Cluster"

I made small changes to the form it served me:
  Ubuntu instead of "cos"
  Size 1 instead of 3

It quickly created 1-node-cluster.

After GCP created the node, I found it listed in this URL:

https://console.cloud.google.com/compute/instances


part-2: Run /bin/bash in new Docker Containers

I started by visiting this URL:

https://console.cloud.google.com/compute/instances

I found the node I create in part-1.

I clicked the SSH link to gain shell access to the node.

I entered a shell command:

sudo docker run -it ubuntu:16.04 /bin/bash

After a bit of work, Docker served me a shell prompt from a newly hatched container.

I entered a shell command:

cat /etc/lsb-release

I saw this:

root@08bfb05c6ca3:/etc# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.4 LTS"
root@08bfb05c6ca3:/etc#

I typed exit to exit the container.

I was now back inside a shell of the cluster node.

So, that was a simple demo of creating a new Docker container and then running /bin/bash inside it.

Here is a another similar demo.

I ran another Docker shell command to bring up another container with Anaconda Python in it:

sudo docker run -it continuumio/anaconda3 /bin/bash

After a bit of work, Docker served me a shell prompt from a newly hatched container.

I entered a shell command:

python

It served me a Python-3 prompt.

I entered Python commands:

import pandas as pd
from sklearn.datasets import load_boston
bos_df = pd.DataFrame(load_boston().data)
bos_df.columns = load_boston().feature_names
bos_df.describe()

The above commands worked well.

So, I could quickly gain access to a container running Anaconda Python.

I exited Python using the quit() command.

I exited the container with the shell command: "exit".

I ran another Docker shell command to bring up another container with Anaconda Python in it:

sudo docker run -it continuumio/anaconda3 /bin/bash

Instantly, Docker served me a shell prompt from a newly hatched container.

I entered a shell command:

python

Instantly, I saw a Python prompt.

I exited Python using the quit() command.

I exited the container with the shell command: "exit".

So, the initial creation of the container was slow because Docker needed to pull an "image" from the net.

But, after the image was cached locally, I could access it instantly.

So, those last two lessons showed how to create a container from an image and then run /bin/bash in the container.

A main idea to remember about Docker is that I can get one or more containers from an image.

Once I have a container, I can boot it up and then use it to support shell commands.

I reviewed the two docker commands I ran above to create containers:

sudo docker run -it ubuntu:16.04 /bin/bash
sudo docker run -it continuumio/anaconda3 /bin/bash

Both of the above commands depended on images that had been built for me by other people.

Both of the images are stored on hub.docker.com:

https://hub.docker.com/_/ubuntu/
https://hub.docker.com/r/continuumio/anaconda3/





Next, I exited the node-shell.

Finally I deleted the 1-node-cluster from a link in this URL:

https://console.cloud.google.com/kubernetes









