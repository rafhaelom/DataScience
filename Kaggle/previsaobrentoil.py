#  Brent Oil Prices - Análise e Previsão de Preços Futuros 
# %% Importando Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
# %% Importando dados
df = pd.read_csv("BrentOilPrices.csv", sep=",")
# %% Análise Exploratória
df.info()
# %%
df.head()
# %%
df.tail()
# %% Verificando se exite valore ausentes.
df.isna().sum()
# %% Verificando se há valores duplicados
df.duplicated().sum()
# %% Vemos que precisa-se modificar a coluna Date 
# para o formato correto Ano-Mes-Dia
df["Date"] = pd.to_datetime(df["Date"])
df
# %% Verificando distribuição dos preços
df.describe()

# %% Criando gráfico para visualizar a distribuição de preços por ano
# Criando gráfico de linhas
plt.plot(df["Date"], df["Price"])
# Título
plt.title("Price per year")
# Visualizando
plt.show()
# %% Criando gráfico de barras
plt.bar(df["Date"], df["Price"])
plt.title("Price per year")
# Visualizando
plt.show()
