from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
else:
    print('Arquivo encontrado com sucesso!')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
        #Opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
        cadastrar(leiaStr('Nome: '), leiaInt('Idade: '), arq)
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Opção inválida! Tente novamente.\033[m')
    sleep(2)