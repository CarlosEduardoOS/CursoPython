print('===== Maior ou menor =====')
maior = 0
menor = 0
contador = 0
soma = 0
resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um número: '))
    if maior == 0 and menor == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    contador += 1
    print('=-' * 20)     
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
while resposta not in 'SN':
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print(f'O maior número é {maior} e o menor é {menor}.', end=' ')
print(f'A média de todos os números digitados é {(soma / contador):.2f}.')
