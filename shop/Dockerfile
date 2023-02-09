FROM python:3.9-alpine

RUN pip install --upgrade pip
RUN pip install django
RUN pip install django-debug-toolbar

COPY . /app

WORKDIR /app

EXPOSE 8000

CMD python manage.py runserver 0:8000
