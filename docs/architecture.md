# 🧱 Arquitetura do Pipeline

## 📌 Visão Geral

Este projeto implementa um pipeline de dados baseado na arquitetura Medallion, utilizando Databricks, Delta Lake e Unity Catalog.

A arquitetura foi desenhada para separar responsabilidades entre ingestão, transformação e consumo analítico.

---

## 🔄 Fluxo de Dados

API (Open Brewery DB)
        ↓
Bronze (Raw Data - Delta)
        ↓
Silver (Refined Data - Incremental MERGE)
        ↓
Gold (Aggregated Data - Analytics)

---

## 🥉 Camada Bronze

- Fonte: API externa
- Tipo: Dados brutos (raw)
- Formato: Delta
- Estratégia: Append-only

### Características:
- Inclusão de ingestion_timestamp
- Sem transformação
- Base para reprocessamento

---

## 🥈 Camada Silver

- Tipo: Dados tratados
- Estratégia: Incremental com MERGE

### Transformações:
- Seleção de colunas relevantes
- Remoção de registros inválidos
- Deduplicação por ID
- Particionamento por localização

### Benefícios:
- Evita reprocessamento completo
- Melhora performance
- Mantém consistência

---

## 🥇 Camada Gold

- Tipo: Dados agregados
- Finalidade: Consumo analítico

### Agregações:
- Quantidade de cervejarias por:
  - país
  - estado
  - tipo

### Benefícios:
- Pronto para BI
- Baixa latência de consulta
- Simplificação para usuários finais

---

## 🔐 Governança (Unity Catalog)

Estrutura:

breweries_catalog
├── bronze
├── silver
└── gold

### Vantagens:
- Organização por camadas
- Controle de acesso
- Padronização

---

## ⚙️ Tecnologias

- Databricks
- PySpark
- Delta Lake
- Unity Catalog

---

## 🚀 Evolução futura

- Streaming ingestion
- Auto Loader
- Data Quality framework
- Monitoramento e alertas
