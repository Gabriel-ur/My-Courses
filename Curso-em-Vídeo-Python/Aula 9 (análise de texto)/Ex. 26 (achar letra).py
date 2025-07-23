from unidecode import unidecode
#essa biblioteca tira os acentos das letras

print('Leitor de letras\n')
frase = unidecode(input('Digite uma frase: ').upper().strip())
letra = input('\nQual letra deseja analisar? ').upper().strip()

print(f'\nA letra "{letra}" aparece {frase.count(letra)} vezes na frase')
print(f'A primeira letra "{letra}" aparece na {frase.find(letra)+1}° posição')
print(f'A última letra "{letra}" aparece na {frase.rfind(letra)+1}° posição')