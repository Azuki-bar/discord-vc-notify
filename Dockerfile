FROM python:3.9.6-slim-buster

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /app

COPY code/client.py code/add_auth_data.py /app/
COPY Pipfile Pipfile.lock /app/
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    gcc \
    linux-libc-dev \
    libc6-dev \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*
RUN pip install pipenv && pipenv install --system

CMD python client.py
