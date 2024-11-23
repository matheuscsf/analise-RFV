# 📐 Arquitetura do Projeto - Análise RFV

Este documento descreve a arquitetura geral do projeto de análise RFV, detalhando os principais componentes, fluxos de dados e funcionalidades.

---

## 🌟 Visão Geral

O projeto foi projetado para realizar a análise RFV de clientes, segmentando-os com base nas métricas **Recência**, **Frequência** e **Valor Monetário**. Ele possui três componentes principais:

1. **Processamento e Cálculo (Notebooks):** Realiza o cálculo das métricas RFV e a segmentação de clientes.
2. **Interface Interativa (Aplicação Streamlit):** Proporciona uma interface amigável para explorar os dados RFV.
3. **Dados de Exemplo:** Fornece um arquivo CSV estruturado para demonstração e teste.

---

## 🗂️ Componentes do Projeto

### 1. **Notebooks**
- Local: `notebooks/Analise RFV.ipynb`
- **Descrição:** Contém o código para processamento e análise dos dados RFV.
  - **Entrada:** Arquivo CSV com dados transacionais dos clientes.
  - **Saída:** Dados processados com as métricas RFV e segmentação exportados para um novo CSV.
  - **Funcionalidades:**
    - Cálculo das métricas RFV.
    - Visualizações iniciais de distribuição das métricas.
    - Geração de arquivos prontos para uso na aplicação Streamlit.

---

### 2. **Aplicação Streamlit**
- Local: `app/app_rfv.py`
- **Descrição:** Interface interativa para explorar dados RFV.
  - **Entrada:** Arquivo CSV gerado no notebook ou qualquer outro dataset estruturado de forma semelhante.
  - **Funcionalidades:**
    - Upload de arquivos CSV.
    - Visualização de dados e estatísticas descritivas.
    - Gráficos interativos para Recência, Frequência e Valor.
    - Filtros dinâmicos para segmentar clientes.
    - Exportação de dados filtrados para análise adicional.

---

### 3. **Dados**
- Local: `data/`
- **Descrição:** Contém o arquivo de exemplo `RFV.csv` e instruções sobre como utilizá-lo.
  - **Formato:** CSV com colunas padrão (ex.: `ClienteID`, `Recencia`, `Frequencia`, `Valor`, `Segmento`).
  - **Propósito:** Demonstrar o funcionamento dos notebooks e da aplicação Streamlit.

---

## 🔄 Fluxo de Dados

1. **Entrada dos Dados:**
   - O arquivo inicial (ex.: `RFV.csv`) é carregado no notebook para processamento ou diretamente na aplicação Streamlit.

2. **Processamento no Notebook:**
   - As métricas RFV são calculadas e os clientes são segmentados.
   - Os resultados são exportados para um novo arquivo CSV.

3. **Exploração na Aplicação:**
   - O CSV gerado no notebook é carregado na aplicação Streamlit para visualizações e análise interativa.

4. **Saída:**
   - Os dados filtrados na aplicação podem ser baixados em um arquivo CSV.

---

## 🎯 Casos de Uso

- **E-commerce:**
  Identificar os clientes mais valiosos e os que estão em risco de churn.
- **Marketing:**
  Desenvolver campanhas segmentadas com base nos comportamentos dos clientes.
- **Gestão de Relacionamento:**
  Personalizar abordagens com base nos segmentos RFV.

---

## 🔧 Tecnologias Utilizadas

- **Python:** Linguagem principal para processamento e construção da aplicação.
- **Bibliotecas:**
  - `pandas` e `numpy`: Processamento de dados.
  - `matplotlib` e `seaborn`: Visualizações.
  - `streamlit`: Desenvolvimento da aplicação web interativa.
