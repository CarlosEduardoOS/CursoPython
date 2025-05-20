n = s = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 999: # assim é melhor do que colocar while n != 999 por que isso evita que o número 999 entre na soma
        break
    s += n
print(f'A soma dos números é {s}.')

