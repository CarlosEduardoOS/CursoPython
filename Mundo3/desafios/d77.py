palavras = ('carro', 'python', 'mouse', 'programa', 'desenvolvedor', 'banana')

vogais = 'aeiou'

for palavra in palavras:
    print(f'\nNa palavra "{palavra}" temos as vogais:', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
