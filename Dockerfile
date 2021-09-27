# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1

# Set work directory
WORKDIR /ch-sag

# Install dependencies
COPY Pipfile Pipfile.lock /ch-sag/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /ch-sag/