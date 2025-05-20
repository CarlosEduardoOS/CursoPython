print('===== Números primos =====')
n = int(input('Digite um número: '))
total = 0 # o total vai armazenar quantos divisores o número n tem.
for c in range(1, n + 1):
    if n % c == 0: # verifica se o número n é divisível por c. Se for, significa que c é um divisor de n.
        print(f'\033[33m{c}\033[m', end=' ')#aqui é aquele sistema de cor que a gente aprender na aula 11 pra pintar o numero do contador atual.
        total += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {n} foi divisível {total} vezes.')
if total == 2: 
    print('E por isso ele é \033[32mPRIMO\033[m!')
else:
    print('E por isso ele \033[31mnão é PRIMO\033[m!')
