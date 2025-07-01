print('========== Desadio 86 ==========')
#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

#Aqui eu falhei, tive que usar o gpt pra fazer
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 20)
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')  # Centraliza o valor dentro de 5 espaços
    print()

# Este programa cria uma matriz 3x3 (3 linhas e 3 colunas), preenchida com valores digitados pelo usuário.
# Utiliza duas estruturas de repetição (for aninhados) para percorrer as posições da matriz e solicitar um número
# para cada coordenada [linha, coluna]. Esses valores são armazenados em uma lista de listas (matriz).
# Após o preenchimento, a matriz é exibida de forma formatada na tela, com cada valor centralizado entre colchetes,
# simulando a aparência tradicional de uma tabela. A quebra de linha após cada linha da matriz garante o formato visual correto.
