#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('===== AUMENTO SALARIAL =====')
salario = float(input('Qual é o salário do funcionário? R$'))
if salario >= 1250:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f'O funcionário terá um aumento de R${aumento:.2f} e seu novo salário será R${novo_salario:.2f}.')
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f'O funcionário terá um aumento de R${aumento:.2f} e seu novo salário será R${novo_salario:.2f}.')
print('=========================================')
     