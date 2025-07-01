#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
print('===== Desafio 78 =====')
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um número:')))
print(f'O Maior valor é {max(valores)}')
print(f'O Menor valor é {min(valores)}')