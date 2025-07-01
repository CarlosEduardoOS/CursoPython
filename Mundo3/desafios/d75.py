numeros = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(4))

print(f"\nVocê digitou os números: {numeros}")

print(f"O número 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O número 3 apareceu pela primeira vez na posição {numeros.index(3)+1}.")
else:
    print("O número 3 não foi digitado.")

pares = [n for n in numeros if n % 2 == 0]
print(f"Os números pares digitados foram: {pares}")