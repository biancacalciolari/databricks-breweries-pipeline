# Plano de Testes do Pipeline

## Objetivo

Este documento descreve os testes mínimos planejados para validar o funcionamento do pipeline de dados implementado em Databricks, seguindo a arquitetura Medallion.

---

## Escopo

- Ingestão (Bronze)
- Transformação (Silver)
- Agregação (Gold)

---

## Bronze

- API retorna status 200
- Tabela criada
- ingestion_timestamp não nulo

---

## Silver

- id não nulo
- country não nulo
- sem duplicidade por id
- particionamento por country/state

---

## Gold

- tabela criada
- total_breweries > 0
- colunas esperadas presentes

---

## Operacional

- execução Bronze → Silver → Gold
- retries configurados
- logs disponíveis

---

## Evidências

docs/evidencias/
