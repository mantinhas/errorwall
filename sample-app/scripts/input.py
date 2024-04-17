# Program that reads user input and sends it as json through websocket to the server

import json
import asyncio
import websockets
import argparse

async def send_input(hostname, port):
    uri = f"ws://{hostname}:{port}"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter a message: ")
            await websocket.send(json.dumps({"message": message}))
            # Wait for the server to respond
            response = await websocket.recv()
            # Print and format the response
            print("Response: " + str({json.loads(response)["response"]}))

def parse_args():
    parser = argparse.ArgumentParser(description="Send input to the server")
    parser.add_argument("--hostname", type=str, default="localhost", help="Hostname of the server")
    parser.add_argument("--port", type=str, default="8765", help="Port of the server")
    return parser.parse_args()

def main():
    args = parse_args()
    asyncio.run(send_input(args.hostname, args.port))

main()
