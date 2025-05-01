v = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(v)}')
print(f'É um número? {v.isnumeric()}')
print(f'É alfabético? {v.isalpha()}')
print(f'É alfanumérico? {v.isalnum()}')
print(f'É maiúsculo? {v.isupper()}')
print(f'É minúsculo? {v.islower()}')
print('--------------------------')
if v.isnumeric():
    resposta = input('O valor que você digitou é um número, porém é do tipo String. Deseja convertê-lo para inteiro? [S/N] ').strip().upper()
    if resposta == 'S':
        v = int(v)
        print(f'O número convertido é {v} e seu tipo agora é {type(v)}')
        print(v)
        print('--------------------------')
    elif resposta == 'N':
        print('O número não foi convertido.')
        print('--------------------------')
    else:
        print('Opção inválida. Valor não convertido.')
        print('--------------------------')

print(f'O tipo primitivo desse valor é {type(v)}')    

                                                                     