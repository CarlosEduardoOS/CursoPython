print('===== Contagem de pares =====')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 % 2 == 0:
    for c in range (n1, n2 + 1, 2):
        print(c)
else:
    for c in range (n1 + 1, n2 + 1, 2):
        print(c)            