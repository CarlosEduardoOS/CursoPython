#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)

def notas(*n, sit=False): #n aqui é um array q recebe todas as notas que o usuário passar
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n) #fiquei com preguiça de faze na mao ent eu usei essas funçoes nativas do python
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Aprovado'
        elif r['média'] >= 5:
            r['situação'] = 'Recuperação'
        else:
            r['situação'] = 'Reprovado'
    return r

#Programa principal
resp = notas(5.5, 6.0, 7.0, 8.0, sit=True) #aqui eu chamei a função notas e passei as notas que eu queria, e o sit=True para mostrar a situação
print(f'{"-" * 20} Notas {"-" * 20}')
for k, v in resp.items(): #isso aqui é mais deixa bonitinho a gente viu isso na aula de manipulação de dicionários, k é key que é a tagzinha e v é value que é o valor dela
    print(f'{k}: {v}') 