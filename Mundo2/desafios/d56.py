print('===== ANALISADOR COMPLETO =====')
countIdade = 0
IdadeMaisVelho = 0
nomeMaisVelho = 0
homemEncontrado = False
mulheresSub20 = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print(f'-----------------------')
    countIdade += idade

    if sexo == 'M':
        if homemEncontrado == False:
            IdadeMaisVelho = idade
            nomeMaisVelho = nome
            homemEncontrado = True
        elif idade > IdadeMaisVelho:
            IdadeMaisVelho = idade
            nomeMaisVelho = nome
    elif sexo == 'F'  and idade < 20:
        mulheresSub20 += 1

print('----- Analise dos Dados -----')
print(f'A média de idade do grupo é de {countIdade / 4} anos.')
print(f'O homem mais velho tem {IdadeMaisVelho} anos e se chama {nomeMaisVelho}.')
print(f'Ao todo são {mulheresSub20} mulheres com menos de 20 anos.')
print('-----------------------')
    