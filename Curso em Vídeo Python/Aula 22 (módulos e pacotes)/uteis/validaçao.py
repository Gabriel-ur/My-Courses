def validaçao(i):
    while True:
        p = input(i).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[31mERRO. "{p}" não é válido.\033[0m')
        else:
            return float(p)