#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('========== Desafio 88 ==========')

print('-=' * 15)
print('     JOGA NA MEGA SENA     ')
print('-=' * 15)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
contador = 1
for i in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    print(f'Jogo {contador}: {jogo}')
    contador += 1
    sleep(1)
