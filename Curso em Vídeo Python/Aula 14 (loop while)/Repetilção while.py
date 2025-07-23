#o while serve pra quando você não souber o limite do loop ou não houver padrões previsíveis, por exemplo
#o while é uma "estrutura de repetição com teste lógico"

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0 and n % 2 == 0:
        par += 1
    elif n != 0 and n % 2 != 0:
        impar += 1
print(f'\nVocê digitou {par} números pares e {impar} números ímpares.')