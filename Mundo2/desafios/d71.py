print('===== CAIXA ELETRÔNICA =====')
print('Seja bem-vindo(a)!')
print('Por favor, insira o valor que deseja sacar:')
valor = int(input('R$'))
total = valor
ced50 = ced20 = ced10 = ced5 = ced1 = 0 #contadores de quantas cedulas vai usou
while True:
    if total >= 50: # enquanto o total foi maior que 50 ele vai continuar tirando 50 do total e adicionando 1 ao contador de 50
        ced50 += 1
        total -= 50
    elif total >= 20: #mesma coisa do que em cima, e vai assim ate o final onde zera o total
        ced20 += 1
        total -= 20
    elif total >= 10:
        ced10 += 1
        total -= 10
    elif total >= 5:
        ced5 += 1
        total -= 5
    elif total >= 1:
        ced1 += 1
        total -= 1
    else: #ele so vem pra esse else quando o total for 0
        break
print('===== RETIRADA =====')
if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$50,00')
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$20,00')
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$10,00')
if ced5 > 0:
    print(f'Total de {ced5} cédulas de R$5,00')
if ced1 > 0:
    print(f'Total de {ced1} cédulas de R$1,00')
print('Obrigado por utilizar nosso caixa eletrônico!')
