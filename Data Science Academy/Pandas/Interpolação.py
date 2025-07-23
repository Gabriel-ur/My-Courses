import pandas as pd

# "Interpolação" é o ato de substituir valores NaN em um dataframe
# isso é muito importante pois dados são muito valiosos, ou seja, sempre deve-se evitar desperdiçá-los

# 'read_csv' transforma um arquivo CSV (valores separados por vírgula) em um dataframe
df = pd.read_csv(r"C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Pandas\dataset.csv")

print(df.head(10))

print(f'\n{'-=-'*5}\n')

# retorna a soma de todos os valores ausentes de cada coluna
print(df.isna().sum())

print(f'\n{'-=-'*5}\n')

# calcula a moda dos valores da coluna "Quantidade" (que é a única que apresenta valores NaN)
# 'index[0]' serve para mostrar apenas a maior moda ('value_counts' conta todos os elementos, não só o que aparece mais)
moda = df['Quantidade'].value_counts().index[0]
print(f'Moda = {moda}')

# calcula a média dos valores da coluna "Quantidade"
media = df['Quantidade'].mean()
print(f'Média = {media:.2f}')

print(f'\n{'-=-'*5}\n')

# 'fillna' preenche todos os valores NaN com base em um valor (entre {}, depois dos :)
# 'inplace', quando True, substitui o valor no dataframe original (se não especificar, ele cria uma cópia com os valores substituídos)
df.fillna({'Quantidade': moda}, inplace = True)
print(df.isna().sum())