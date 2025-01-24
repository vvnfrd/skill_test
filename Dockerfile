FROM python:3.12

WORKDIR /web

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .