print('=====  Validação de Dados =====')
sexo = input('Informe o sexo (M/F): ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dados Invalidos. Informe o sexo (M/F): ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')