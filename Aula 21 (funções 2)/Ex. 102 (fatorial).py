def fatorial(a, show=False):
    """
    Calcula o fatorial de um número:
        a: número a ser calculado o fatorial
        show: mostra as multiplicações (por padrão, NÃO MOSTRA)
        return: retorna o fatorial de a
    """
    f = 1
    for c in range(a, 0, -1):
    
        if show == True:
            print(c, end=' ')
            if c != 1:
                print('x ', end='')
            else:
                print('= ', end='')
        f *= c
    return f


num = int(input('Digite um número: '))

print('-' * 20)
print(fatorial(num)) #colocar o 'print' aqui é MUITO IMPORTANTE, se n não funciona
print('-' * 20)

num = int(input('Digite um número: '))

print('-' * 20)
print(fatorial(num, True))