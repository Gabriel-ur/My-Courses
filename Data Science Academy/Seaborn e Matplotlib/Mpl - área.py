# %%
from matplotlib import pyplot as plt

# 'stackplot()' cria um gráfico de área empilhada
# gráficos de área mostram a evolução de variáveis ao longo do tempo, com foco no volume
# semelhante aos gráficos de linha, mas possui preenchimento abaixo das linhas

dias = [1,2,3,4,5,6,7]
horas_sono = [8,6,9,5,4,6,7]
horas_estudo = [1,0,2,0,0,4,2]
horas_trabalho = [8,8,8,8,7,0,0]

plt.stackplot(dias, horas_sono, horas_estudo, horas_trabalho, 
              labels = ['Horas de sono', 'Horas de estudo', 'Horas de trabalho'], 
              colors = ['lime','indigo','teal'], 
              alpha = 0.6) # 'alpha' altera a transparência
plt.legend()
plt.show()

# do jeito abaixo, ele consegue deixar o transparente realmente transparente
# 'fill_between()' permite manipular cada preenchimento separadamente

# %%
import matplotlib.pyplot as plt

dias = [1,2,3,4,5,6,7]
horas_sono = [8,6,9,5,4,6,7]
horas_estudo = [1,0,2,0,0,4,2]
horas_trabalho = [8,8,8,8,7,0,0]

plt.fill_between(dias, horas_sono, color='blue', alpha=0.7, label='Horas de sono')
plt.fill_between(dias, horas_estudo, color='green', alpha=0.7, label='Horas de estudo')
plt.fill_between(dias, horas_trabalho, color='red', alpha=0.7, label='Horas de trabalho')

plt.legend()
plt.title("Sobreposição com Transparência (fill_between)")
plt.show()