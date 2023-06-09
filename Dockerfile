FROM python:3.9 

ENV PYTHONUNBUFFERED 1 

RUN apt-get update && apt-get install -y \  
    postgresql-client 

RUN mkdir /app 

WORKDIR /app 

COPY req.txt /app/ 

RUN pip install --no-cache-dir -r req.txt

COPY . /app/
