import numpy as np
arr = np.diag(np.arange(21))

# 'slicing' em python significa "fatiar" um objeto para pegar os elementos do índice x ao índice y
# é possível passar o índice inicial, final e o step
'''Por padrão:

inicial: 0 (incluso)
final: comprimento do array (excluso)
step: 1
'''

print(f'\nDa 5° à 10° linha: \n{arr[5:11]}')
print(f'\nAté a 15° linha: \n{arr[:16]}')
print(f'\nDa 10° em diante: \n{arr[10:]}')
print(f'\nDa 4° à 16° de 2 em 2: \n{arr[4:17:2]}')
print(f'\nDa 1° à 20° de 5 em 5: \n{arr[::5]}\n\n')

# 'flatten' serve para tornar um array multidimensional em um array unidimensional
arr1 = np.array([[1 ,2], [3, 4]])
print(f'Array multidimensional: \n{arr1}\n')
print(f'Array unidimensional: \n{arr1.flatten()}')