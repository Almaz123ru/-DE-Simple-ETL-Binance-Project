from kafka import KafkaProducer
import json
import websockets
import asyncio

async def stream_binance_data():
    uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            producer.send('market-data', value=data)

asyncio.run(stream_binance_data())