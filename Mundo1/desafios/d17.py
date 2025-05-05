import math
print('===== CALCULADORA DE HIPOTENUSA =====')
catOposto = float(input('Digite o valor do cateto oposto: '))
catAdjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(catOposto, catAdjacente)
print(f'A hipotenusa é: {hipotenusa:.2f}') #hypot é uma função que calcula a hipotenusa de um triângulo retângulo dado os catetos.