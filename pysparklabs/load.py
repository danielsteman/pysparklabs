import kagglehub
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("local").getOrCreate()
path = kagglehub.dataset_download(
    "stealthtechnologies/gdp-growth-of-european-countries"
)

df = spark.read.csv(path)
df.printSchema()
