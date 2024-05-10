import asyncio
import websockets

async def echo(websocket, path):
    print("클라이언트가 연결되었습니다.")  # 클라이언트 연결 시 로그 출력
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Server received your message: {message}")

start_server = websockets.serve(echo, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
print("서버가 실행되었습니다.")  # 서버 시작 시 로그 출력
asyncio.get_event_loop().run_forever()
