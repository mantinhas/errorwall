FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["sh", "-c", "python input.py --hostname=$HOSTNAME --port=$PORT"]
