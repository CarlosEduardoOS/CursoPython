#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
print('=========================================')
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome tem SILVA? {"SILVA" in nome.upper()}') # o in procura na string toda se existe o conjunto de caracteres informado, no caso SILVA, e retorna True ou False
print('=========================================')