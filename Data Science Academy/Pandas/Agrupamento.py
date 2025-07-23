import pandas as pd
df = pd.read_csv(r"C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Pandas\dataset.csv")

# é possível agrupar dados de um dataframe com a função 'groupby'
# essa função é útil para visualizar melhor a relação entre variáveis distintas
# em adição, a função 'agg' (agregação) mostra os dados com base em outras funções

# aqui, as variáveis qualitativas estão sendo agrupadas em relação à média da variável quantitativa
print(df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean())

print(f'\n{'-=-'*5}\n')

# aqui, após o agrupamento, é mostrado a média, desvio padrão e contagem de elementos da variável que ficou fora do groupby ('Valor_Venda')
# 'agg()' recebe como parâmetro uma lista de funções
print(df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']))