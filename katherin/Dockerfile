############################################################
# Dockerfile for dev env image
# Based on an Debian Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu:16.04

# Set the file maintainer (your name - the file's author)
MAINTAINER Amir Meirbekov

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y openssl libssl-dev libssl-doc libffi-dev build-essential libpq-dev python3-dev python-pycurl python-bs4 python3 python3-pip mysql-client libmysqlclient-dev nano

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install setuptools

# Copy folder with python dependencies and install them
COPY backend/reqs/ /reqs
RUN pip3 install -r /reqs/dev.txt

# Define mounting points from external containers
VOLUME ["/www/katherin/"]