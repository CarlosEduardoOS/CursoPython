print('===== SENO COSENO E TANGENTE =====')
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {coseno:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
# math.radians() converte o ângulo de graus para radianos, pois as funções trigonométricas em Python trabalham com radianos.
# ou seja eu so consigo usar .sin, .cos e .tan se o angulo estiver em radianos, por isso eu usei o math.radians(angulo) para converter o angulo de graus para radianos.