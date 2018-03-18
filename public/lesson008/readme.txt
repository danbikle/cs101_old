~/cs101/public/lesson008/readme.txt

This file shows some of my efforts to learn about Docker.

How I installed Docker on Ubuntu 16:

ref:
  https://docs.docker.com/install/linux/docker-ce/ubuntu/

sudo bash


apt-get remove docker docker-engine docker.io

apt-get update

apt-get install apt-transport-https ca-certificates software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   
apt-get update

apt-get install docker-ce

systemctl enable docker

docker run hello-world

usermod -aG docker bikle101

ssh bikle101@ub10

docker run hello-world


ref:
  https://docs.docker.com/get-started/

docker ps # what is docker doing now?

docker --version

docker info

docker run hello-world
docker image ls # I should see hello-world image

# image gives me many containers:
## List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq

mkdir ~/dock10
cd    ~/dock10

cat>Dockerfile<<EOF
# ref:
# https://docs.docker.com/get-started/part2/#dockerfile

# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

EOF

cat>requirements.txt<<EOF
Flask
Redis
EOF

"""
app.py
Ref:
https://docs.docker.com/get-started/part2/#the-app-itself
"""

from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
# end



docker build -t danhello .       # I can call it this
docker build -t friendlyhello .  # I can call it this too

docker image ls

docker run    -p 4000:80 friendlyhello
docker run -d -p 4000:80 friendlyhello # I can detach

docker ps
docker container ls
docker container ls -a

How to kill detached container?
A:
docker container stop id
demo:

