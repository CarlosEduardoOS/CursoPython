import random

numeros = tuple(random.randint(0, 10) for c in range(5)) #esse tuple é tipo o int() ou float(), é um jeito que eu achei de fazer varios numeros aleatorios, o numwero dentro do range é a quantidade de numeros que ele vai gerar, ent fica a dica
print("Números sorteados:", numeros) 

maior = max(numeros) #o modulo max e o min procura o maior e o menor numero
menor = min(numeros)

print("Maior número:", maior)
print("Menor número:", menor)

