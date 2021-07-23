FROM python:3.9.6-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY client.py add_auth_data.py /app/
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --system

CMD python client.py
