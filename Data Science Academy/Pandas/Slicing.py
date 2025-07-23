import pandas as pd
dados = {'Nome': ['Alice', 'Bob', 'Charlie'],
        'Cidade': ['Nova York', 'Los Angeles', 'Chicago'],
        'Idade': [25, 30, 35]}
df = pd.DataFrame(dados,
             columns = ['Nome', 'Idade', 'Cidade', 'Estado'],
             index = ['pessoa1', 'pessoa2', 'pessoa3'])

# o pandas também permite fatiamento, principalmente nos dataframes
# o último elemento de um fatiamento, no pandas, NÃO É EXCLUSIVO, diferentemente do numpy e o prórpio python

print(df['pessoa1' : 'pessoa2'])

print(f'\n{'-=-'*5}\n')

print(df[df['Idade'] >= 30])