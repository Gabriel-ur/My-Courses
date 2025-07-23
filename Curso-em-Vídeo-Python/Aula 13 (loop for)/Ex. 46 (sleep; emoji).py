#o módulo time é semelhante ao datetime, mas ele possui mais funções relacionadas à tempo em si, não necessariamente horários
#o módulo emoji é um módulo externo python que só serve pra fazer graça

from time import sleep
import emoji

print('-=-' * 4)
print('VAI EXPLODIR')
print('-=-' * 4)

print('\nOs fogos vão explodir em...\n')
sleep(1)

for c in range(10, 0-1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[1mCABUM :fireworks:\033[0m'))