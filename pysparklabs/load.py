import kagglehub
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("Fraud Detection").getOrCreate()  # type: ignore
path = kagglehub.dataset_download("kartik2112/fraud-detection")

df = spark.read.option("header", "true").csv(path)
df.printSchema()

df.show(10)
