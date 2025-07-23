def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mERRO. O valor que digitou é inválido, tente novamente.\033[0m')
        else:
            return n
        

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[31mERRO. O valor que digitou é inválido, tente novamente.\033[0m')
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')

print(f'''\nO número inteiro que digitou é \033[32m{n1}!\033[0m :)
O número real que digitou é \033[32m{n2}!\033[0m :)''')