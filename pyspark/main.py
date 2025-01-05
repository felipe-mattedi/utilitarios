from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pyspark.sql.functions as F
import json
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# Create a SparkSession
spark = SparkSession.builder.appName("Exemplo do pyspark").getOrCreate()

# Read CSV File
df_1 = spark.read.option("header",True).csv("table_1.csv")
df_2 = spark.read.option("header",True).csv("table_2.csv")
df_3 = spark.read.option("header",True).csv("table_3.csv")

df_12 = df_1.join(df_2, df_1["id"] == df_2["id"]).join(df_3, df_1["id"] == df_3["id"]).drop(df_2["id"]).drop(df_3["id"])

print(df_12.show())

df_json = df_12.toJSON()

print(df_json.collect())

df_x = df_2.groupBy('id').agg(F.collect_list('idade').alias('idade'))
print(df_x.show())


df_13 = df_1.join(df_x, df_1["id"] == df_x["id"]).join(df_3, df_1["id"] == df_3["id"]).drop(df_x["id"]).drop(df_3["id"])

print(df_13.show())

df_json_2 = df_13.toJSON()

print(df_json_2.collect())