FROM python:3.10.13-slim

WORKDIR /app/closedqa-ja-dataset

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y git

COPY . /app/closedqa-ja-dataset

# gradio
EXPOSE 7860
