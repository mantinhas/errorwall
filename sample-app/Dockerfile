FROM gramineproject/gramine:latest

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip install -r requirements.txt

RUN gramine-sgx-gen-private-key

RUN make SGX=1

ENTRYPOINT ["sh", "-c", "gramine-sgx ./python scripts/input.py --hostname=$HOSTNAME --port=$PORT"]
