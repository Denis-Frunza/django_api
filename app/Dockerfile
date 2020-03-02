FROM python:3.8.1-alpine


WORKDIR /usr/src/app

ENV DJANGO_ALLOWED_HOSTS 0.0.0.0

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip3 install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt


COPY . /usr/src/app/

