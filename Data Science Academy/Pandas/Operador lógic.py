import pandas as pd
df = pd.read_csv(r"C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Pandas\dataset.csv")

# é possível usar operadores lógicos para filtrar ainda mais especificamente os dados do dataframe

# '&' significa "and": ambas as preposições devem ser verdadeiras
print(df[(df.Segmento == 'Home Office') & (df.Regiao == 'South')].sample(5)) # 'sample' retorna os dados de aleatoriamente

print(f'\n{'-=-'*5}\n')

# '|' significa "or": apenas um deve ser verdadeiro
print(df[(df.Segmento != 'Home Office') | (df.Regiao != 'South')].tail()) # 'tail' retorna o fim do dataframe