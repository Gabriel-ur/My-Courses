# %%
import matplotlib as mpl

# Matplotlib é uma biblioteca python dedicada para criação de gráficos
# "plot" significa simplesmente um gráfico; "plotar" significa criar um gráfico
# a função 'plot()' cria um gráfico de linha
# gráficos de linha são usados para visualizar algo ao longo do tempo

# pyplot é uma "sub biblioteca" do matplotlib que fornece funções para a geração e controle de gráficos
from matplotlib import pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9]) # cria um gráfico com os parâmetros fornecidos
plt.title("Gráfico 1")


plt.figure()  # cria um gráfico separado
plt.plot([1, 2, 3], [2, 5, 7])
plt.title("Gráfico 2")


x = [32, 75, 13, 45]
y = [81, 59, 21, 57]

plt.figure()
plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title("Gráfico 3")


plt.figure()
plt.plot(x, y, label = 'Evolução de ...') # 'label' indica o nome da linha do gráfico
plt.legend() # cria a legenda das linhas


plt.show()  # mostra os dois gráficos