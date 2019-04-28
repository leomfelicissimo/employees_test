FROM python:3.7.3-slim-stretch
ENV PYTHONUNBUFFERED 1
RUN mkdir /employees_app
WORKDIR /employees_app
COPY requirements.txt /employees_app/
RUN pip install -r requirements.txt
COPY . /employees_app/
