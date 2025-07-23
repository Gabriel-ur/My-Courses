print('Bem vindo ao conversor de medidas!\n'
      'Digite um número em metros e te direi seu valor em centímetros e milímetros!\n')

n = float(input('Seu número de escolha: '))

#o :.0f serve para restringir o número de casas decimais
#:.0f restringe a 0 casas decimais, :.1f restringe a 1, etc

print(f'\nA medida de {n:.0f}m corresponde à:\n\n {n*100:.0f}cm \n{n*1000:.0f}mm')