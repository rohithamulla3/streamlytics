from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, from_json, col
from pyspark.sql.types import StructType, StringType
from sentiment_model import get_sentiment

spark = SparkSession.builder.appName("TwitterSentiment").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

schema = StructType().add("text", StringType()).add("id", StringType()).add("created_at", StringType())
sentiment_udf = udf(get_sentiment, StringType())

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "raw_tweets") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")
scored_df = json_df.withColumn("sentiment", sentiment_udf(col("text")))

query = scored_df.writeStream.outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
