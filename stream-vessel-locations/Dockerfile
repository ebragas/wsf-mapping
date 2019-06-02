# Dockerfile for vessel location pinging app

# BUILD-USING:    docker build -t wsf-data-coll .
# RUN-USING:      docker run -v $(pwd)/data:/app/data wsf-data-coll
# INSPECT-USING:  docker run -it -v $(pwd)/data:/app/data wsf-data-coll /bin/sh

FROM python:alpine

LABEL Name=wsf-mapping Version=0.0.1

# RUN apt-get update && apt-get install -y software-properties-common python-software-properties && apt-get update
# RUN apt-get install -y python cron

WORKDIR /app
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt

ADD . /app
# ADD my-crontab /
# ADD test.py /
RUN chmod a+x /app/main.py

RUN crontab /app/crontab
ENTRYPOINT crond -f
# CMD ["python", "main.py"]
