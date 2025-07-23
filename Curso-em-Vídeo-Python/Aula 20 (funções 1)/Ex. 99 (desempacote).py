from time import sleep

def maior(* num):
    print('-=-' * 12)
    print('Analisando os valores...')

    for c in range(len(num)):
        sleep(0.3)
        print(f'\033[32m{num[c]}\033[0m', end=' ', flush=True)
    
    if len(num) == 0:
        sleep(0.3)
        print('\033[31mNenhum valor informado\033[0m')
    else:
        sleep(0.3)
        print(f'\nForam informados \033[31m{len(num)}\033[0m números ao todo.')
        sleep(0.3)
        print(f'O maior valor informado foi \033[36m{max(num)}\033[0m')


maior(3, 1, 5, 2, 5, 12, 2, 7)
maior(6, 9, 10, 4, 5, 7)
maior(21, 3, 12, 2)
maior(73, 49)
maior(2)
maior()