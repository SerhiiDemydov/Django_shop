FROM python:3.9-alpine

RUN pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN python manage.py makemigrations | python manage.py migrate


