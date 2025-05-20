print('===== Sequência de Fibonacci =====')
n = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')

contador = 3  # Começa do 3º termo, pois já mostramos os dois primeiros

while contador <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3 #eles vao recebendo o termo anterior
    contador += 1

print(' -> FIM')

 