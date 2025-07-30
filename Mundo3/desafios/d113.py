#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except ValueError:
            print('ERRO! Digite um número real válido.')

#Programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número inteiro {n}.')
f = leiaFloat('Digite um número real: ')
print(f'Você digitou o número real {f}.')