# Funções
def mensagem():
    msg = input('Digite uma mensagem: ').strip().upper()

    print('-' * 30)
    print(msg)
    print('-' * 30)

def soma(a, b):
    return a + b    

def media(a, b):
    return soma(a, b) / 2

def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# Programa principal

print('Calculadora de média')
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
print(f'A média entre {a} e {b} é: {media(a, b)}')

valores = [1, 2, 3, 4, 5]
dobra(valores)
print(f'Lista dobrada: {valores}')