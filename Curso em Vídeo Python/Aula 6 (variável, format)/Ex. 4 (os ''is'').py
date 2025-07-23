algo = input('Digite qualquer coisa: ')

#"type" mostra o tipo primitivo da váriavel
print('O tipo primitivo deste algo é: ', type(algo))
#"isspace" mostra se a variável possui apenas espaços
print('Este algo possui apenas espaços? ', algo.isspace())
#"isnumeric" diz se a variável é um número
print('Este algo é um número? ', algo.isnumeric())
#"isalpha" diz se a variável é alfabética
print('Este algo é alfabético? ', algo.isalpha())
#"isalnum" diz se a variável contêm letras OU núemros
print('Este algo é alfanumérico? ', algo.isalnum())
#"isupper" diz se a variável inteira está em caps lock
print('Este algo está inteiro maiúsculo? ', algo.isupper())
#"islower" diz se a variável inteira é minúscula
print('Este algo está inteiro minúsculo? ', algo.islower())
#"istitle" diz se a variável começa com maiúsucla e dps é minúscula
print('Este algo está capitalizado? ', algo.istitle())