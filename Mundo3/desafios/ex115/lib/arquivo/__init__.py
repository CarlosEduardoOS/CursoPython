from ..interface import leiaInt, cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # função open tenta abrir o arquivo para leitura
        a.close() # se conseguir abrir, fecha o arquivo
    except FileNotFoundError:
        return False
    return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # esse wt+ cria o arquivo para escrita e leitura | w = write, t = text, + = read/write
        a.close() # se conseguir criar, fecha o arquivo
    except:
        print('Houve um erro na criação do arquivo!')
        return False
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        return True
    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')  # abre o arquivo para leitura
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.strip().split(';')  # strip remove \n
            print(f'Nome: {dado[0]}, Idade: {dado[1]}')
    finally:
        a.close()  # garante que o arquivo será fechado

def cadastrar(nome, idade, arquivo):
    try:
        a = open(arquivo, 'a+')  # abre para leitura e append
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            a.seek(0)  # vai para o início
            conteudo = a.read()
            if len(conteudo) > 0 and not conteudo.endswith('\n'):
                a.write('\n')  # adiciona quebra de linha se não houver
            a.write(f'{nome};{idade}\n')  # escreve o novo dado
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
    finally:
        a.close()

def leiaStr(msg):
    while True:
        try:
            valor = input(msg).strip()
            if valor == '':
                raise ValueError('Entrada inválida! Tente novamente.')
        except ValueError as e:
            print(e)
        else:
            return valor      