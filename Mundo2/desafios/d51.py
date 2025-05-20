print('===== Progressão Aritmética =====')
n1 = int(input('Digite o primeiro termo: ')) 
r = int(input('Digite a razão: '))
termos = 10
print(f'Os {termos} primeiros termos da PA são:')
for c in range(0, termos):
    print(n1 + c * r, end=' -> ')
print('FIM')