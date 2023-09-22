FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip \
    && apt-get install -y git 

WORKDIR /processing

COPY requirements.txt /processing
COPY verify_ades.py /processing
COPY verify_ades_config.yaml /processing
COPY utils/ utils/

RUN pip install -r requirements.txt


