print('Analisarei se a cidade em que mora começa com "Santo"\n')
nome = input('Digite o nome da sua cidade: ').lower().strip()
nome2 = nome.split()
#o split serve pra ver se "santo" está especificamente no começo e não depois

print('santo' in nome2[0])