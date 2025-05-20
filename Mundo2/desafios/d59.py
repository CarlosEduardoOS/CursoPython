print('===== Menu Calculadora =====')
import textwrap
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')
opcao = int(input('>>>>> Escolha uma opção: '))
while opcao != 5:
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
        print(textwrap.dedent('''\
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa
        '''))
        opcao = int(input('>>>>> Escolha uma opção: '))
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
        print(textwrap.dedent('''\
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa
        '''))
        opcao = int(input('>>>>> Escolha uma opção: '))
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}.')
            print(textwrap.dedent('''\
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 4 ] Novos Números
            [ 5 ] Sair do Programa
            '''))
            opcao = int(input('>>>>> Escolha uma opção: '))
        elif n2 > n1:
            print(f'O maior número é {n2}.')
            print(textwrap.dedent('''\
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 4 ] Novos Números
            [ 5 ] Sair do Programa
            '''))
            opcao = int(input('>>>>> Escolha uma opção: '))
        else:
            print('Os números são iguais.')
            print(textwrap.dedent('''\
            [ 1 ] Somar
            [ 2 ] Multiplicar
            [ 3 ] Maior
            [ 4 ] Novos Números
            [ 5 ] Sair do Programa
            '''))
            opcao = int(input('>>>>> Escolha uma opção: '))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print(textwrap.dedent('''\
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa
        '''))
        opcao = int(input('>>>>> Escolha uma opção: '))
    else:
        print('Opção inválida. Tente novamente.')

print('Finalizando...')
print('Fim do programa! Volte sempre!')
    