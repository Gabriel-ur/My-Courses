def dobro(m, f=False):
    """
    Retorna o dobro de um valor
        m: valor a ser dobrado
        f: formata para estilo moeda (R$xx,xx)
    """
    if f==False:
        return m * 2
    else:
        return moeda(m * 2)


def metade(m, f=False):
    """
    Retorna a metade de um valor
        m: valor a ser dividido pel metade
        f: formata para estilo moeda (R$xx,xx)
    """
    if f==False:
        return m / 2
    else:
        return moeda(m / 2)


def aumento(m, p, f=False):
    """
    Retorna o aumento percentual de um valor
        m: valor a sofrer aumento
        a: (int ou float), porcentagem do aumento de m
        f: formata para estilo moeda (R$xx,xx)
    """
    if f==False:
        return m + (m * (p / 100))
    else:
        return moeda(m + (m * (p / 100)))


def reduz(m, p, f=False):
    """
    Retorna a diminuição percentual de um valor
        m: valor a sofrer redução
        a: (int ou float), porcentagem de redução de m
        f: formata para estilo moeda (R$xx,xx)
    """
    if f==False:
        return m - (m * (p / 100))
    else:
        return moeda(m - (m * (p / 100)))


def moeda(m):
    """
    Retorna o valor m formtado em padrão moeda (R$xx,xx)
        m: valor a ser formatado
    """
    return f'R${m:.2f}'.replace('.', ',')


def resumo(m, a, r):
    """
    Retorna uma tabela com o dobro e metade de m, assim como o aumento percentual a de m e a redução percentural r de m
        m: valor digitado pelo usuário
        a: porcentagem de aumento
        r: porcentagem de redução
    """
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'{"Preço analisado:"} \t\033[36m{moeda(m)}\033[0m')
    print(f'{"Dobro do preço:"} \t\033[34m{dobro(m, True)}\033[0m')
    print(f'{"A metade do preço:"} \t\033[35m{metade(m, True)}\033[0m')
    print(f'{a}%{" de aumento:"} \t\033[31m{aumento(m, a, True)}\033[0m')
    print(f'{r}%{" de redução:"} \t\033[32m{reduz(m, r, True)}\033[0m')
    print('-' * 35)