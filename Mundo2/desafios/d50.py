print('===== Soma dos pares =====')
soma = 0
for c in range(1, 7): # 1 a 6
    num = int(input('Digite um número: '))
    if num % 2 == 0: # se o numero for par ele adiciona no somador
        soma += num
print(f'A soma dos números pares é {soma}')        