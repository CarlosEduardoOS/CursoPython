#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
print('=========================================')
num = int(input('Digite um número de 0 a 9999: '))
n = str(num)
print(f'Analisando o número {num}...')
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
print('=========================================')

