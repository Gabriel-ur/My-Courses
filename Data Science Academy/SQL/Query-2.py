import sqlite3
con = sqlite3.connect(r'ambiente_virtual\SQL\cap12_dsa.db')
cursor = con.cursor()

query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa' # 'AVG' retorna a média (avarege) do parâmetro dado

cursor.execute(query2)

print(cursor.fetchall())
print(f'\n{'-=-'*53}\n')

# a query abaixo seleciona a coluna Nome_Produto, calcula a média da coluna Unidades_Vendidas e às agrupa com base em cada dado diferente da coluna Nome_Produto
# como regra geral, a coluna que não está na função de agregação (nesse caso, AVG) vai para o GROUP BY
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'

cursor.execute(query3)

print(cursor.fetchall()[:16])
print(f'\n{'-=-'*53}\n')

query4 = '''SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto''' # 'WHERE' serve como um filtro; funciona de forma semelhante ao "if/else" ("selecione a coluna Nome_Produto da tabela tb_vendas_dsa, calcule a media de unidades vendidas - apenas quando o valor unitário for maior que 199 - e agrupe os dados com base no nome do produto")

cursor.execute(query4)

print(cursor.fetchall())
print(f'\n{'-=-'*53}\n')

query5 = '''SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10''' # 'HAVING' serve para filtrar os grupos criados pelo GROUP BY

cursor.execute(query5)

print(cursor.fetchall())

# é importante fechar a conexão e o cursor para evitar falhas de segurança e problemas no geral
cursor.close()
con.close()