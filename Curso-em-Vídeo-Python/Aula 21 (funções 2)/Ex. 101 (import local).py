def voto(n):
    """
    Informa a idade do usuário e se deve ou não votar:
        n: ano de nascimento de usuário
        se idade igual 16 ou 17 ou idade maior/igual 70: informa OPCIONAL
        se idade maior/igual 18: informa OBRIGATÓRIO
        se idade menor que 16: informa NÃO É OBRIGATÓRIO
    """
    from datetime import date #importar o módulo dentro do def economiza memória

    idade = date.today().year - n

    if 16 <= idade < 18 or idade >= 70:
        print(f'Com \033[34m{idade}\033[0m anos, o voto é \033[34mOPCIONAL.\033[0m')
    elif idade >= 18:
        print(f'Com \033[31m{idade}\033[0m anos, o voto é \033[31mOBRIGATÓRIO.\033[0m')
    elif idade < 16:
        print(f'Com \033[32m{idade}\033[0m anos, o voto \033[32mNÃO É OBRIGATÓRIO.\033[0m')


nascimento = int(input('Digite seu ano de nascimento: '))

voto(nascimento)

help(voto)