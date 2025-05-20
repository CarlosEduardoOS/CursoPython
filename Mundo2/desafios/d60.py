import math 
n = int(input('Digite um número para calcular o fatorial: '))
f = math.factorial(n)
contador = n-1
print('--------------------')
print(f'!{n} = 5 ', end='')
while contador > 0:
    contador -= 1
    print(f'x {contador + 1}', end=' ')
print(f'= {f}.')
print('--------------------')
#dava pra fazer com for, mas o guanabara quis que fosse com while entao eu fiz do jeito dele