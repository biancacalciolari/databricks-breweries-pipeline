# Databricks notebook source
# DBTITLE 1,Cell 1
# CONFIGURAÇÃO
from pyspark.sql.functions import col, count

# 1. Definição dos caminhos
SILVER_TABLE = "breweries_catalog.silver.breweries_partitioned"
GOLD_TABLE = "breweries_catalog.gold.breweries_report"

def create_gold_layer():
    # Lendo os dados curados da Silver
    df_silver = spark.read.table(SILVER_TABLE)

    # 2. Agregação solicitada: quantidade de cervejarias por tipo e localização
    # Localização aqui compreende 'state' e 'city' conforme o requisito 5.c
    df_gold = df_silver.groupBy("state", "city", "brewery_type") \
                       .agg(count("id").alias("total_breweries")) \
                       .orderBy("state", "city", col("total_breweries").desc())

    # 3. Escrita da camada analítica
    # Na Gold, costumamos salvar sem particionamento se o volume for pequeno,
    # ou em uma tabela única para facilitar o consumo via SQL/BI.
    df_gold.write.format("delta") \
           .mode("overwrite") \
           .saveAsTable(GOLD_TABLE)

    # Exibindo o resultado para validação rápida
    display(df_gold.limit(10))
    print(f"Camada Gold gerada com sucesso.")

# Executa a agregação
create_gold_layer()
