def dobro(m):
    """
    Retorna o dobro de um valor
        m: valor a ser dobrado
    """
    return m * 2


def metade(m):
    """
    Retorna a metade de um valor
        m: valor a ser dividido pel metade
    """
    return m / 2


def aumento(m, p):
    """
    Retorna o aumento percentual de um valor
        m: valor a sofrer aumento
        a: (int ou float), porcentagem do aumento de m
    """
    return m + (m * (p / 100))


def reduz(m, p):
    """
    Retorna a diminuição percentual de um valor
        m: valor a sofrer redução
        a: (int ou float), porcentagem de redução de m
    """
    return m - (m * (p / 100))


def moeda(m):
    """
    Retorna o valor m formtado em padrão moeda (R$xx,xx)
        m: valor a ser formatado
    """
    return f'R${m:.2f}'.replace('.', ',')

