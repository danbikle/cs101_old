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
# Use an official Python runtime as a parent image
FROM python:2.7-slim
EOF
