FROM ubuntu:22.04

WORKDIR /app

COPY ./scripts /app/scripts

RUN apt-get update && apt-get install -y python3 python3-pip -y git

COPY requirements.txt /app

RUN pip install -r requirements.txt






