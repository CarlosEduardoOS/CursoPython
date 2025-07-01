num = [4,3,2,6,8,54,32,123,5,7,456,2,1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2,0) #elemento 0 na posição 2
if 5 in num:
    num.remove(5)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
print('=========================================')
for c, v in enumerate(num): #o enumarate cria uma lista tupla onde cada valor fica do ladinho do seu indice, ai ele pega o valor do indice e coloca o c e o valor e coloca no v. Tenta rodar print(list(enumerate(num)))
    print(f'Na posição {c} encontrei o valor {v}')
print('=========================================')
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um número:')))
for c, v in enumerate(valores): 
    print(f'Na posição {c+1} encontrei o valor {v}')
print('=========================================')
a = [2,3,4,7]
b = a #isso aqui conecta os dois arrays, ai tudo uq vc  fizer em um altera o outro
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')
print('=========================================')
a = [2,3,4,7]
b = a[:]#isso aqui copia os valores de a para b sem fazer a conexao igual o exemplo de cima
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')

