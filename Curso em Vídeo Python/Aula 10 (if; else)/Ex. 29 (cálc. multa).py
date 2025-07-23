print('-=-' * 12)
print('LEITOR DE MULTA POR ALTA VELOCIDADE')
print('-=-' * 12)

vel = float(input('\nQual a velocidade do carro (km/h)? '))
limite = int(input('Qual era o limite de velocidade (km/h)? '))
multa = float(input('Qual o valor da multa por km excedido (R$)? '))

if vel <= limite:
    print('\nTudo certo, o carro estava dentro do limite :)')
    print('\033[36mQue ótimo cidadão você é')
else:
    print(f'\n\033[1;31mPÉÉÉHH\033[0m, você excedeu o limite de {limite}km/h, portanto deve pagar uma multa de R${(vel-limite)*multa:.2f}')
    print('Comprou a carteira, é?')