# /binance_streaming/binance_websocket.py
import asyncio
import websockets
import json
from kafka import KafkaProducer

def binance_producer():
    uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    async def stream_binance_data():
        async with websockets.connect(uri) as websocket:
            while True:
                data = await websocket.recv()
                producer.send('market-data', value=data)
                print(f"Sent to Kafka: {data}")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(stream_binance_data())
    loop.close()

if __name__ == "__main__":
    binance_producer()