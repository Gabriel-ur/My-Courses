import numpy as np

arr_E = np.array([24, 61, 92, 79, 50, 108])

# é possível fazer análises estatísticas com o NumPy devido a algumas de suas funções
# ** o próprio python já vem instalado com a biblioteca "statistics", oferecendo funções para tratamento estatístico, mas possui limitações 

# 'mean' retorna a média do array
print(f'Mean: {np.mean(arr_E)}')

print(f'\n{'-=-'*4}\n')

# 'std' retorna o desvio padrão (standard deviation)
print(f'Std: {round(np.std(arr_E), 2)}')

print(f'\n{'-=-'*4}\n')

# 'var' retorna a variância
print(f'Var: {round(np.var(arr_E), 2)}')

print(f'\n{'¨'*150}\n')

# também é possível realizar operações matemáticas com numpy
# novamente, o próprio python já possui funções semelhantes

# 'arange' cria um array com base num valor mínimo e máximo
arr_M = np.arange(5, 100, 10)
print(f'Arange: {arr_M}')

print(f'\n{'-=-'*4}\n')

# 'sum' retorna a soma dos elementos do array
print(f'Sum: {np.sum(arr_M)}')

print(f'\n{'-=-'*4}\n')

# 'pro' retorna o produto dos elementos do array
print(f'Prod: {np.prod(arr_M)}')

print(f'\n{'-=-'*4}\n')

# 'cumsum' retorna uma lista com a soma progressiva dos elementos do array (soma os 2 primeiros, depois soma com o 3°...)
print(f'Cumsum: {np.cumsum(arr_M)}')

print(f'\n{'-=-'*4}\n')

# 'add' retorna um array que é a soma de outros arrays COM A MESMA QUANTIDADE DE ELEMENTOS**
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(f'Add: {np.add(arr1, arr2)}')

print(f'\n{'-=-'*4}\n')

# 'dot' multiplica array por array (N° COLUNAS DA PRIMEIRA = N° LINHAS DA SEGUNDA) ou array por vetor
print(f'Dot: {np.dot(arr1, arr2)}')
# ou
print(f'@ (dot): {arr1 @ arr2}')