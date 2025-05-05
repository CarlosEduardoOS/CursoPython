print("===== SORTEIO =====")
import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4] # não sabia se o guanabara ia usar lista, ou ia usar um random.rand(aluno1, aluno2, aluno3, aluno4), mas como eu sei usar array eu optei po essa opção
sorteio = random.choice(alunos) # o metodo choice() escolhe um elemento do array aleatoriamente, é bem útil
print(f'O aluno sorteado foi: {sorteio}')