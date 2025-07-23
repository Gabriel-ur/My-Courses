import numpy as np

# o numpy (Numerical Python) é uma biblioteca externa python usada para lidar com arrays (estruturas com múltiplos valores armazenados, como listas)
# o numpy é resumidamente mais rápido e prático para lidar com grandes quantidades de dados em relação às listas

# um objeto array em numpy se chama "ndarray" ('nd' significa Número de Dimensões)
# qualquer estrutura python que se comporta como array (como listas ou tuplas) pode ser passada como argumento, sendo transformada em array pelo numpy
# as arrays podem ser visualizadas como elementos em linhas e colunas

array1 = np.array([1,2,3,4,5])
print(array1)

print(f'\n{'-=-'*5}\n')

# arrays possuem dimensões (profundidade), se relacionando com o conceito de "aninhamento"

# 0-D (cada valor de um array se comporta como um array de 0 dimensões)
a = np.array(42)
# 1-D (um array de uma dimensão com elementos 0-D)
b = np.array([1, 2, 3, 4, 5])
# 2-D (um array de duas dimensões com elementos 1-D) (normalmente representa matrizes)
c = np.array([[1, 2, 3], [4, 5, 6]])
# 3-D (um array de três dimensões com elementos 2-D)
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# 'ndim' retorna a quantidade de dimensões de uma array
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print(f'\n{'-=-'*5}\n')

# uma array pode ter uma quantidade infinita de dimensões
# o 'ndmin' serve para informar a quantidade de dimensões que a array deve ter ao criá-la

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print(f'Número de dimensões: {arr.ndim}')

print(f'\n{'-=-'*5}\n')