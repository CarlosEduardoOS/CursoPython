print('===== LOJAS EDUARDO =====')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] À vista no dinheiro/cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1 or opcao == 2:
    if opcao == 1:
        desconto = preco - (preco * 10 / 100) #calcula desconto de 10%
    else:
        desconto = preco - (preco * 5 / 100) #calcula desconto de 5%
    print(f'O valor a ser pago pela sua compra é de R${desconto:.2f}')
elif opcao ==3 or opcao == 4:
    if opcao == 3:
        parcela = preco / 2
        print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
    else:
        total = preco + (preco * 20 / 100)
        parcelas = int(input('Quantas parcelas? '))
        parcela = total / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${parcela:.2f} COM JUROS')
else: 
    print('Opção inválida. Tente novamente!')    