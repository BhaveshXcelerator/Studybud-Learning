FROM python:3.11

RUN mkdir /app
WORKDIR /app

COPY . /app/
RUN pip install -r /app/requirements.txt