# Databricks notebook source
# DBTITLE 1,Cell 1
from pyspark.sql.functions import col, coalesce

BRONZE_TABLE = "breweries_catalog.bronze.breweries_bronze"
SILVER_TABLE = "breweries_catalog.silver.breweries_silver"

spark.sql(f"""
CREATE TABLE IF NOT EXISTS {SILVER_TABLE} (
    id STRING,
    name STRING,
    brewery_type STRING,
    street STRING,
    city STRING,
    state STRING,
    postal_code STRING,
    country STRING,
    longitude FLOAT,
    latitude FLOAT,
    ingestion_timestamp TIMESTAMP,
    source_system STRING
)
USING DELTA
PARTITIONED BY (country, state)
""")

df_bronze = spark.read.table(BRONZE_TABLE)

df_silver = (
    df_bronze.select(
        col("id").cast("string").alias("id"),
        col("name").cast("string").alias("name"),
        col("brewery_type").cast("string").alias("brewery_type"),
        col("street").cast("string").alias("street"),
        col("city").cast("string").alias("city"),
        coalesce(col("state"), col("state_province")).cast("string").alias("state"),
        col("postal_code").cast("string").alias("postal_code"),
        col("country").cast("string").alias("country"),
        col("longitude").cast("float").alias("longitude"),
        col("latitude").cast("float").alias("latitude"),
        col("ingestion_timestamp"),
        col("source_system")
    )
    .filter(col("id").isNotNull())
    .filter(col("country").isNotNull())
)

df_silver.createOrReplaceTempView("vw_breweries_silver_stage")

spark.sql(f"""
MERGE INTO {SILVER_TABLE} AS target
USING vw_breweries_silver_stage AS source
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
""")
