#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def titulo(msg, cor=0):
    cores = [
        '\033[m',          # 0 - sem cor
        '\033[0;30;41m',   # 1 - vermelho
        '\033[0;30;42m',   # 2 - verde
        '\033[0;30;43m',   # 3 - amarelo
        '\033[0;30;44m',   # 4 - azul
        '\033[0;30;45m',   # 5 - roxo
    ]
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print('\033[m', end='')  # reset

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou Biblioteca (ou FIM para sair): ').strip()
    if comando.upper() == 'FIM':
        break
    else:
        titulo(f'Acessando o manual do comando \'{comando}\'', 4)
        print('\033[7m', end='')  # fundo branco, texto preto
        help(comando)
        print('\033[m', end='')   # reset

titulo('ATÉ LOGO!', 1)

#Esse aqui eu fiz no gpt msm, slk eu to a 5 horas vendo isso aqui ja minha cabeça n entra mais nada eu vo morrer, as cores nao tao funcionando no meu terminal, mas a funcionalidade ta ai, ent fé