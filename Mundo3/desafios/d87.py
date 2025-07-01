# Este programa cria uma matriz 3x3 preenchida com valores digitados pelo usuário.
# Depois de preencher a matriz, ele exibe:
# A) A soma de todos os valores pares
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

#Não to com cabeça, pedi pro gpt

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna3 = 0
maior_valor_linha2 = 0

# Preenchimento da matriz e cálculo parcial
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valor

        if valor % 2 == 0:
            soma_pares += valor  # Soma dos pares

        if coluna == 2:
            soma_coluna3 += valor  # Soma da terceira coluna

        if linha == 1:
            if coluna == 0:
                maior_valor_linha2 = valor  # Inicializa com o primeiro valor da linha 2
            elif valor > maior_valor_linha2:
                maior_valor_linha2 = valor  # Atualiza se achar valor maior

# Exibição da matriz formatada
print('-=' * 30)
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print()

# Exibindo os resultados
print('-=' * 30)
print(f'A) A soma dos valores pares é {soma_pares}')
print(f'B) A soma dos valores da terceira coluna é {soma_coluna3}')
print(f'C) O maior valor da segunda linha é {maior_valor_linha2}')
