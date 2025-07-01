#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
print('===== Desafio 78 =====')
valores = []
print('[Valor negativo para parar a execução]')
print('[Valores repetidos não serão adicionados]')
while True:
    n = int(input('Digite um valor:'))
    if n < 0:
        break
    if n not in valores:
        valores.append(n)
    
valores.sort()
print(f'Aqui está seu araay ordenado: {valores}')