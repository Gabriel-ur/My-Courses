def leiaInt(msg):
    """
    Verifica se a variável do usuário é numérica:
        msg: input
    """
    while True:
        n = input(msg)
        if n.isnumeric():
            return n
        else:
            print('\033[31mERRO. Digite um número inteiro.\033[0m')


n = leiaInt('Digite um número: ')

print(f'O valor que digitou é \033[32m{n}\033[0m')