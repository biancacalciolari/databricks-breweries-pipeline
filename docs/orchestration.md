# 🚀 Orquestração do Pipeline

## 📌 Visão Geral

A orquestração do pipeline foi implementada utilizando **Databricks Workflows (Jobs)**, permitindo execução automatizada, controle de dependências, retries e monitoramento.

---

## 🧱 Estrutura do Pipeline

O pipeline é composto por três etapas principais:

1. Bronze - Ingestão da API
2. Silver - Transformação e carga incremental
3. Gold - Agregação analítica

### 🔄 Fluxo

Bronze → Silver → Gold

---

## ⚙️ Configuração das Tasks

### 🥉 Bronze - Ingestion

- Tipo: Notebook
- Função: Consumo da API e persistência na camada Bronze
- Estratégia: Append-only
- Retry: 3 tentativas
- Intervalo: 5 minutos

---

### 🥈 Silver - Transformation

- Tipo: Notebook
- Dependência: Bronze
- Função: Limpeza, padronização e carga incremental com MERGE
- Retry: 2 tentativas
- Intervalo: 5 minutos

---

### 🥇 Gold - Aggregation

- Tipo: Notebook
- Dependência: Silver
- Função: Agregação analítica para consumo
- Retry: 2 tentativas
- Intervalo: 5 minutos

---

## 🔗 Dependências

- Silver executa apenas após sucesso da Bronze
- Gold executa apenas após sucesso da Silver

Configuração utilizada:
- Run if: All succeeded

---

## ⏰ Agendamento

- Tipo: Scheduled
- Frequência: Daily
- Execução automática do pipeline completo

---

## ❗ Tratamento de Erros

- Uso de retries automáticos para falhas transitórias
- Tratamento de erro na API com `raise_for_status()`
- Interrupção do fluxo em caso de falha crítica

---

## 📊 Monitoramento

- Histórico de execuções disponível no Databricks
- Logs detalhados por task
- Visualização do status de cada etapa

---

## 🚀 Benefícios

- Execução automatizada e confiável
- Controle de dependências entre etapas
- Facilidade de monitoramento
- Escalabilidade para cenários maiores
