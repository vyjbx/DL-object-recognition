#!/bin/bash

# This is the setup for ubuntu

apt-get update && apt-get update && apt-get dist-upgrade -y
# opencv dependecy libs
apt-get install -y libsm6 libxext6 libxrender-dev
apt-get install -y python python-pip
pip install opencv-python
