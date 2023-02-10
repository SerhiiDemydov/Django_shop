FROM python:3.9-alpine

RUN pip install --upgrade pip
RUN pip install django
RUN pip install django-debug-toolbar
RUN python -m pip install Pillow
RUN pip install gunicorn

COPY . /app

WORKDIR /app

RUN python manage.py makemigrations | python manage.py migrate


