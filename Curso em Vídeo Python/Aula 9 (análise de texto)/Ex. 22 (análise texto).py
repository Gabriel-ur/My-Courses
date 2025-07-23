nome = input('Digite seu nome completo: ').strip()
print('\n\033[45mAnalisando seu nome...\033[m\n')

print(f'Seu nome em capslock é: {nome.upper()}.\n')

print(f'Seu nome em minúsculo é: {nome.lower()}.\n')

print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras.\n')

print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras.')