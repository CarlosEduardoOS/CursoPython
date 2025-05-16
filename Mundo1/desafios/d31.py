#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('===== Desafio 31 =====')
distancia = float(input('Qual a distância da sua viagem em Km? '))
if distancia <= 200:
    preco = distancia * 0.50
    print(f'O preço da passagem é R${preco:.2f}.')
else:
    preco = distancia * 0.45
    print(f'O preço da passagem é R${preco:.2f}.')
print('Tenha uma boa viagem!')
print('=========================================')

