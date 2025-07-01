print('===== Brasileirao =====')

times = (
    "Palmeiras", "Flamengo", "Cruzeiro", "Red Bull Bragantino", "Ceará",
    "Bahia", "Fluminense", "Corinthians", "Atlético-MG", "Botafogo",
    "São Paulo", "Mirassol", "Vasco da Gama", "Fortaleza", "Internacional",
    "Vitória", "Grêmio", "Juventude", "Santos", "Sport"
)
print("a) Os 5 primeiros colocados são:")
print(times[:5])

print("\nb) Os 4 últimos colocados são:")
print(times[-4:])

# c) Times em ordem alfabética
print("\nc) Times em ordem alfabética:")
print(sorted(times)) # o sorted() deixa em ordem alfabetica

# d) Posição da Chapecoense
print("\nd) Posição do Palmeiras:")
print(f"O Palmeiras está na {times.index('Palmeiras') + 1}ª posição.")
