('===== Detector de Palíndromos =====')
frase = str(input('Digite uma frase: ')).strip().upper().replace(" ", "") # o .strp tira os espaços
# o .replace esta repocionando os espaços por nada
invertida = frase[::-1]# o [::-1] inverte a string, o chat que deu essa dica
if frase == invertida:
    print(f'A frase {frase} é um palíndromo!')
else:
    print(f'A frase {frase} não é um palíndromo!')
