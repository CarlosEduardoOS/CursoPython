print('===== PINTOR DE PAREDES =====')
largura = float(input('Qual a largura da parede? (m) '))
altura = float(input('Qual a altura da parede? (m) '))
area = largura * altura
litros = area / 2 # Cada litro de tinta pinta 2m quadrados
print(f'A área da parede é de {area:.2f}m² e você precisará de {litros:.2f}l de tinta para pintá-la.')
print('==================================')