print('===== Soma e Contagem de Números =====')
soma = 0
contador = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break # o break interrompe o loop
    soma += num
    contador += 1

print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
