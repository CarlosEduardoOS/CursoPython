#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#Funções
def area(largura, comprimento):
    return largura * comprimento

#Programa principal
print('Controle de Terrenos')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
print(f'A área do terreno {largura} x {comprimento} é de {area(largura, comprimento)} m²')
print('-' * 30)