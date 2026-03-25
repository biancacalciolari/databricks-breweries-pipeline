# Databricks notebook source
# DBTITLE 1,Cell 1
#CONFIGURAÇÃO   
import requests
import json
from pyspark.sql.functions import current_timestamp, lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType


# 1. Definição de Caminhos (Usando Unity Catalog ao invés de DBFS)
BRONZE_TABLE = "breweries_catalog.bronze.breweries_bronze"

def fetch_and_save_bronze():
    # URL da API conforme as instruções do case [cite: 5]
    api_url = "https://api.openbrewerydb.org/v1/breweries"

    try:
        # Realizando a requisição (Camada de extração)
        response = requests.get(api_url, timeout=30)
        response.raise_for_status() # Lança erro se o status for 4xx ou 5xx [cite: 7, 29]

        data = response.json()

        # Definindo schema explícito para evitar problemas de inferência
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

        # Convertendo para Spark DataFrame com schema explícito
        df_raw = spark.createDataFrame(data, schema=schema)

        # Adicionando metadados (Prática Sênior: Linhagem e Auditoria)
        df_bronze = df_raw.withColumn("extraction_at", current_timestamp()) \
                          .withColumn("source_system", lit("OpenBreweryDB_API"))

        # Salvando na Camada Bronze (Persistência do dado bruto) 
        # Usamos Delta para garantir transações ACID e Time Travel
        df_bronze.write.format("delta") \
                .mode("overwrite") \
                .saveAsTable(BRONZE_TABLE)

        print(f"Sucesso: {df_bronze.count()} registros salvos na Bronze.")

    except Exception as e:
        # Tratamento de erro conforme requisito 6 [cite: 16, 29]
        print(f"Erro crítico na ingestão: {str(e)}")
        raise e

# Executa a função
fetch_and_save_bronze()
