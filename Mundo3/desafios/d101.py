#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

#Funções
def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    
    if idade < 16:
        return idade, 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return idade, 'OPCIONAL'
    else:
        return idade, 'OBRIGATÓRIO'
#Programa principal
print('==' * 20)
ano_nascimento = int(input('Em que ano você nasceu?: '))
idade, situacao = voto(ano_nascimento)
print(f'Com {idade} anos, seu voto é {situacao}.')