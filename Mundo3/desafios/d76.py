produtos = (
    'Lápis', 1.50,
    'Caderno', 15.90,
    'Borracha', 0.99,
    'Caneta', 2.00,
    'Mochila', 120.00,
    'Estojo', 9.50
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')  # Centraliza o título
print('-' * 40)

# Percorre a tupla de 2 em 2 elementos (nome, preço)
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i+1]
    print(f'{nome:.<30} R$ {preco:>7.2f}')  # Alinhamento bonito com pontilhado

print('-' * 40)
