#essa linha é só graça mesmo

print('Bem vindo(a) à calculadora mais simples do universo! Nela, digite dois valores, que direi a soma destes')

#aqui tem que lembrar de colocar o "int" (ou variante disso, tipo float) na frente do input pra ele ser considerado númearo e não string

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

#se não colocar "int" ou companhia, esse '+' vai só colar os números um no outro

s = n1 + n2

print('A soma de', n1, 'e', n2, 'é', s)