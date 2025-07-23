print('Analisarei se seu nome possui "Silva"\n')
nome = input('Digite seu nome completo: ').lower().strip().split()
#aqui o split impede que "silvana" tambem retorne True

print('silva' in nome)