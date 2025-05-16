#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('===== Aprovando Empréstimo =====')
valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valorCasa / (anos * 12) #valor da casa dividido pelo número de meses
print(f'Para pagar uma casa de R${valorCasa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}')
if prestacao <= (salario * 30) / 100: # se a prestação for menor ou igual a 30% do salário
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')

