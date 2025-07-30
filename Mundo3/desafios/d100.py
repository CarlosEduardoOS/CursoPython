#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

def sorteia(numerosParametro):
    from random import randint
    for i in range(5):
        numerosParametro.append(randint(1, 100))  # Sorteia números entre 1 e 100
    return numerosParametro

def somaPar(numerosParametro):
    soma = 0
    print('Os números pares são: {', end=' ')
    for n in numerosParametro:
        if n % 2 == 0:
            soma += n
            print(n, end=' ')
    print('}')
    print('--' * 20)
    return soma

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

#Programa principal
escreva('Sorteio de Números e Soma dos Pares')
numeros=list()
print(f'A lista gerada foi:{sorteia(numeros)}')
print('--' * 20)
print(f'A soma dos números pares é: {somaPar(numeros)}')
print('--' * 20)