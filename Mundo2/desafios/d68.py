import random

vit = 0
print('===== Par ou Ímpar =====')

while True:
    computador = random.randint(1, 5)
    n = int(input('Digite um número de 1 a 5: '))
    while n < 1 or n > 5: # Verifica se o número está entre 1 e 5
        n = int(input('Número inválido. Digite de 1 a 5: '))
        
    jogo = input('Par ou Ímpar? [P/I]: ').strip().upper()
    while jogo not in ('P', 'I'): # Verifica se a opção é válida
        jogo = input('Par ou Ímpar? [P/I]: ').strip().upper()
        
    total = n + computador
    resultado = 'PAR' if total % 2 == 0 else 'ÍMPAR'
    
    print(f'Você jogou {n} e o computador {computador}. Total de {total} = {resultado}')
    
    if (jogo == 'P' and total % 2 == 0) or (jogo == 'I' and total % 2 == 1):
        print('Você VENCEU!\n')
        vit += 1
    else:
        print('Você PERDEU!\n')
        break

print(f'Você venceu {vit} vez(es).')
print('FIM DO JOGO')


