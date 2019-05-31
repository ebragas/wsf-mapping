# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

LABEL Name=wsf-mapping Version=0.0.1
EXPOSE 3000

WORKDIR /app
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt

ADD . /app

# Using pip:
CMD ["python3", "wsf-mapping"]
