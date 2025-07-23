import numpy as np

# "indexiçação de array" nada mais é do que acessar um elemento da array pelo seu índice

# assim como no Python normal, as arrays iniciam com índice 0

arr1 = np.array([1, 2, 3, 4])
print(arr1)
print()
print(arr1[0])

print(f'\n{'-=-'*5}\n')


# confome aumentam os números de dimensões, os índices precisam ser especificados

arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr2)
print(f'\nElemento da primeira linha e segunda coluna: {arr2[0, 1]}')

print(f'\n{'-=-'*5}\n')

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)
print(f'\nTerceiro elemento da segunda array da primeira array: {arr3[0, 1, 2]}')

print(f'\n{'-=-'*5}\n')

# as arrays também suportam indexiçação negativa, para contar de trás pra frente

arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr4)
print(f'\nÚltimo elemento da segunda linha: {arr4[1, -1]}')