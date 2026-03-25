# BEES Data Engineering Case - Brewery Pipeline 🍻
 
## 🎯 Objetivo
[cite_start]Este projeto implementa um pipeline de dados robusto utilizando a **Arquitetura Medallion** para consumir, transformar e agregar dados da [Open Brewery DB API](https://www.openbrewerydb.org/)[cite: 3, 5].
 
## 🏗️ Arquitetura e Design
[cite_start]A solução foi construída utilizando **PySpark** no ecossistema **Databricks**, garantindo escalabilidade horizontal e resiliência[cite: 8, 9].
 
### Camadas do Data Lake (Medallion):
1.  [cite_start]**Bronze (Raw):** Ingestão dos dados em seu formato nativo (JSON convertido para Delta) com adição de metadados de auditoria (`extraction_at`, `source_system`)[cite: 11, 12].
2.  **Silver (Curated):** Limpeza, tipagem (Casting) e tratamento de nulos. [cite_start]Os dados são persistidos no formato **Delta** e **particionados por localização (State)** para otimização de consultas regionais (Data Skipping)[cite: 13, 14].
3.  [cite_start]**Gold (Analytical):** Visão agregada que reporta a quantidade de cervejarias por tipo e localização, pronta para consumo por ferramentas de BI[cite: 15].
 
## 🛠️ Decisões Técnicas & Trade-offs
- **Delta Lake:** Escolhido em vez de Parquet comum para garantir transações ACID, versionamento de dados (Time Travel) e evolução de schema simplificada.
- **Particionamento:** A escolha do campo `state` na camada Silver visa performance. [cite_start]Em cenários de Big Data, o particionamento reduz drasticamente o custo de I/O[cite: 13, 26].
- [cite_start]**Idempotência:** O pipeline foi desenhado para ser re-executável sem gerar duplicidade (usando o modo `overwrite` e tratamento de IDs únicos)[cite: 29].
 
## 🚦 Monitoramento e Alerta
[cite_start]Para um ambiente de produção, a estratégia proposta inclui[cite: 16]:
- [cite_start]**Data Quality:** Implementação de testes de expectativa (como Great Expectations) para validar se campos críticos (ID, Type) não possuem nulos após a camada Silver[cite: 17].
- [cite_start]**Observabilidade:** Uso de **Databricks Workflows** com alertas configurados via Webhook para falhas no job ou latência acima do esperado[cite: 7].
- [cite_start]**Retries:** Configuração de até 3 tentativas automáticas com backoff exponencial para lidar com instabilidades momentâneas da API de origem[cite: 7].
 
## 🚀 Como Executar
1. Importe os notebooks da pasta `/scripts` para seu Workspace Databricks.
2. [cite_start]Configure um cluster com **Runtime 13.3 LTS** ou superior[cite: 10].
3. Execute os notebooks na ordem: `01_Bronze`, `02_Silver`, `03_Gold`.
