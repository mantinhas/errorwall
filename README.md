# Errorwall

Simple Error Firewall that intercepts messages from an application. This error firewall detects the flag "yao" in messages

## Building

### Building errorwall docker container

```
docker build -f errorwall/Dockerfile -t errorwall errorwall/
```

### Building sample application for input

```
docker build -f sample-app/Dockerfile -t sample-app sample-app/
```

## Deployment

Firstly, create a network

```
docker network create -d bridge errorwall-net
```

### Running errorwall

```
docker run -it --rm \
    --name=errorwall \
    -p 8765:8765 \
    --network=errorwall-net \
    errorwall:latest
```

### Running sample application

```
docker run -it --rm \
    --name=sample-app \
    -e HOSTNAME=errorwall \
    -e PORT=8765 \
    --network=errorwall-net \
    sample-app:latest
```

## Cleanup

```
docker network rm errorwall-net
docker image rm errorwall
docker image rm sample-app
```
