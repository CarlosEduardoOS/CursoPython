print('===== Desafio 55 =====')
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:  # Primeira pessoa define os valores iniciais
        maior = peso
        menor = peso
    if peso >= maior:
        maior = peso
    if menor >= peso:
        menor = peso
print(f'O maior peso lido foi de {maior}kg.')
print(f'O menor peso lido foi de {menor}kg.')



