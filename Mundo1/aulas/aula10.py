nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('Nota inválida')
else:
    if media >= 7:
        print(f'Média: {media} || Aprovado')
    else:
        print(f'Média: {media} || Reprovado')
