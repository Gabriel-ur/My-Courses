import pandas as pd

# a biblioteca pandas serve para visualização e manipulação de dados
# ele é usado principalmente para dados tabulares (em tabela)
# assim, ele é basicamente um conjunto de chaves e valores em forma de tabela

dados = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Cidade': ['Nova York', 'Los Angeles', 'Chicago'],
        'Idade': [25, 30, 35]}

# 'DataFrame' transforma os dados em uma tabela (dataframe)
df = pd.DataFrame(dados)

# 'head' mostra as primeiras n linhas do dataframe (por padrão: 5)
print(df.head(3))

print(f'\n{'-=-'*5}\n')

# é possível mudar especificamente os nomes das colunas e das linhas
df = pd.DataFrame(dados,
             columns = ['Nome', 'Idade', 'Cidade', 'Estado'],
             index = ['pessoa1', 'pessoa2', 'pessoa3'])

print(df)

print(f'\n{'-=-'*5}\n')

# 'values' retorna um array com todos os valores do dataframe
print(df.values)

print(f'\n{'-=-'*5}\n')

# 'types' retorna o tipo de cada valor do dataframe (object: str)
print(df.dtypes)

print(f'\n{'-=-'*5}\n')

# 'columns' retorna uma lista com o nome de todas as colunas e o tipo
print(df.columns)

print(f'\n{'-=-'*5}\n')

print(df['Idade'])

print(f'\n{'-=-'*5}\n')

print(df[['Nome', 'Cidade']])

print(f'\n{'-=-'*5}\n')

# 'filter' retorna todos os dados de uma linha ou coluna de escolha
print(df.filter(items = ['pessoa1'], axis = 0))

print(f'\n{'-=-'*5}\n')

# 'isna' retorna true para todos os valores ausentes do dataframe
print(df.isna())
print(f'\n{'-=-'*5}\n')
print(df['Estado'].isna())