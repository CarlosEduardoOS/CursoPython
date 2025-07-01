#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

print('========== Desafio 94 ==========')
pessoas = []
while True:
    pessoa = dict()
    pessoa['Nome'] = input('Nome: ')
    while True:
        pessoa['Sexo'] = input('Sexo (M/F): ').strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    pessoas.append(pessoa)
    
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo, temos {len(pessoas)} pessoas cadastradas.')
if len(pessoas) > 0:
    media_idade = sum([p['Idade'] for p in pessoas]) / len(pessoas)
    print(f'B) A média de idade é de {media_idade:.2f} anos.')
    print(f'C) A lista de mulheres é: {[p["Nome"] for p in pessoas if p["Sexo"] == "F"]}')
    print(f'D) A lista de pessoas com idade acima da média é: {[p["Nome"] for p in pessoas if p["Idade"] > media_idade]}')
else:
    print('Nenhuma pessoa foi cadastrada.')