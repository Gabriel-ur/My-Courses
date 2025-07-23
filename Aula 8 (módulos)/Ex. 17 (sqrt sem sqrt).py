cat_a = float(input('Digute o valor do cateto adjacente: '))
cat_o = float(input('Digite o valor do cateto oposto: '))

#pra fazer raiz quadrada sem importar função, é só elevar algo à 1/2 (meio)

hip = (cat_a**2 + cat_o**2) **(1/2)

print(f'Em um triângulo retângulo cujo cateto adjacente mede {cat_a} e o cateto oposto mede {cat_o}, sua hipotenusa será {hip:.2f}')

#é possível calcular a hipotenusa pela biblioteca math com "hypot", aí ficaria hip = hypot(cat_a, cat_o)