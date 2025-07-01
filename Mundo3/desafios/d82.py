#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    
    resp = input('Quer continuar? [S/N] ').strip().lower()
    if resp == 'n':
        break

for num in numeros: #aqui ele percorre cada numero do array numeros e analisa c é par ou impar
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('-=' * 30)
print(f'Lista completa: {numeros}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')
