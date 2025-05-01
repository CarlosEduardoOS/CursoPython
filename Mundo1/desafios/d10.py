print('===== CONVERSOR DE MOEDAS =====')
real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real / 5.68
euros = real / 6.45
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f} e €{euros:.2f}')
print('==================================') 
