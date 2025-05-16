#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('===== RADAR ELETRÔNICO =====')
velocidade = int(input('Qual é a velocidade atual do carro? (km/h): '))
if velocidade <= 0:
    print('O carro está parado.')
elif velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido de 80Km/h.')
    multa = (velocidade - 80) * 7 # aqui ele pega e subtai o limite, pq é 7 reais por cada km ultraopassado por isso ele pega so a diferença
    print(f'O valor da multa é R${multa:.2f}.')
else:
    print('Você está dentro do limite de velocidade permitido.')
print('Tenha um bom dia. Dirija com segurança!')
print('=========================================')
