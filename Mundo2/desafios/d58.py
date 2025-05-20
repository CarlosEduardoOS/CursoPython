print('===== Adivinhação 2 =====')
import random
computador = random.randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. Tente adivinhar...')
jogador = int(input('Qual o seu palpite? '))
tentativas = 1
while jogador != computador: #enquanto o palpite do jogador n for igual ao numero do computador
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
print(f'Você acertou! O número era {computador} e você precisou de {tentativas} tentativas.')
    