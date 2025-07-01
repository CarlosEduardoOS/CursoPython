#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
print('========== Desafio 90 ==========')
aluno = dict()
aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input('Média do aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(aluno)
print('-=' * 30)
for k, v in aluno.items():
    print(f'     - {k} é igual a {v}')