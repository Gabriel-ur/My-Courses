print('Nesse programa, me diga as dimensões de uma parede e te responderei quanta tinta será necessária para pintá-la\n')

largura = float(input('Largura da parede (em metros): '))
altura = float(input('Altura da parede (em metros): '))
area = largura*altura
tinta = area/2

print(f'\nA dimensão da sua parede é {largura}x{altura}, com área igual à {area:.2f}m²\nAssim, serão necessários {tinta:.2f}L de tinta')