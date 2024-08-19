# /spark_processing/spark_streaming.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

def start_spark_processing():
    spark = SparkSession.builder.appName("KafkaSparkStreaming").getOrCreate()

    schema = StructType([
        StructField("e", StringType(), True),
        StructField("E", StringType(), True),
        StructField("s", StringType(), True),
        StructField("p", StringType(), True),
        StructField("q", StringType(), True)
    ])

    kafka_df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092")\
        .option("subscribe", "market-data").load()

    parsed_df = kafka_df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")

    query = parsed_df.writeStream.outputMode("append").format("console").start()

    query.awaitTermination()

if __name__ == "__main__":
    start_spark_processing()