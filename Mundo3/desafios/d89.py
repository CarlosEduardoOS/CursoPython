#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print('========== Desafio 89 ==========')
boletim = []
while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    if input('Deseja continuar? [S/N] ').strip().upper() != 'S':
        break
print('=-' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}') # n sabia como fazer o alinhamento mas o chat falo q dava pra fazer assim e eu achei interessante
print('=-' * 30)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')#esse .1f é pra mostrar uma casa decimal só
print('=-' * 30)
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para sair) '))
    if opcao == 999:
        break
    if 0 <= opcao < len(boletim):
        print(f'Notas de {boletim[opcao][0]}: {boletim[opcao][1]}')
    else:
        print('Aluno não encontrado.')