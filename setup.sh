#!/bin/bash

# This is the setup for ubuntu

apt-get update && apt-get upgrade && apt-get dist-upgrade -y
apt-get install -y curl 
# opencv dependecy libs
apt-get install -y libsm6 libxext6 libxrender-dev
apt-get install -y python python-pip
pip install opencv-python



# download coco_v1
mkdir model
cd model
http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_11_06_2017.tar.gz
