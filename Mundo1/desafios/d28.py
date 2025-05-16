print('===== JOGO DA ADIVINHAÇÃO =====')
import random
numero = random.randint(0, 5) # sorteia um número entre 0 e 5
print('==========================================================')
print('Tente adivinhar o número que estou pensando entre 0 e 5')
print('==========================================================')
palpite = int(input('Qual seu palpite? '))
if palpite == numero:
    print('Parabéns! Você acertou!')
    print(f'O número era {numero}')
else:
    print('Você errou!')
    print(f'O número era {numero}')
print('==========================================================')


