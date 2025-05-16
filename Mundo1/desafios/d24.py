#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
print('=========================================')
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(f'Seu nome começa com SANTO? {cidade[:5].upper() == "SANTO"}') # apartir do momento que usamos == ele passa a retornar um booleano, ou seja, True ou False
print('=========================================')