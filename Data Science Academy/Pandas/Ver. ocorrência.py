import pandas as pd
df = pd.read_csv(r"C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Pandas\dataset.csv")

# é possível verificar a ocorrência de valores específicos em um dataframe com a função 'isin()'

# 'shape' retorna a quantidade de linhas e colunas de um dataframe
print(df.shape)

print(f'\n{'-=-'*5}\n')

# 'isin()' aceita uma lista como argumento; o print mostra a quantidade de linhas e colunas que o dataframe fica após a filtragem
print(df[df['Quantidade'].isin([5, 11])])

print(f'\n{'-=-'*5}\n')

# desse jeito, printa apenas a quantidade de linhas e colunas após a filtragem
print(df[df['Quantidade'].isin([5, 11])].shape)