from concurrent.futures import ThreadPoolExecutor
from binance_streaming.binance_websocket import binance_producer
from spark_processing.spark_streaming import start_spark_processing

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(binance_producer)
        executor.submit(start_spark_processing)