aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print(f'A média de {aluno} é {media:.1f}')
if media >=7:
    print(f'{aluno} foi aprovado!')
else:
    print(f'{aluno} foi reprovado!')
