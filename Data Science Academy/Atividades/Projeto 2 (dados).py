# Pergunta de Negócio 1: Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
import pandas as pd
df = pd.read_csv(r'ambiente_virtual\Atividades\dataset.csv')

cidade_maior_valvenda_officesupplies = df[df['Categoria'] == 'Office Supplies'].groupby('Cidade')['Valor_Venda'].sum().idxmax()

print(f'A cidade com o maior valor de venda para produtos da categoria "Office Supplies" é \033[32m{cidade_maior_valvenda_officesupplies}\033[0m')

# %%
# Pergunta de Negócio 2: Qual o Total de Vendas Por Data do Pedido?
# Demonstre o resultado através de um gráfico de barras

from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv(r'C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Atividades\dataset.csv')

tot_vendas_data = df.groupby('Data_Pedido')['Valor_Venda'].sum()


plt.figure(figsize = (20, 6))
tot_vendas_data.plot(x = 'Data do Pedido', y = 'Valor da Venda')
plt.title('Total de Vendas Por Data do Pedido')
plt.show()

# %%
# Pergunta de Negócio 3: Qual o Total de Vendas por Estado?
# Demonstre o resultado através de um gráfico de barras

from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
df = pd.read_csv(r'C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Atividades\dataset.csv')


tot_vendas_estado = df.groupby('Estado')['Valor_Venda'].sum()
cores = ['crimson' if vendas < 45623 else 'deepskyblue' for vendas in tot_vendas_estado]

legenda = [Patch(color='deepskyblue', label='Vendas acima da média'), 
           Patch(color='crimson', label='Vendas abaixo da média')]
plt.legend(handles=legenda, title='Legenda')


tot_vendas_estado.plot(kind = 'bar', 
                       x = 'Estado', 
                       y = 'Valor da venda',
                       color = cores,
                       width = 0.7,
                       figsize= (12, 6))

plt.title('Total de Vendas por Estado')
plt.show()

# %%
# Pergunta de Negócio 4: Quais São as 10 Cidades com Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de barras

from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv(r'C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Atividades\dataset.csv')

tot_vendas_cidade = df.groupby('Cidade')['Valor_Venda'].sum().reset_index()
top10_cidades = tot_vendas_cidade.nlargest(10, 'Valor_Venda')

top10_cidades.plot(kind= 'bar',
                   x= 'Cidade',
                   y= 'Valor_Venda',
                   color = 'gold',
                   figsize= (14, 6),
                   width = 0.8,)

plt.xticks(rotation = 0)
plt.title('Top 10 Cidades com Maior Total de Vendas')
plt.show()

# %%
# Pergunta de Negócio 5: Qual Segmento Teve o Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de pizza

from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv(r'C:\Users\Gabriel\OneDrive\Data Science Academy\ambiente_virtual\Atividades\dataset.csv')

tot_vendas_segmento = df.groupby('Segmento')['Valor_Venda'].sum().reset_index()

def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format

plt.figure(figsize = (16, 6))

plt.pie(tot_vendas_segmento['Valor_Venda'],
        colors = ['darkorchid', 'mediumorchid', 'violet'],
        labels = tot_vendas_segmento['Segmento'],
        autopct = autopct_format(tot_vendas_segmento['Valor_Venda']),
        wedgeprops = {'width': 0.15},
        startangle = 350)


plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(tot_vendas_segmento['Valor_Venda']))), xy = (-0.5, 0))

plt.title('Total de Vendas Por Segmento')
plt.show()