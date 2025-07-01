#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
#mt mais facil usar o sort duq isso aqui


lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos +=1
print('-='*30)
print(f'Os valores digitadores em ordem foram {lista}')