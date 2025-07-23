from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Scikit-Learn é uma biblioteca para criar modelos de machine learning

# pergunta: é possível prever o salário de uma pessoa com base nas suas horas de estudo semanais?

df = pd.read_csv(r'ambiente_virtual\Scikit-Learn\dataset.csv')

print(df.shape)
print(f'\n{'-=-'*53}\n')
print(df.columns)
print(f'\n{'-=-'*53}\n')
print(df.head())
print(f'\n{'-=-'*53}\n')

print(df.isnull().sum()) 
print(f'\n{'-=-'*53}\n')
print(df.describe()) 
print(f'\n{'-=-'*53}\n')
print(df.corr())
print(f'\n{'-=-'*53}\n')
sns.histplot(data=df, x= 'horas_estudo_mes', kde= True)
plt.figure()

X = np.array(df['horas_estudo_mes'])
X = X.reshape(-1, 1)
y = df['salario']

plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.figure()

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.2, random_state = 42)

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)
plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.plot(X, modelo.predict(X), color = "red", label = "Reta de Regressão com as Previsões do Modelo")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.figure()

score = modelo.score(X_teste, y_teste)
print(f"Coeficiente R^2: {score:.2f}")

# Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[21]]) 
# Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print(f"Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)





plt.show()