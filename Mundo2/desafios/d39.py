print('===== Alistamento Militar =====')
from datetime import date
nascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year #pega a data do pc
idade = anoAtual - nascimento
if idade < 18:
    saldo = 18 - idade
    print(f'Você ainda vai se alistar, faltam {saldo} anos.')
    anoAlistamento = anoAtual + saldo
    print(f'Seu alistamento será em {anoAlistamento}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    anoAlistamento = anoAtual - saldo
    print(f'Seu alistamento foi em {anoAlistamento}.')
else:
    print('Você deve se alistar IMEDIATAMENTE!')
    anoAlistamento = anoAtual
    print(f'Seu alistamento é em {anoAlistamento}.')    