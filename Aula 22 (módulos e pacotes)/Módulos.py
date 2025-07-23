#é possível criar os próprios módulos e importá-los
#um conjunto de módulos se chama pacote (ou biblioteca)
#o python entende uma pasta como pacote, e os documentos dentro dela (terminados em .py) de módulos

from uteis import numeros, strings

n = int(input('Digite um valor: '))
print(f'\nO fatorial de {n} é {numeros.fatorial(n)}')
print(f'O dobro de {n} é {numeros.dobro(n)}')
print(f'A metade de {n} é {numeros.metade(n)}\n')

txt = input('Digite um texto: ')
strings.escreva(txt)