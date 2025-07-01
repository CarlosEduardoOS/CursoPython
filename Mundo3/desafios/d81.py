#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []
print('[Digite 00 para sair]')
while True:
    entrada = input('Digite um valor: ')
    if entrada == '00':
        break
    n = int(entrada)
    valores.append(n)
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'Em ordem descresente: {valores}')
if 5 in valores:
    print('O número 5 foi digitado!!!')
else:
    print('O número 5 não foi digitado ;-;')
