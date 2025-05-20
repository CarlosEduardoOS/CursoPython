print('===== Progressão Aritmética Pt3 =====')
numero = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
contador = int(input('Quantos termos você quer mostrar? [0] para parar: '))
if contador == 0:
    print('FIM')
    exit()
while contador > 0:
    print(f'{numero} -> ', end='')
    numero += razao
    contador -= 1
print('FIM')