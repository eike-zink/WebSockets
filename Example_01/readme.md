# Ein einfaches Beispiel für einen Websocket

- [Grundlage](https://websockets.readthedocs.io/en/stable/)

## Server

``` python
#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, 'localhost', 8765):
        await asyncio.Future() # run forever

asyncio.run(main())
```

## Client

``` python
#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

def hello():
    with connect('ws://localhost:8765') as websocket:
        websocket.send('Hello from Client!')
        message = websocket.recv()
        print(f'Received: {message}')

hello()
```
Der Server kann auch über einen interaktiven Client getestet werden:

``` sh
python -m websockets ws://localhost:8765/
Connected to ws://localhost:8765/.
> Hallo from Client
< Hallo from Client                                                                                                                           
Connection closed. 
```

Dieser interaktive Client kann mit ``ctrl-c` abgebrochen werden.