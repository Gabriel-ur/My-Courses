#math é um módulo interno do python que dá acesso à várias funções relacionadas a contas matemáticas

from math import sin, cos, tan, radians

print('Bem vindo à calculadora de seno, cosseno e tangente! Digite um ângulo que te direi seu sen, cos e tg\n')

angulo = radians(float(input('Digite o ângulo de escolha: ')))

print(f'\nO seno, cosseno e a tangente - respectivamente - de {angulo:.2f} é {(sin(angulo)):.2f}, {(cos(angulo)):.2f} e {(tan(angulo)):.2f}')