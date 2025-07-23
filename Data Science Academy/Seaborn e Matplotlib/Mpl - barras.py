# %%
from matplotlib import pyplot as plt

# 'bar()' cria um gráfico de barras
# gráficos de barras são utilizados para comparar categorias

x1 = [1,3,5,7]
y1 = [7,5,2,7]

plt.bar(x1, y1, label = 'Barras', color = 'green')
plt.legend()

# %%
x2 = [2,4,6,8]
y2 = [7,8,2,4]

# como aqui não tem o 'figure()', os gráficos são sobrepostos
plt.bar(x1, y1, label = 'Categoria 1', color = 'blue')
plt.bar(x2, y2, label = 'Categoria 2', color = 'red')
plt.legend()

# %%
idades = [35,12,53,16,18,38,21,69,41,30,69,11,48,24,19,42,60,33,8,16,67,55,54,81,12,4,13,26]
pessoa = [p for p in range(len(idades))]

plt.bar(pessoa, idades)
plt.xlabel('Pessoas')
plt.ylabel('Idades')
plt.show()