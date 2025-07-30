try:
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    r = a / b
except ValueError:
    print("Você não digitou um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"O resultado da divisão é: {r}")
finally:
    print("Fim do programa.")