from time import sleep
from random import randint

nums = []


def sorteio():
    print('Sorteando os 5 valores da lista:', end=' ')
    for c in range(5):
        n = randint(0, 100)
        sleep(0.5)
        nums.append(n)
        print(f'\033[34m{n}\033[0m', end=' ', flush=True)

    print('\033[32mPRONTO!\033[0m')


def soma_par():
    soma = 0
    for c in range(len(nums)):
        if nums[c] % 2 == 0:
            soma += nums[c]
    
    print(f'A soma dos valores \033[32mPARES\033[0m de {nums} é \033[35m{soma}\033[0m')


sorteio()
sleep(0.5)
soma_par()