print('===== IMC =====')
peso = float(input('Qual o seu peso? (kg): '))
altura = float(input('Qual a sua altura? (m): '))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO do peso ideal!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')    