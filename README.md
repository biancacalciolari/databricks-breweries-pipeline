# 🚀 Breweries Data Pipeline (Databricks + Unity Catalog)

## 📌 Visão Geral

Este projeto implementa um pipeline de dados ponta a ponta utilizando **Databricks**, **PySpark**, **Delta Lake** e **Unity Catalog**, seguindo o padrão de arquitetura **Medallion (Bronze, Silver e Gold)**.

A solução contempla ingestão de dados via API, processamento incremental e organização em camadas, simulando um cenário real de produção.

---

## 🧱 Arquitetura

API (Open Brewery DB)
        ↓
Bronze (Raw - Delta)
        ↓
Silver (Refined - MERGE incremental)
        ↓
Gold (Aggregated - Analytics)

---

## 🥉 Camada Bronze

- Consumo da API via Python (`requests`)
- Conversão para DataFrame Spark
- Persistência em Delta Lake
- Inclusão de `ingestion_timestamp`
- Estrutura append-only

📌 Objetivo: garantir rastreabilidade e reprocessamento

---

## 🥈 Camada Silver

- Seleção de colunas relevantes
- Remoção de dados inválidos (`id` e `country`)
- Deduplicação lógica via `MERGE`
- Particionamento por `country` e `state`

### 🔥 Processamento incremental

MERGE INTO breweries_catalog.silver.breweries

📌 Objetivo: evitar full refresh e otimizar performance

---

## 🥇 Camada Gold

- Agregação por:
  - país
  - estado
  - tipo de cervejaria

COUNT(*) AS total_breweries

📌 Objetivo: disponibilizar dataset analítico pronto

---

## ⚙️ Tecnologias

- Databricks
- PySpark
- Delta Lake
- Unity Catalog
- Python (requests)

---

## 🔄 Execução

1. Executar notebook Bronze (ingestão API)
2. Executar Silver (transformação + MERGE)
3. Executar Gold (agregação)

---

## 🧪 Data Quality

Validações aplicadas:

- Verificação de `id` nulo
- Filtro de registros inválidos
- Controle de duplicidade via MERGE

---

## 🔐 Governança

Estrutura no Unity Catalog:

breweries_catalog.bronze  
breweries_catalog.silver  
breweries_catalog.gold  

📌 Permite:
- organização
- controle de acesso
- rastreabilidade

---

## 🧠 Decisões Técnicas

- Uso de MERGE para processamento incremental
- Particionamento baseado em padrão de acesso
- Separação clara entre camadas
- Uso de Delta Lake para confiabilidade (ACID)

---

## 🚀 Diferenciais

- Pipeline completo (ingestão + transformação + consumo)
- Uso de Unity Catalog (nível produção)
- Processamento incremental real
- Arquitetura escalável

---

## 🔮 Melhorias Futuras

- Auto Loader
- Streaming ingestion
- Data Quality framework (Great Expectations)
- CI/CD com GitHub Actions

---

## 📎 Fonte de Dados

https://api.openbrewerydb.org/v1/breweries

---

## 👩‍💻 Autora

Bianca de Jesus Calciolari Reis
