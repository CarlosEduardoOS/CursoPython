print('===== Maioridade =====')
from datetime import date
ano_atual = date.today().year
total = 0
for c in range(1, 8):
    anoNascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if ano_atual - anoNascimento >= 18: #se o ano atual menos o ano de nascimento da pessoa for maior ou igual a 18, o total de pessoas maiores aumenta em 1 ponto
        total += 1
print(f'Ao todo tivemos {total} pessoas maiores de idade.')
print(f'E também tivemos {7 - total} pessoas menores de idade.')