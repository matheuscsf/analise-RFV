# 📂 Aplicação Streamlit - Análise RFV

Esta pasta contém o código da aplicação desenvolvida em Streamlit para análise interativa das métricas RFV (Recência, Frequência e Valor Monetário).

---

## 📄 Arquivo: `app_rfv.py`

### Descrição Geral
A aplicação `app_rfv.py` permite que os usuários façam o upload de um arquivo CSV com dados de clientes, explorem gráficos interativos das métricas RFV e apliquem filtros para analisar diferentes segmentos de clientes.

---

### 🚀 Funcionalidades

1. **Upload de Arquivo CSV:**
   - Faça upload de um arquivo com dados RFV para análise.

2. **Visualização de Dados:**
   - Exibe os dados carregados em uma tabela interativa.

3. **Estatísticas Descritivas:**
   - Mostra as principais estatísticas das métricas RFV.

4. **Gráficos Interativos:**
   - Histogramas para Recência, Frequência e Valor Monetário.
   - Gráficos da distribuição dos segmentos (caso incluídos nos dados).

5. **Filtros Dinâmicos:**
   - Filtre os clientes por intervalos de Recência, Frequência e Valor.

6. **Download de Dados Filtrados:**
   - Exporte os dados filtrados para um arquivo CSV.

---

### 🛠️ Como Configurar e Rodar a Aplicação

1. **Pré-requisitos:**
   - Instale o Python 3.8 ou superior.
   - Instale as dependências listadas em `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **Rodando a Aplicação:**
   - No terminal, navegue até a pasta `app/` e execute:
     ```bash
     streamlit run app_rfv.py
     ```
   - O terminal exibirá um link (ex.: `http://localhost:8501`). Clique ou copie e cole no navegador para acessar a aplicação.

3. **Upload do Arquivo CSV:**
   - Faça o upload de um arquivo seguindo o formato descrito em [`data/README.md`](../data/README.md).

---

### 📋 Exemplo de Uso

1. Faça o upload do arquivo `RFV.csv` (fornecido na pasta `data/`).
2. Explore os gráficos de Recência, Frequência e Valor.
3. Use os filtros para segmentar clientes por intervalos específicos.
4. Baixe os dados filtrados para análises adicionais.
