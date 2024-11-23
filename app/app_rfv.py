# Importando bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando a página
st.set_page_config(
    page_title="Análise RFV",
    page_icon="📊",
    layout="wide",
)

# Função para carregar os dados
@st.cache
def carregar_dados(arquivo):
    dados = pd.read_csv(arquivo)
    return dados

# Título e descrição
st.title("📊 Análise RFV - Recência, Frequência e Valor Monetário")
st.markdown("""
Bem-vindo à aplicação de análise RFV!  
Aqui você poderá explorar os dados de clientes com base nos pilares RFV:  
- **Recência:** Há quanto tempo foi a última compra do cliente.  
- **Frequência:** Quantidade de compras realizadas.  
- **Valor Monetário:** Quanto o cliente gastou ao todo.  

Faça o upload do arquivo RFV e comece a explorar!
""")

# Upload do arquivo CSV
arquivo_carregado = st.file_uploader("Faça o upload do arquivo RFV (formato CSV):", type=["csv"])

if arquivo_carregado:
    # Carregar os dados
    dados_rfv = carregar_dados(arquivo_carregado)

    # Mostrar a tabela inicial
    st.subheader("📋 Dados Carregados")
    st.dataframe(dados_rfv.head())

    # Estatísticas gerais
    st.subheader("📈 Estatísticas Descritivas")
    st.write(dados_rfv.describe())

    # Análise de cada métrica
    st.subheader("🔍 Análise das Métricas RFV")

    # Recência
    st.markdown("### Recência")
    grafico_recencia = plt.figure(figsize=(8, 5))
    sns.histplot(dados_rfv['Recencia'], kde=True, bins=30)
    plt.title("Distribuição da Recência")
    plt.xlabel("Dias desde a última compra")
    plt.ylabel("Frequência")
    st.pyplot(grafico_recencia)

    # Frequência
    st.markdown("### Frequência")
    grafico_frequencia = plt.figure(figsize=(8, 5))
    sns.histplot(dados_rfv['Frequencia'], kde=True, bins=30, color='orange')
    plt.title("Distribuição da Frequência")
    plt.xlabel("Número de compras")
    plt.ylabel("Frequência")
    st.pyplot(grafico_frequencia)

    # Valor Monetário
    st.markdown("### Valor Monetário")
    grafico_valor = plt.figure(figsize=(8, 5))
    sns.histplot(dados_rfv['Valor'], kde=True, bins=30, color='green')
    plt.title("Distribuição do Valor Monetário")
    plt.xlabel("Valor Gasto (em unidades monetárias)")
    plt.ylabel("Frequência")
    st.pyplot(grafico_valor)

    # Segmentação RFV
    st.subheader("🎯 Segmentação RFV")
    st.markdown("""
    A análise RFV normalmente segmenta os clientes em diferentes grupos, como:  
    - **Melhores clientes:** Alta Recência, Alta Frequência, Alto Valor Monetário.  
    - **Clientes em Risco:** Alta Recência, Baixa Frequência e Valor Monetário.  
    - **Potenciais Perdas:** Alta Recência, Baixa Frequência e Baixo Valor Monetário.
    """)

    if 'Segmento' in dados_rfv.columns:
        grafico_segmentos = plt.figure(figsize=(8, 5))
        dados_rfv['Segmento'].value_counts().plot(kind='bar')
        plt.title("Distribuição dos Segmentos")
        plt.xlabel("Segmento")
        plt.ylabel("Contagem")
        st.pyplot(grafico_segmentos)

    # Filtros interativos
    st.subheader("⚙️ Filtros Interativos")
    st.markdown("Use os filtros abaixo para explorar os dados RFV de maneira interativa.")

    # Filtros de Recência, Frequência e Valor Monetário
    min_recencia, max_recencia = int(dados_rfv['Recencia'].min()), int(dados_rfv['Recencia'].max())
    filtro_recencia = st.slider("Filtrar por Recência (dias):", min_value=min_recencia, max_value=max_recencia, value=(min_recencia, max_recencia))

    min_frequencia, max_frequencia = int(dados_rfv['Frequencia'].min()), int(dados_rfv['Frequencia'].max())
    filtro_frequencia = st.slider("Filtrar por Frequência (compras):", min_value=min_frequencia, max_value=max_frequencia, value=(min_frequencia, max_frequencia))

    min_valor, max_valor = float(dados_rfv['Valor'].min()), float(dados_rfv['Valor'].max())
    filtro_valor = st.slider("Filtrar por Valor Monetário:", min_value=min_valor, max_value=max_valor, value=(min_valor, max_valor))

    # Aplicar filtros
    dados_filtrados = dados_rfv[
        (dados_rfv['Recencia'] >= filtro_recencia[0]) & (dados_rfv['Recencia'] <= filtro_recencia[1]) &
        (dados_rfv['Frequencia'] >= filtro_frequencia[0]) & (dados_rfv['Frequencia'] <= filtro_frequencia[1]) &
        (dados_rfv['Valor'] >= filtro_valor[0]) & (dados_rfv['Valor'] <= filtro_valor[1])
    ]

    st.markdown("### Dados Filtrados")
    st.dataframe(dados_filtrados)

    # Baixar os dados filtrados
    st.markdown("### 📥 Baixar Dados Filtrados")
    csv = dados_filtrados.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Baixar CSV",
        data=csv,
        file_name="dados_filtrados_rfv.csv",
        mime="text/csv"
    )

else:
    st.warning("Por favor, faça o upload do arquivo RFV para começar a análise.")
