import json
import asyncio
import websockets


async def hello():
    uri = "ws://59.13.29.135:8080"  # IPv4 주소를 명시적으로 사용
    async with websockets.connect(uri) as websocket:
        # 보낼 데이터의 딕셔너리
        data = {"name": "Alice", "age": 30}

        # 딕셔너리를 JSON 문자열로 변환하여 전송
        await websocket.send(json.dumps(data))
        response = await websocket.recv()
        print(f"Received from server: {response}")

asyncio.get_event_loop().run_until_complete(hello())
