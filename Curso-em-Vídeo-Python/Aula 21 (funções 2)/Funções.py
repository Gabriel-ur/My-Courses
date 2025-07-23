#'docstrings' servem como documentação da funcionalidade de uma função (tipo manual)
#em programação, é sempre necessário descrever as funções, para que outros programadores entendam

def contador(i, f, p): #isso não é tão simples de entender
    """
    >> Cria um contador onde:
        i: número inicial da contagem
        f: número final da contagem (INCLUSO)
        p: passo da contagem
    """
    for c in range(i, f + 1, p):
        print(c, end=' ')
    print('FIM')


contador(0, 100, 10)

help(contador)

#é possível fazer uma função que, caso não receba um parâmetro, ela não é afetada
# isso é chamado de 'parâmetros opcionais'

def soma(a=0, b=0, c=0):
    s = a + b + c 
    print(f'A soma vale {s}')

soma(1, 2) #como não tem o 'c', daria erro, porém, já que não foi informado, ele vale 0, não impactando nd

def mult(a=1, b=1, c=1):
    m = a * b * c
    print(f'A multiplicação vale {m}\n')

mult(3, 4)

#o conceito de 'escopo' é basicamente a posição de variáveis num programa

def teste():
    a = 7 #'a' tem ESCOPO LOCAL
    b = 20 #'b' (dentro da função) tem ESCOPO LOCAL
    print(f'Na função teste, (a) vale {a}')
    print(f'Na função teste, (b) vale {b}')

b = 2 #'b' (no programa principal) tem ESCOPO GLOBAL

teste()
print(f'No programa principal, (b) vale {b}\n')

def teste2():
    global x #o 'global' torna a váriavel global. aqui, x = 10 vale para o programa principal
    x = 10
    print(f'Em teste2, (x) vale {x}')

x = 3432

teste2()
print(f'No programa principal, (x) vale {x}')