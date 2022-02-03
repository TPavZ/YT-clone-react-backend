#version with python
FROM python:3

#new directory inside container to save changes to
WORKDIR /usr/src/app

#environmental variables
ENV PYTHONDONTWRITEBYCODE=1 
ENV PYTHONBUFFERED=1

#copy requiremenents.txt
COPY requirements.txt ./

#install dependencies
RUN pip install -r requirements.txt
RUN adduser -u 1234 --disabled-password nonroot-user
USER nonroot-user

#copy other app files
COPY ./ ./
