#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('===== Conversor de Bases =====')
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}') #a funçaõ bin() retorna o número em binário
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}') #a funçaõ oct() retorna o número em octal
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')#a funçaõ hex() retorna o número em hexadecimal
else:
    print('Opção inválida. Tente novamente!')