# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

# install psycopg2
RUN apk update \
    && apk add --update python3 py-pip postgresql-dev python3-dev musl-dev cmake gcc g++ openssl-dev build-base \
    && apk add libffi-dev

# install dependencies
RUN pip install --upgrade pip
# RUN pip install uamqp

# copy project
COPY . .

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD python manage.py  runserver  0.0.0.0:${PORT}
