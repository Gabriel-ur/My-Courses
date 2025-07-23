import sqlite3
con = sqlite3.connect(r'ambiente_virtual\SQL\cap12_dsa.db')
cursor = con.cursor()

# query faz uma consulta no banco de dados com base em cláusulas SQL
# ** a ordem de escrita das cláusulas é: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT
# ** a ordem lógica de execução da query é: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT

#   FROM	    Escolhe a tabela base e faz joins, se houver
#   WHERE	    Filtra as linhas antes de qualquer agrupamento
#   GROUP BY	Agrupa as linhas com base em uma ou mais colunas
#   HAVING	    Filtra os grupos criados pelo GROUP BY
#   SELECT	    Seleciona as colunas e calcula funções como AVG(), SUM(), etc
#   ORDER BY	Ordena os resultados (ascendente ou descendente)
#   LIMIT	    Limita o número de linhas retornadas

query1 = 'SELECT * FROM tb_vendas_dsa' # traz todas as linhas e colunas da tabela

cursor.execute(query1)

# a linha abaixo cria uma lista com o nome de cada coluna
nomes_colunas = [description[0] for description in cursor.description] # 'description' retorna as informações das colunas (nome, tipo de dado, etc)

print(nomes_colunas)
print(f'\n{'-=-'*5}\n')

dados = cursor.fetchall() # retorna todas as linhas da tabela (os dados em si)

print(dados[:7])