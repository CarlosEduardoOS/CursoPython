import random
#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
print('===== EMBARALHAR LISTA =====')
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos) # o metodo shuffle() embaralha a lista, ou seja, ele muda a ordem dos elementos da lista
print('A ordem de apresentação será:')
print(alunos) # aqui eles ja estão embaralhados