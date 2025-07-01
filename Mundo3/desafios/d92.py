#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

print('========== Desafio 92 ==========')
pessoa = dict()
pessoa['Nome'] = input('Nome: ')
pessoa['Nascimento'] = int(input('Ano de Nascimento: '))
pessoa['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['Ctps'] != 0:
    pessoa['Contratacao'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Salário: R$'))
print('-=' * 30)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
