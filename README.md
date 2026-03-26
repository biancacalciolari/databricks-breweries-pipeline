# 🚀 Breweries Data Pipeline (Databricks + Unity Catalog)

## 📌 Visão Geral

Este projeto implementa um pipeline de dados ponta a ponta utilizando **Databricks**, **PySpark**, **Delta Lake** e **Unity Catalog**, seguindo o padrão de arquitetura **Medallion (Bronze, Silver e Gold)**.

A solução contempla ingestão de dados via API, processamento incremental e organização em camadas, simulando um cenário real de produção.

---

## 🏗️ Estrutura do Projeto
O projeto segue a **Arquitetura Medallion** utilizando **PySpark** e **Delta Lake**:
 
- **Bronze:** Ingestão dos dados brutos com metadados de auditoria.
- **Silver:** Limpeza, tipagem e **particionamento por estado** (otimização de I/O).
- **Gold:** Agregação final por tipo e localização para consumo analítico.
 
## 🛠️ Requisitos Técnicos
- **Escalabilidade:** Processamento distribuído com Spark.
- **Resiliência:** Tratamento de erros de API e idempotência nas cargas.
- **Performance:** Uso de particionamento e formato Delta para Data Skipping.
 
## 🚦 Monitoramento
Estratégia de observabilidade baseada em:
- Logs de execução em cada camada.
- Alertas de falha via Databricks Workflows.
- Retries automáticos para instabilidades de rede na extração da API.

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

## ▶️ Execução

O pipeline pode ser executado de duas formas:

### Execução manual
1. Executar notebook Bronze
2. Executar notebook Silver
3. Executar notebook Gold

### Execução orquestrada
Também foi criada uma orquestração no Databricks Workflows, com execução sequencial:
Bronze → Silver → Gold

As evidências estão disponíveis na pasta `docs/evidencias/`.

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

## 📄 Documentação

- Arquitetura → docs/architecture.md  
- Explicação → docs/explanation.md  
- Orquestração → docs/orchestration.md  
- Monitoramento → docs/monitoring.md
- Evidência de execução → docs/evidencias/Evidencia_pipeline.png
- Evidência de dados → docs/evidencias/Evidencia_Dados.png

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
