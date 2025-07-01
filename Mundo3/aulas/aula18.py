galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('='*30)
pessoas = list()
dado = list()
for c in range(0,3): #guarda isso aqui, talvez use em algum exercicio ai vc so copia e cola
    dado.append(str(input('Nome:')))
    dado.append(str(input('Idade:')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)