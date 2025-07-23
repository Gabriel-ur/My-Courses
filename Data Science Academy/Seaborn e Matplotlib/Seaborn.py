# %%
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import random

# o seaborn é uma biblioteca para geração de gráficos estatísticos
# ele usa o matplotlib como base (não funciona sem ele)
# ambos são muito semelhantes mas o seaborn cria gráficos mais bonitos 

dados = sns.load_dataset('tips')
print(dados.head(3))

# 'jointplot()' cria um gráfico de dispersão relacionando duas variáveis e os gráficos individuais de histograma e densidade de cada variável no topo e na direita do gráfico
sns.jointplot(data = dados, # 'data' se refere ao dataframe utilizado para o gráfico
              x = 'total_bill', 
              y = 'tip', 
              kind = 'reg') # 'kind' informa o tipo do gráfico central. Por padrão: scatter (dispersão)

# 'lmplot()' cria um gráfico de regressão linear (Linear Model Plot) separado por categorias
sns.lmplot(data = dados,
           x = 'total_bill', 
           y = 'tip',
           col = 'smoker') # 'col' informa a terceira variável (categoria) para ser usada como colunas


df = pd.DataFrame()
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(40, 200), 30)

sns.jointplot(data = df,
              x = 'idade',
              y = 'peso',
              kind = 'reg')

# 'kdeplot()' cria um gráfico de densidade
plt.figure()
sns.kdeplot(df.idade, color = 'purple')

plt.figure()
sns.kdeplot(df.peso, color = 'red')
# %%
