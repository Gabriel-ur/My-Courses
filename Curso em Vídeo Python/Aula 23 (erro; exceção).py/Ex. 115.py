from modulos import cadastro, arquivo

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    u = cadastro.menu(['Ver pessoas cadastradas', 'Adicionar cadastro', 'Sair do programa'])

    if u == 1:
        arquivo.lerArquivo(arq)

    if u == 2:
        print('-' * 30)
        print('NOVO CADASTRO'.center(30))
        print('-' * 30)

        nome = input('Digite o nome: ').title().strip()
        idade = cadastro.leiaInt('Digite a idade: ')
        arquivo.cadastrar(arq, nome, idade)
        print('-' * 30)

    if u == 3:
        print('-' * 30)
        print('Finalizando... Até logo!'.center(30))
        print('-' * 30)
        break