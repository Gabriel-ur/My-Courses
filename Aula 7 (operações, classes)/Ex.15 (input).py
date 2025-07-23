print('Neste programa, me diga os dias e os km rodados por um carro alugado, assim como os custos relacionados, que te direi o quanto deverá ser pago\n')

v_dia = float(input('Valor a ser pago por dia: '))
v_km = float(input('Valor a ser pago por km rodado: '))
q_dia = int(input('Quantidade de dias que o carro ficou alugado: '))
q_km = float(input('Quantidade de km rodados: '))

print(f'O custo final será de R${v_dia*q_dia+v_km*q_km} (R${v_dia*q_dia} pelos dias e R${v_km*q_km} pelos kms rodados)')