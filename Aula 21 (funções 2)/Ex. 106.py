from time import sleep

def interactiveHelp():
    while True:
        txt = '  Sistema de ajuda PyHelp'
        print('~' * (len(txt) + 2))
        print(f'\033[32m{txt}\033[0m')
        print('~' * (len(txt) + 2))

        h = input('Função ou biblioteca (fim para)> ').strip().lower()
        sleep(0.5)

        txt = f'  Acessando manual do {h}'
        print('~' * (len(txt) + 2))
        print(f'\033[34m{txt}\033[0m')
        print('~' * (len(txt) + 2))
        sleep(0.5)

        print(help(h))
        sleep(1)

        if h == 'fim':
            txt = '  FIM'
            print('~' * (len(txt) + 2))
            print(f'\033[31m{txt}\033[0m')
            print('~' * (len(txt) + 2))
            break


interactiveHelp()