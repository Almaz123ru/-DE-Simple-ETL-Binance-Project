from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType
from configs.kafka_config import KAFKA_TOPIC, KAFKA_BROKER
from configs.database_config import POSTGRES_URL, POSTGRES_TABLE, POSTGRES_USER, POSTGRES_PASSWORD
#from configs.spark_config import


def process_stream():
    # Создание Spark сессии
    spark = SparkSession.builder \
        .appName("BinanceStreamProcessing") \
        .getOrCreate()

    # Настройки Kafka
    df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BROKER) \
        .option("subscribe", KAFKA_TOPIC) \
        .load()

    # Определение схемы для сообщений
    schema = StructType([
        StructField("e", StringType()),  # Event type
        StructField("E", StringType()),  # Event time
        StructField("s", StringType()),  # Symbol
        StructField("p", FloatType()),   # Price
        StructField("q", FloatType()),   # Quantity
    ])

    # Преобразование сообщений из JSON
    df = df.selectExpr("CAST(value AS STRING)")
    df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

    # Запись данных в PostgreSQL
    df.writeStream \
        .outputMode("append") \
        .format("jdbc") \
        .option("url", POSTGRES_URL) \
        .option("dbtable", POSTGRES_TABLE) \
        .option("user", POSTGRES_USER) \
        .option("password", POSTGRES_PASSWORD) \
        .option("driver", "org.postgresql.Driver") \
        .start() \
        .awaitTermination()

if __name__ == "__main__":
    process_stream()