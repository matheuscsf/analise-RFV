# 📂 Dados de Exemplo - RFV

Esta pasta contém os dados de exemplo utilizados no projeto para análise RFV.

---

## 📄 Arquivo: `RFV.csv`

### Descrição Geral
O arquivo `RFV.csv` é um exemplo de dados estruturados para aplicação da metodologia RFV (Recência, Frequência e Valor Monetário). Este dataset é usado tanto para demonstração do notebook quanto para a aplicação Streamlit.

---

### 📋 Estrutura do Arquivo

O arquivo está no formato CSV com as seguintes colunas:

| Coluna      | Descrição                                                                 |
|-------------|---------------------------------------------------------------------------|
| `ClienteID` | Identificador único do cliente.                                          |
| `Recencia`  | Número de dias desde a última compra do cliente.                         |
| `Frequencia`| Quantidade de compras realizadas pelo cliente.                           |
| `Valor`     | Valor total gasto pelo cliente (em unidades monetárias).                 |
| `Segmento`  | (Opcional) Segmentação RFV aplicada ao cliente (ex.: "Melhor Cliente"). |

---

### 🌟 Como Usar os Dados

- **Para análise RFV no notebook:**  
  Use este arquivo como entrada no notebook `Analise RFV.ipynb` para realizar o cálculo e a segmentação RFV.

- **Na aplicação Streamlit:**  
  Faça o upload deste arquivo na aplicação `app_rfv.py` para explorar os gráficos e filtros interativos.

---

### 🔔 Nota

Os dados fornecidos são fictícios e têm como único propósito demonstrar a funcionalidade do projeto. Certifique-se de usar dados reais apenas em ambientes seguros.
