produtos = ('Caderno', 50.00, 'Lápis', 3.50, 'Borracha', 3.50, 'Caneta', 8.00,
            'Estojo', 10.00, 'Tesoura', 6.00, 'Mochila', 250.00)

print('-=-' * 14)
print('TABELA DE PRODUTOS')
print('-=-' * 14)

for posiçao in range(0,len(produtos),2):
        print(f'{produtos[posiçao]:.<30}', end='')
        print(f'R${produtos[posiçao+1]:.2f}')
