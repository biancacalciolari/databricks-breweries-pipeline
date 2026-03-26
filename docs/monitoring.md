# 📊 Monitoramento e Alertas

## 📌 Visão Geral

O monitoramento do pipeline foi planejado utilizando recursos nativos do Databricks, garantindo visibilidade, confiabilidade e capacidade de resposta a falhas.

---

## 🔍 Monitoramento de Execução

O Databricks Workflows fornece:

- Histórico de execuções (runs)
- Status por task (Success, Failed, Skipped)
- Tempo de execução
- Logs detalhados

---

## 🔔 Alertas

Configuração recomendada:

- Notificação por e-mail em caso de falha
- Possibilidade de integração com Slack/Webhook

Eventos monitorados:

- Falha de execução
- Tempo de execução acima do esperado
- Interrupção do pipeline

---

## 🧪 Data Quality

Validações implementadas no pipeline:

### Bronze
- Verificação de retorno da API
- Validação de schema

### Silver
- Remoção de registros com `id` nulo
- Remoção de registros sem `country`

### Gold
- Validação de contagem de registros
- Garantia de dados agregados consistentes

---

## 📈 Métricas sugeridas

- Quantidade de registros ingeridos
- Quantidade de registros processados
- Tempo de execução por etapa
- Taxa de falhas

---

## 🚨 Estratégia de Alertas

- Falha na Bronze → alerta crítico
- Falha na Silver → alerta médio
- Falha na Gold → alerta analítico

---

## 🔮 Melhorias Futuras

- Integração com ferramentas externas (Datadog, Prometheus)
- Alertas baseados em volume de dados
- Monitoramento de SLA
- Implementação de testes automatizados

---

## 🚀 Benefícios

- Maior confiabilidade do pipeline
- Detecção rápida de falhas
- Melhor governança de dados
- Suporte à operação contínua
