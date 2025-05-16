print('===== Média de Provas =====')
n1 = float(input('Primeira Nota:'))
n2 = float(input('Segunda Nota:'))
media = (n1 + n2) / 2
print(f'A sua média é {media:.1f}')
if media < 5:
    print('Você está REPROVADO!')
elif media >= 5 and media < 7:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você está APROVADO!')
