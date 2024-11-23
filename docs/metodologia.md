# 📘 Metodologia RFV - Recência, Frequência e Valor Monetário

Este documento descreve a metodologia RFV utilizada no projeto, explicando os conceitos, cálculos e aplicações práticas.

---

## 🌟 O Que é a Metodologia RFV?

RFV (Recência, Frequência e Valor Monetário) é uma técnica amplamente utilizada em marketing e análise de dados para segmentar clientes com base em seu comportamento transacional. Cada métrica avalia um aspecto crítico da relação entre o cliente e o negócio:

- **Recência:** Mede há quanto tempo o cliente realizou sua última compra.
- **Frequência:** Mede o número total de compras realizadas pelo cliente em um período definido.
- **Valor Monetário:** Representa o valor total gasto pelo cliente em suas compras.

---

## 🔍 Por que Usar RFV?

A metodologia RFV é eficaz para entender o comportamento do cliente, permitindo:

1. **Identificar os melhores clientes:** 
   - Clientes que compram frequentemente, gastam mais e realizaram compras recentes.

2. **Reconhecer padrões de abandono:**
   - Clientes que compravam regularmente, mas não realizaram compras recentemente.

3. **Planejar ações direcionadas:**
   - Estratégias personalizadas para retenção, recuperação ou maximização de valor.

---

## 📋 Etapas da Metodologia

### 1. **Coleta de Dados**
Reúna os dados transacionais dos clientes, incluindo:
- Identificador único do cliente.
- Data de cada compra.
- Valor de cada compra.

### 2. **Cálculo das Métricas RFV**

#### Recência:
- **Definição:** Número de dias desde a última compra do cliente.
- **Cálculo:** 
  - Subtraia a data da última compra do cliente da data de referência (normalmente a data atual).
  - Fórmula: `Recência = Data de Referência - Data Última Compra`.

#### Frequência:
- **Definição:** Total de compras realizadas pelo cliente em um período específico.
- **Cálculo:**
  - Conte o número de transações únicas realizadas pelo cliente.
  - Fórmula: `Frequência = Total de Transações`.

#### Valor Monetário:
- **Definição:** Soma total do valor gasto pelo cliente em todas as compras.
- **Cálculo:**
  - Some o valor das transações para cada cliente.
  - Fórmula: `Valor = Soma(Total Gasto)`.

### 3. **Pontuação RFV**

- Cada métrica é convertida em uma pontuação relativa (ex.: de 1 a 5), onde:
  - **Recência:** Pontuação mais alta para valores mais recentes.
  - **Frequência:** Pontuação mais alta para clientes que compram frequentemente.
  - **Valor:** Pontuação mais alta para clientes que gastam mais.
- **Exemplo de cálculo:**
  - Divida os clientes em quintis ou percentis para atribuir as pontuações.

### 4. **Segmentação RFV**
Com base nas pontuações combinadas, os clientes são classificados em segmentos como:
- **Melhores Clientes:** Alta Recência, Alta Frequência, Alto Valor.
- **Clientes Leais:** Alta Frequência, Alto Valor, Recência Moderada.
- **Clientes em Risco:** Alta Recência, Baixa Frequência e Valor.
- **Potenciais Perdas:** Alta Recência, Baixa Frequência e Valor.

---

## 🎯 Aplicações Práticas

1. **Melhores Clientes:**
   - Recompensas exclusivas e programas de fidelidade.
2. **Clientes em Risco:**
   - Campanhas de reativação, como descontos ou incentivos.
3. **Clientes Novos:**
   - Incentivar a fidelização com promoções direcionadas.
4. **Clientes Potenciais:**
   - Cross-sell e upsell para aumentar o valor de compra.

---

## 📊 Visualizações no Projeto

1. **Distribuições:** Histogramas para entender os padrões de cada métrica.
2. **Segmentação:** Gráficos de barras para visualizar a distribuição dos clientes em cada segmento.

---

## 🌟 Benefícios da Metodologia RFV

- **Simplicidade:** Fácil de calcular e implementar.
- **Flexibilidade:** Pode ser adaptada a diferentes setores e necessidades.
- **Impacto Prático:** Fornece insights claros para decisões estratégicas.

---

## 🔧 Limitações e Cuidados

1. **Dados Antigos:**
   - Pode não refletir comportamentos recentes se os dados estiverem desatualizados.
2. **Setores Específicos:**
   - Não é igualmente eficaz em negócios de compra única ou baixa recorrência.
3. **Sazonalidade:**
   - Pode ser influenciado por padrões sazonais de compras.

---

## 🛠️ Extensões Possíveis

- **Machine Learning:** Usar algoritmos de clusterização (ex.: K-Means) para criar grupos baseados nas métricas RFV.
- **Previsão:** Integrar modelos preditivos para prever o comportamento do cliente com base nos dados RFV.
