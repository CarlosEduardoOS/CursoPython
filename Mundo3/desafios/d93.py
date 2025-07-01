#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
jogador['Nome'] = input('Nome do Jogador: ')
jogador['Partidas'] = int(input('Quantas partidas jogou? '))
gols = []
for i in range(jogador['Partidas']):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['Gols'] = gols
jogador['Total de Gols'] = sum(gols)
print('-=' * 30)
for k, v in jogador.items():
    print(f'- {k} tem o valor {v}')
