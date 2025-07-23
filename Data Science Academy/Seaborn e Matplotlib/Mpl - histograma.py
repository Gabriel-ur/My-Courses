# %%
from matplotlib import pyplot as plt
import random

# 'hist()' cria um histograma
# histogramas servem para mostrar a distribuição de frequência de variáveis contínuas

dados = [random.randint(0, 1000) for _ in range(1000)]

plt.hist(dados, 
         bins=100,      # 'bins' representa a quantidade de intervalos
         color='skyblue')
plt.xlabel("Número")
plt.ylabel("Frequência")
plt.show()