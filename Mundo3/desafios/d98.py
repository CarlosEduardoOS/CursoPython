#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1  b) de 10 até 0, de 2 em 2  c) uma contagem personalizada
from time import sleep
def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1
    if inicio < fim and passo < 0:
        passo = abs(passo)   #
    elif inicio > fim and passo > 0:
        passo = -passo       
    #Esse bando de if e elif vai analisar automaticamente se é crescente ou decrescente, mas é mais pra contagem personalizada, já que as outras duas contagens são fixas.

    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True) # o flush=True força a impressão imediata, impedindo o buffer de saída
        sleep(0.1)
    print('\n')
    print('=' * 30)

#Programa principal
print('Contagem de 1 até 10, de 1 em 1:')
contador(1, 11, 1)
print('Contagem de 10 até 0, de 2 em 2:')
contador(10, -1, -2)
print('Contagem personalizada:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
