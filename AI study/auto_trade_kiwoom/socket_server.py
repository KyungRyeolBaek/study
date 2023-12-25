import json
import asyncio
import websockets


def process(data):
    data['age'] += 1
    return data

async def echo(websocket, path):
    print("클라이언트가 연결되었습니다.")  # 클라이언트 연결 시 로그 출력
    async for message in websocket:
        # JSON 문자열을 딕셔너리로 변환
        data = json.loads(message)
        data = process(data)

        print(f"Received: {data}")
        # 응답을 위한 딕셔너리 생성
        response = {"message": "Data received", "data": data}
        await websocket.send(f"Server received your message: {data}")

start_server = websockets.serve(echo, "0.0.0.0", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
print("서버가 실행되었습니다.")  # 서버 시작 시 로그 출력
asyncio.get_event_loop().run_forever()