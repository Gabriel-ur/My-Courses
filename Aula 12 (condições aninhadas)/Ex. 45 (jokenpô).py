from random import choice

print('-=-' * 2)
print('JOKENPÔ')
print('-=-' * 2)

player = input('\nSua jogada: ').strip().lower() 
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
print(f'Jogada do pc: {pc}')

if pc == 'pedra':
    if player == 'pedra':
        print('\nEmpatamos')
    elif player == 'papel':
        print('\nDroga, você ganhou :(')
    elif player == 'tesoura':
        print('\nHa, eu ganhei >:)')
    else:
        print('\nJogada inválida')
elif pc == 'papel':
    if player == 'pedra':
        print('\nHa, eu ganhei >:)')
    elif player == 'papel':
        print('\nEmpatamos')
    elif player == 'tesoura':
        print('\nDroga, você ganhou :(')
    else:
        print('\nJogada inválida')
elif pc == 'tesoura':
    if player == 'pedra':
        print('\nDroga, você ganhou :(')
    elif player == 'papel':
        print('\nHa, eu ganhei >:)')
    elif player == 'tesoura':
        print('\nEmpatamos')
    else:
        print('\nJogada inválida')