def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')

    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('-' * 30)
        print('PESSOAS CADASTRADAS'.center(30))
        print('-' * 30)
        for linha in a:
            dado = linha.split('-')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<22}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}-{idade}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()