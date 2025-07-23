# %%
from matplotlib import pyplot as plt

# 'scatter()' cria um gráfico de dispersão
# gráficos de dispersão são utilizados para analisar a relação de duas variáveis numéricas

x1 = [1,3,5,7,9,3,1,8,4]
y1 = [7,5,2,7,4,5,5,10,3]

plt.scatter(x1, y1, label = 'Pontos', color = 'gold', marker = 'o') # 'marker' é o formato dos pontos
plt.legend()
plt.show()