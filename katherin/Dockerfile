############################################################
# Dockerfile for dev env image
# Based on an Debian Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu:16.04

# Set the file maintainer (your name - the file's author)
MAINTAINER Amir Meirbekov

ADD . /katherin

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y curl sudo
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y \
	openssl libssl-dev libssl-doc \
	libffi-dev build-essential libpq-dev \
	python3-dev python-pycurl python-bs4 \
	python3 python3-pip libmysqlclient-dev nano
RUN apt-get install -y nodejs

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install setuptools

# Copy folder with python dependencies and install them
WORKDIR /katherin/backend/reqs
RUN pip3 install -r dev.txt

# Create logs directory
RUN mkdir /logs
RUN chmod +x /katherin/entrypoint.sh

# npm install and build
WORKDIR /katherin/frontend
RUN npm install
RUN npm run build

# Define mounting points from external containers
WORKDIR /katherin
VOLUME ["/www/katherin/"]