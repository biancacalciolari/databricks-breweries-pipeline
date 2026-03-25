# 🍻 Brewery Data Pipeline - BEES Engineering Case
 
Este repositório contém a solução para o case técnico de Engenharia de Dados da BEES. O objetivo é consumir dados da API Open Brewery DB e estruturá-los num Data Lake seguindo a arquitetura Medallion.
 
## 🚀 Arquitetura da Solução
A solução foi desenvolvida utilizando **PySpark** no **Databricks**, aproveitando as vantagens do formato **Delta Lake**.
 
### Camadas (Medallion Architecture):
1.  **Bronze (Raw):** Ingestão direta da API. O dado é persistido em formato Delta mantendo a fidelidade à origem, acrescido de metadados (`ingestion_timestamp` e `source_file`) para rastreabilidade.
2.  **Silver (Clean/Curated):** - **Transformações:** Limpeza de esquemas, conversão de tipos (coordenadas para float) e remoção de registos sem ID (Data Quality).
    - **Particionamento:** Os dados foram **particionados por `state` e `city`**. Esta escolha de design visa otimizar a performance de consultas analíticas regionais (Data Skipping).
3.  **Gold (Analytical):** Criação de uma tabela agregada que consolida a quantidade de cervejarias por tipo e localização, pronta para consumo por ferramentas de BI.
 
## 🛠️ Decisões de Design & Trade-offs
- **Porquê PySpark?** Em vez de bibliotecas como Pandas, o PySpark permite processamento distribuído. Para um Engenheiro Sénior, a solução deve ser escalável para milhões de registos sem alteração de código.
- **Delta Lake vs Parquet:** O Delta foi escolhido por suportar transações ACID (evitando corrupção de dados em escritas interrompidas) e *Time Travel* (auditoria de versões anteriores).
- **Idempotência:** Todo o pipeline é idempotente. Se for executado novamente para o mesmo período, o resultado final será consistente, sem duplicados.
 
## 🚦 Monitorização e Alerta (Item 6 do Case)
Num ambiente produtivo, a estratégia de monitorização baseia-se em:
1.  **Data Quality Checks:** Implementação de verificações entre as camadas (ex: se `count` na Bronze == `count` na Silver).
2.  **Pipeline Failure:** Uso do **Databricks Workflows** com alertas via Email/Slack. Se a API estiver offline, o sistema está configurado com 3 retries (backoff exponencial).
3.  **Audit Logs:** Registo de volumetria em cada carga para detetar anomalias (ex: queda repentina no número de cervejarias retornadas pela API).
 
## 📦 Como Executar
1. Importar os notebooks da pasta `/notebooks` para o Workspace do Databricks.
2. Configurar um cluster com **Runtime 13.3 LTS**.
3. Executar o fluxo: `01_Bronze` -> `02_Silver` -> `03_Gold`.
