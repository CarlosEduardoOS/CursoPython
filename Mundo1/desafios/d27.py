#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('=========================================')
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split() 
#OBS Em Python, os índices negativos contam de trás para frente, então:
# n[0] é o primeiro nome
# n[-1] é o último nome
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')