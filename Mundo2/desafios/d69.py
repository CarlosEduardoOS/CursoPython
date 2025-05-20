mais18 = 0
homens = 0
mulheres_menos20 = 0

while True:
    print('--- Cadastro de Pessoa ---')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        sexo = input('Sexo inválido. Digite [M/F]: ').strip().upper()
    
    if idade > 18:
        mais18 += 1
    
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos20 += 1
    
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Resposta inválida. Quer continuar? [S/N]: ').strip().upper()
    
    if continuar == 'N':
        break

print('\n=== RESULTADOS ===')
print(f'A) Total de pessoas com mais de 18 anos: {mais18}')
print(f'B) Total de homens cadastrados: {homens}')
print(f'C) Total de mulheres com menos de 20 anos: {mulheres_menos20}')
