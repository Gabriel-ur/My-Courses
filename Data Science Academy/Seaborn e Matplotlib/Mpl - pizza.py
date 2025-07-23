# %%
from matplotlib import pyplot as plt

# 'pie()' cria um gráfico de pizza
# gráficos de pizza são usados para mostrar proporções de um todo
# não são bons para muitas variáveis ou para variáveis semelhantes

fatias = [32, 9, 48] # dados das váriaveis do gráfico
atividades = ['Sono', 'Estudo', 'Trabalho'] # labels dos gráficos

plt.pie(fatias, 
        labels = atividades, 
        colors = ['blueviolet', 'mediumspringgreen', 'deepskyblue'],
        shadow = True, # cria uma sombra nas fatias
        explode= (0,0.2,0), # destaca a(s) fatia(s) desejada(s)
        startangle = 45) # indica o valor do ângulo inicial do gráfico
plt.show()