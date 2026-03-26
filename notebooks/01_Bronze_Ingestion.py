# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# DBTITLE 1,Cell 1
import requests
from pyspark.sql.functions import current_timestamp, lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

BRONZE_TABLE = "breweries_catalog.bronze.breweries_bronze"

def fetch_all_pages():
    api_url = "https://api.openbrewerydb.org/v1/breweries"
    all_data = []
    page = 1
    per_page = 200

    while True:
        response = requests.get(
            api_url,
            params={"page": page, "per_page": per_page},
            timeout=30
        )
        response.raise_for_status()
        data = response.json()

        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data

schema = StructType([
    StructField("id", StringType(), True),
    StructField("name", StringType(), True),
    StructField("brewery_type", StringType(), True),
    StructField("address_1", StringType(), True),
    StructField("address_2", StringType(), True),
    StructField("address_3", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state_province", StringType(), True),
    StructField("postal_code", StringType(), True),
    StructField("country", StringType(), True),
    StructField("longitude", DoubleType(), True),
    StructField("latitude", DoubleType(), True),
    StructField("phone", StringType(), True),
    StructField("website_url", StringType(), True),
    StructField("state", StringType(), True),
    StructField("street", StringType(), True)
])

def fetch_and_save_bronze():
    data = fetch_all_pages()
    df_raw = spark.createDataFrame(data, schema=schema)

    df_bronze = (
        df_raw.withColumn("ingestion_timestamp", current_timestamp())
              .withColumn("source_system", lit("OpenBreweryDB_API"))
    )

    df_bronze.write.format("delta") \
        .mode("append") \
        .saveAsTable(BRONZE_TABLE)

fetch_and_save_bronze()
