import sqlite3

# sqlite é um banco de dados relacional simples que já vem embutido no python
# é muito usado para pequenos projetos e aplicações pequenas/médias (mobile/desktop)

con = sqlite3.connect(r'ambiente_virtual\SQL\cap12_dsa.db') # 'connect()' recebe como argumento o banco de dados e se conecta a ele

cursor = con.cursor() # 'cursor()' permite percorrer o banco de dados

# 'query' consulta algo do banco de dados
# tudo que estiver em maiúsculo representa uma instrução em SQL
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

cursor.execute(sql_query) # 'execute()' executa a consulta estabelecida anteriormente

print(cursor.fetchall()) # 'fetchall()' mostra os resultados obtidos na consulta
