#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda
preco = float(input("Digite o preço: R$ "))
print(f"Aumentando 10%, temos R$ {moeda.aumentar(preco, 10):.2f}")
print(f"Diminuindo 10%, temos R$ {moeda.diminuir(preco, 10):.2f}")
print(f"Dobro do preço: R$ {moeda.dobro(preco):.2f}")
print(f"Metade do preço: R$ {moeda.metade(preco):.2f}")