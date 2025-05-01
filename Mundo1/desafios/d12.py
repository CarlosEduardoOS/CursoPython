print('===== APLICADOR DE DESCONTO =====')
preco = float(input('Qual o preço do produto? R$'))
resposta = input('Deseja aplicar o cupom de 5%? (S/N) ').strip().upper()
if resposta == 'S':
    desconto = 5
    preco_final = preco - (preco * desconto / 100)
    print(f'O preço final com {desconto}% de desconto é R${preco_final:.2f}')
elif resposta == 'N':
    print(f'O preço final é R${preco:.2f}')
else:
    print(f'Opção inválida. O preço final é R${preco:.2f}')    