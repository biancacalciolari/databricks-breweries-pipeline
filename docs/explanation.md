# 🧠 Explicação do Case Técnico

## 📌 Objetivo

O objetivo deste projeto foi construir um pipeline de dados completo simulando um cenário real de engenharia de dados, desde a ingestão até a camada analítica.

---

## 🧱 Abordagem adotada

A solução foi estruturada seguindo a arquitetura Medallion:

- Bronze: ingestão dos dados brutos
- Silver: transformação e tratamento
- Gold: agregação para consumo

Essa abordagem permite separar responsabilidades e facilitar manutenção.

---

## ⚙️ Decisões técnicas

### 1. Uso de Databricks
Escolhido por oferecer processamento distribuído, integração com Spark e suporte a Delta Lake.

---

### 2. Uso de Delta Lake
- Garantia de consistência (ACID)
- Suporte a MERGE
- Melhor performance para leitura e escrita

---

### 3. Processamento incremental (MERGE)
Foi utilizado MERGE na camada Silver para:

- Evitar reprocessamento completo
- Atualizar registros existentes
- Inserir novos dados

Isso simula um cenário real de pipeline incremental.

---

### 4. Unity Catalog
Utilizado para:

- Organizar dados em camadas
- Garantir governança
- Facilitar controle de acesso

---

### 5. Particionamento
Aplicado por:

- country
- state

Motivo:
- Melhorar performance de leitura
- Reduzir volume de dados processados

---

## 🧪 Data Quality

Validações implementadas:

- Verificação de campos obrigatórios
- Filtro de registros inválidos
- Controle de duplicidade via MERGE

---

## 🚀 Diferenciais do projeto

- Pipeline completo (end-to-end)
- Uso de arquitetura padrão de mercado
- Processamento incremental
- Organização pronta para produção

---

## 🔮 Possíveis melhorias

- Implementação de streaming
- Monitoramento e alertas
- Testes automatizados
- CI/CD
