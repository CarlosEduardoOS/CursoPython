#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
print('========== Desafio 95 ==========')

time = list()

while True:
    jogador = dict()
    jogador['Nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols = []
    for i in range(partidas):
        gols.append(int(input(f'   Quantos gols na partida {i+1}? ')))
    jogador['Gols'] = gols[:]
    jogador['Total de Gols'] = sum(gols)
    time.append(jogador.copy())

    resp = input('Deseja continuar? [S/N] ').strip().upper()
    if resp != 'S':
        break

print('=-' * 30)
print(f'{"cod":<4}{"Nome":<15}{"Gols":<20}{"Total":<5}')
print('=-' * 30)
for i, j in enumerate(time):
    print(f'{i:<4}{j["Nome"]:<15}{str(j["Gols"]):<20}{j["Total de Gols"]:<5}')
print('=-' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('=-' * 30)
print('<<< VOLTE SEMPRE! >>>')