resp1 = input('Você sabe programar em python? (\033[32ms/\033[31mn\033[0m): ')

if resp1 == 's':
    print('\nParabéns então né')
else:
    print('\nQue incrível, eu também não :O')

resp2 = int(input('\nQuantos anos você tem? '))

#aqui tem uma condição simplificada, porém é difícil de entender o que ta acontecendo

print('\nBem xofen' if resp2 <=18 else '\nNossa que idoso')