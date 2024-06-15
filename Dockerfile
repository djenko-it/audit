FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y nmap && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "flask db upgrade && python run.py"]
