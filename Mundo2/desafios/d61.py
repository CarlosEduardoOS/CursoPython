print('===== Progressão Aritmética Pt2 =====')
numero = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
contador = 10
while contador > 0:
    print(f'{numero} -> ', end='')
    numero += razao
    contador -= 1
print('FIM')
#No desafio 51 a gente fez um gerador de PA tambem, porem usando o For, aqui é mais pra mostrar que no python é possivel fazer a mesma coisa de jeitos diferentes.