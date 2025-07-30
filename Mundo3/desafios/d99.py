#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    maior_num = num[0] 
    for n in num:
        if n > maior_num: 
            maior_num = n 
    return maior_num 
#maior_num recebe a primeira posição da lista, ai vai passando, valor por valor, comparando se o valor atual é maior que o maior_num, se for, ele substitui o maior_num pelo valor atual.

#Programa principal
print('Analisador de Números')
numeros = []  # lista para armazenar os números
while True:
    try:
        num = int(input('Digite um número (ou -1 para sair): '))
        if num == -1:
            break
        numeros.append(num)
    except ValueError:
        print('Por favor, digite um número válido.')

if len(numeros) > 0:
    print(f'O maior número digitado foi: {maior(*numeros)}')
else:
    print('Nenhum número válido foi digitado.')