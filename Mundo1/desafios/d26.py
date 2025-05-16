#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
print('=========================================')
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes')
print(f'A primeira letra A aparece na posição {frase.find("A") + 1}') # esse +1 é para não aparecer 0, pois a contagem começa do 0
print(f'A última letra A aparece na posição {frase.rfind("A") + 1}') # o rfind procura a letra A da direita para a esquerda.
print('=========================================')