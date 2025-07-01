#xercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
print('========== Desafio 85 ==========')
numeros = []
pares = []
impares = []

for c in range(0,7):
    n = int(input(f'Digite o {c+1}° número:'))
    numeros.append(n)

for num in numeros: #aqui ele percorre cada numero do array numeros e analisa c é par ou impar
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('-=' * 30)
pares.sort()
impares.sort()
print(f'Lista completa: {numeros}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')