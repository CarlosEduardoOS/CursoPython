def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')

def linha(tam=42):
    print('-' * tam)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    opcao = leiaInt('\033[32mSua Opção: \033[m')
    return opcao
