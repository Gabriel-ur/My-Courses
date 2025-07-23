frase1 = 'Curso em Vídeo Python'

#len é uma função que mostra a quantidade de itens de algo (começa no 0). Pode ser a quantidade de itens de uma string, lista, dicionário, etc
print(len(frase1))

#aqui ele printa apenas os itens de 1 a 20 (começa no 0) pulando de 3 em 3
print(frase1[1:20:3])

#count retorna a quantidade de ocorrências de uma string
print(frase1.count('e'))

#find retorna a menor posição de uma string 
print(frase1.find('Vídeo'))

print('Curso' in frase1)
print(frase1.upper())
print(frase1.lower())
print(frase1.capitalize())
print(frase1.title())
print(frase1.upper().count('O'))

print()

frase2 = '  Aula Nove  '

#strip tira os espaços do início e final de uma string. Muito importante para evitar erros de usuário quando receber um input
print(frase2.strip())

#tira apenas os espaços da direita ('r' -> 'right' -> 'direita')
print(frase2.rstrip())

#tira apenas os espaços da esquerda ('l' -> 'left' -> 'esquerda')
print(frase2.lstrip())

#substitui um termo por outro. Por padrão, troca todas as ocorrências. Se quiser especificar quantas ocorrências deseja trocar da esquerda para direita, coloca vírgula e o número de trocas
print(frase2.replace('Nove', 'Show'))

#split quebra a cadeia de caracteres e forma uma lista, com cada elemento sendo os caracteres divididos por espaço
print(frase2.split())

frase3 = frase2.split() 


#'...'.join junta a cadeia de caracteres, sendo o elemento entre aspas o que vai aparecer nas junções (se quiser juntar com espaço, só colocar um espaço em branco nas aspas)
print('-'.join(frase3))

#aqui os colchetes servem pra indicar quais itens deseja mostrar
print(frase3[0]) #mostra o 1° item da lista
print(frase3[0][3]) #mostra o 3° item do 1° item da lista