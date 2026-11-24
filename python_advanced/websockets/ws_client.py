#!/usr/bin/env python3
"""WebSocket client that sends one message to the echo server."""
import asyncio

import websockets

URI = "ws://localhost:8765"
MESSAGE = "Hello WebSocket"


async def connect_and_send(uri: str, text: str) -> str:
    """Open a connection, send text once, receive once and close."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    """Send the demo message and print the server response."""
    response = await connect_and_send(URI, MESSAGE)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
