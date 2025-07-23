#o import serve pra pegar uma biblioteca pra usar novas funções que não vem como padrão

import math

#esse exemplo de média não funciona tão bem, precisa de limitantes, mas é assim que funciona:

media = float(input('Digite a sua média: '))
arredondamento = math.ceil(media)

print(f'Sua média, após o arredondamento, será {arredondamento}')