# Pull official base python Docker Image
FROM python:3.14

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.tx .
RUN pip install -r requirements.txt

# Copy te django project
COPY . .