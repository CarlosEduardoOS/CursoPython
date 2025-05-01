print('===== TABUADA =====')
try:
    numero = int(input('Digite um número: '))
    if numero < 0:
        print('Número inválido!')
    else:
        print(f'A tabuada de {numero} é:')
        for i in range(1, 11): # o 11 não é incluído, então vai de 1 a 10
            print(f'{numero} x {i} = {numero * i}')
except ValueError:
    print('Por favor, digite um número inteiro válido!')
print('====================')