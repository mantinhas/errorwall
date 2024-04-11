# Python websocket server that reads json requests, and if they contain the word "clap" print

import json
import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        # Parse the json message
        message = json.loads(message)
        # If the message contains the word "clap"
        if "yao" in message["message"]:
            print("yao detected")
        else:
            print("Nothing to see here")
        await websocket.send(json.dumps({"response": "Message received"}))

async def main():
    async with serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
