#esse eu não tive ideia de como faze tive qyue ver o video

expressao = input('Digite a expressão: ')
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')  # Para marcar erro
            break

if len(pilha) == 0:
    print('A expressão está válida.')
else:
    print('A expressão está inválida.')