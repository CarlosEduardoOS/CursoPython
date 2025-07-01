print('========== Desafio 84 ==========')
#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas.B) Uma listagem com as pessoas mais pesadas.C) Uma listagem com as pessoas mais leves.
dado = list()
pessoas = list()
countCadastradas = 0
maisPesada = maisLeve = []
while True:
    dado.append(str(input('Nome:')))
    dado.append(int(input('Peso:')))
    pessoas.append(dado[:])
    
    if len(pessoas) == 1:
        maisPesada = dado[:]
        maisLeve = dado[:]
    else:
        if dado[1] > maisPesada[1]:
            maisPesada = dado[:]
        if dado[1] < maisLeve[1]:
            maisLeve = dado[:]

    
    countCadastradas += 1
    dado.clear()
    resposta = str(input('Continuar? [S] [N]')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Continuar? [S] [N]')).strip().upper()
    if resposta == 'N':
        break
print('='*50)
print(f'A) Pessoas cadastradas: {countCadastradas}')
print(f'B) Pessoa mais pesada: {maisPesada[0]} com {maisPesada[1]}')
print(f'B) Pessoa mais leve: {maisLeve[0]} com {maisLeve[1]}')
