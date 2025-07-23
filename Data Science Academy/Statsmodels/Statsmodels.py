from statsmodels import api as sm
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Statsmodels é uma biblioteca python utilizada para anásile estatística aprofundada

# pergunta: a metragem de um imóvel influencia no valor de seu aluguel?

df = pd.read_csv(r'ambiente_virtual\Statsmodels\dataset.csv')

print(df.shape)
print(f'\n{'-=-'*53}\n')
print(df.columns)
print(f'\n{'-=-'*53}\n')
print(df.head())
print(f'\n{'-=-'*53}\n')

# Análise exploratória: conhecer e entender os dados

print(df.isnull().sum()) # retorna quantos falores ausentes existem no dataset
print(f'\n{'-=-'*53}\n')
print(df.describe()) # retorna um resumo estatístico do dataset
print(f'\n{'-=-'*53}\n')
print(df['valor_aluguel'].describe()) # retorna resumo estatístico da variável alvo
print(f'\n{'-=-'*53}\n')
sns.histplot(data=df, x= 'valor_aluguel', kde= True)
plt.figure()
print(df.corr()) # retorna a correlação entre as variáveis
sns.scatterplot(data=df, x= 'area_m2', y= 'valor_aluguel')
print(f'\n{'-=-'*53}\n')

# Regressão Linear modela a relação entre duas ou mais variáveis
# a função OLS (Ordinary Least Squares) em Statsmodels serve para ajustar o modelo de regressão linear

y = df['valor_aluguel']     # definição da variável alvo
x = df['area_m2']           # definição da variável independente
x = sm.add_constant(x)      # adição de constante para a variável independente

modelo = sm.OLS(y, x)       # cria o modelo OLS
resultado = modelo.fit()    # treina o modelo
print(resultado.summary())




plt.show()