FROM python:3.9-alpine
RUN apk add --no-cache wget
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .