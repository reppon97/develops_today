# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt
COPY .docker /code/
RUN apt-get update && apt-get install make postgresql-client -y
RUN ["chmod", "+x", "wait_for_postgres.sh"]
RUN ["ls", "-la"]
ENTRYPOINT [".docker/wait_for_postgres.sh"]