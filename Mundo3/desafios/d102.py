#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

#Funções
def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.
    
    :param numero: Número a ser calculado o fatorial.
    :param show: Se True, mostra o processo de cálculo.
    :return: Fatorial do número.
    """
    f = 1
    for i in range(1, numero + 1):
        f *= i
        if show:
            if i == 1:
                print(f'{i}', end=' ')
            else:
                print(f'x {i}', end=' ')
    if show:
        print('=', end=' ')
    return f
#Programa principal
print(fatorial(5, show=True))