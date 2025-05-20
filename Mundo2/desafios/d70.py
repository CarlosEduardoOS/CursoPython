print('===== CAIXA REGISTRADORA =====')
total = mais1000 = barato = 0 # isso aqui é tudo contador
nomeBarato = ''
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    total += preco

    if preco > 1000:
        mais1000 += 1
    if barato == 0 or preco < barato:
        barato = preco
        nomeBarato = produto
    
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Resposta inválida. Quer continuar? [S/N]: ').strip().upper()
    
    if continuar == 'N':
        break
print('\n=== RESULTADOS ===')
print(f'A) Total gasto: R$ {total:.2f}')
print(f'B) Total de produtos acima de R$ 1.000,00: {mais1000}')
print(f'C) Nome do produto mais barato: {nomeBarato} (R$ {barato:.2f})')
print('FIM')    