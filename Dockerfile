FROM python:3.10.13-slim

WORKDIR /app/closedqa-ja-dataset

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/closedqa-ja-dataset
