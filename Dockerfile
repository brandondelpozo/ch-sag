# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1

# Set work directory
WORKDIR /ch-sag

# Install dependencies
RUN apt-get update && apt-get install -y  libmariadb-dev-compat libmariadb-dev \
    build-essential libssl-dev libffi-dev \
    libxml2-dev libxslt1-dev zlib1g-dev 
    
COPY Pipfile Pipfile.lock /ch-sag/
RUN pip install pipenv && pipenv install --system

