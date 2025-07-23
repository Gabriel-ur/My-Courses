import sqlite3
import pandas as pd
con = sqlite3.connect(r'ambiente_virtual\SQL\cap12_dsa.db')
cursor = con.cursor()

query = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query)
dados = cursor.fetchall()


# transforma os dados em uma tabela pandas
df = pd.DataFrame(dados, columns = ['Id_Pedido',
                                    'Id_Cliente',
                                    'Nome_Produto',
                                    'Valor_Unitário',
                                    'Unidades_Vendidas',
                                    'Custo'])

print(df.head())
print(f'\n{'-=-'*53}\n')

# fecha o banco de dados pois agora é possível utilizar o data frame que foi criado em linguagem pandas
cursor.close()
con.close()

# calcula a média usando linguagem pandas invés de SQL
media_unidades_vendidas = df['Unidades_Vendidas'].mean()
print(media_unidades_vendidas)
print(f'\n{'-=-'*53}\n')

# calcula a média de unidades vendidas por produto usando groupby com pandas
# ** as colunas que se quer agrupar vão entre () e as que se quer calcular a média vão entre []
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(media_unidades_vendidas_por_produto.head(5))
print(f'\n{'-=-'*53}\n')

# média de unidades vendidas por produto cujo valor unitário é maior que 199
media_produto_199 = df[df['Valor_Unitário'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(media_produto_199.head(5))