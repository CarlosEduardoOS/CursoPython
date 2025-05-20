n = s = c = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 999: # assim é melhor do que colocar while n != 999 por que isso evita que o número 999 entre na soma
        break
    c += 1
    s += n
print(f'Você digitou {c} números e a soma deles é {s}.')