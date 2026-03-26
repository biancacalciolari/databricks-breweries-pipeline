# Databricks notebook source
# DBTITLE 1,Cell 1
from pyspark.sql.functions import count

SILVER_TABLE = "breweries_catalog.silver.breweries_silver"
GOLD_TABLE = "breweries_catalog.gold.breweries_report"

df_silver = spark.read.table(SILVER_TABLE)

df_gold = (
    df_silver.groupBy("country", "state", "brewery_type")
             .agg(count("id").alias("total_breweries"))
)

df_gold.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(GOLD_TABLE)
