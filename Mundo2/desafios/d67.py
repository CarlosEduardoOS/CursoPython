while True:
    n = int(input('Digite um número (negativo para sair): '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
print('FIM')
