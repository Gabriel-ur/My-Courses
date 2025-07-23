import pandas as pd
df = pd.read_csv(r"C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Pandas\dataset.csv")

# 'query' é uma função usada para "filtrar" um dataframe, criando um novo apenas com o intervalo de valores desejado

# 'describe' retorna informações sobre um dataframe/coluna/linha, como valor mínimo, máximo, média e desvio padrão
print(df.Valor_Venda.describe())

df2 = df.query('300 < Valor_Venda < 1000')

print(f'\n{'-=-'*5}\n')

print(df2.Valor_Venda.describe())