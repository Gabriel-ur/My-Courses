import pandas as pd
df = pd.read_csv(r"C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Pandas\dataset.csv")

# é possível realizar várias ações com str no pandas, incluindo filtrar, dividir, cortar, substituir e combinar

# '.str' é colocado para indicar um tratamento envolvendo strings
print(df.Segmento.value_counts())
print(f'\n{'-=-'*5}\n')
print(df[df.Segmento.str.startswith('Con')].head(3)) # 'startswith' filtra o que começa com o parâmetro indicado
print(df[df.Segmento.str.endswith('ate')].head(3)) # 'endswith' filtra o que termina com o parâmetro indicado

print(f'\n{'-=-'*5}')
print(f'{'-=-'*5}\n')

# 'split()' recebe como parâmetro o caracter desejado para dividir uma informação em várias
print(df['ID_Pedido'].head(3))
print(f'\n{'-=-'*5}\n')
print(df['ID_Pedido'].str.split('-').head(3)) # o 'split()' cria uma lista de valores separados pelo caracter de parâmetro
print(f'\n{'-=-'*5}\n')
df['Ano'] = df['ID_Pedido'].str.split('-').str[1] # cria uma nova coluna com o segundo valor da lista do split
print(df.head(3))

print(f'\n{'-=-'*5}')
print(f'{'-=-'*5}\n')

# 'strip()' (ou lstrip e rstrip) retira o parâmetro indicado de um valor
print(df['Data_Pedido'].sample(3))
print(f'\n{'-=-'*5}\n')
print(df['Data_Pedido'].str.lstrip('20').sample(3))

print(f'\n{'-=-'*5}')
print(f'{'-=-'*5}\n')

# 'replace()' substitui uma string com base em 2 parâmetros (o que vai ser substituído e pelo o que deve ser substituído)
df['ID_Cliente'] = df['ID_Cliente'].str.replace('CG', 'AX')
print(df.head(3))

print(f'\n{'-=-'*5}')
print(f'{'-=-'*5}\n')

# 'cat()' permite "concatenar" variáveis, criando uma nova
df['Pedido_Segmento'] = df['ID_Pedido'].str.cat(df['Segmento'], sep = '-') # 'sep' é o separador que junta ambos
print(df.head(3))