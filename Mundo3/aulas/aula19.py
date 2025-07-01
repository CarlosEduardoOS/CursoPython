estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())  #o copy é pra evitar que o dicionario estado seja sobrescrito  na hora que faze o append aqui na linha
  
for e in brasil:
    print(f"Unidade Federativa: {e['uf']}, Sigla: {e['sigla']}")