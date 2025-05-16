#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('===== Maior e Menor =====')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
#Esse cofigo funciona assim: primeiro a gen te cria duas variaveis maior e menor, e atribui o valor de n1 a elas. Depois, ele compara n2 e n3 com o valor de maior e menor, se n2 for maior que maior, ele atribui o valor de n2 a maior, se n3 for maior que maior, ele atribui o valor de n3 a maior. E assim por diante para menor. Tem a função max e min, mas não quero deixar complexo, então vou fazer na mão mesmo.    
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')    
