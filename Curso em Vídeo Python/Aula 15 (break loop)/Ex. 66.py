print('Leitor de soma de números...')
print('>>> Para parar, digite \033[1m999\033[0m\n')

s = c = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n

print(f'\nVocê digitou {c} números e a soma entre eles é {s}')