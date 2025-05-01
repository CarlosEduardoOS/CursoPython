print('===== REAJUSTE SALARIAL =====')
salario = float(input('Qual o salário do funcionário? R$'))
print('O funcionário receberá um aumento de 15%')
aumento = 15
salario_final = salario + (salario * aumento / 100)
print(f'O salário final com {aumento}% de aumento é R${salario_final:.2f}')
print('==================================')