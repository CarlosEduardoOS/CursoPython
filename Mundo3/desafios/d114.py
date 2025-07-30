#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request
#urllib.request é um módulo da biblioteca padrão do Python que permite abrir e manipular URLs de forma programática, ou seja, fazer requisições HTTP e FTP diretamente do Python sem precisar instalar bibliotecas externas.
def site_acessivel(url):
    try:
        response = urllib.request.urlopen(url)
        return True
    except urllib.error.URLError:
        return False

# Programa principal
url = 'http://www.pudim.com.br'
if site_acessivel(url):
    print(f'O site {url} está acessível.')
else:
    print(f'O site {url} não está acessível.')
#Este código testa se um site está online ao tentar abrir a URL, usando tratamento de exceção para retornar True se o site está acessível e False se não estiver, permitindo automatizar verificações de conectividade em seus projetos.