FROM python:3.9-alpine
RUN apk add --no-cache wget
WORKDIR /app
COPY requirements.txt client.py .
RUN pip install --no-cache-dir -r requirements.txt
