from functions.utilidades import *
from functions.personalizacao import linha

duvida = ['[1] - Como utilizar o programa?', '[2] - Como fazer cadastros?', '[0] - Voltar ao Menu']


def utiliza_program():
    while True:
        linha()
        print('[        Como utilizar o programa na Semeamos?        ]')
        linha()

        print()
        continuar = input('Gostaria de continuar? (S/N): ').strip().lower()
        if continuar == 's':
            print()
            print('Para utilizar o programa, basta seguir os passos abaixo:')
            print('1 Passo: Execute o Programa')
            print('2 Passo: Se cadastre')
            print('3 Passo: Selecione a opcao desejada e digite o numero dela, ex: uso (opcao 1)')
            print('4 Passo: Apos selecionar a opcao, siga o que pedir para cada funcionalidade')
            print('Pronto, siga os passos e voce conseguira seguir com as funcionalidades.')
            print()
            voltar_menu()

        else:
            print()
            duvidas()
            break


def utiliza_cadastro():
    while True:
        linha()
        print('[       Como efetuar cadastros na Semeamos?        ]')
        linha()

        print()
        continuar = input('Gostaria de continuar? (S/N): ').strip().lower()
        if continuar == 's':
            print()
            print('Cadastros:')
            print('Nos campos de cadastros ou ate mesmo ao tentar logar, o cadastro e feito automaticamente.')
            print('Todas as informacoes sao necessarias, caso falte um dado se quer a informacao nao sera armazenada.')
            print()
            voltar_menu()

        else:
            print()
            duvidas()
            break


def voltar_menu():
    while True:
        linha()
        print('[            VOLTAR AO MENU - SEMEAMOS!            ]')
        linha()

        print()
        voltar = input('Gostaria de voltar ao Menu? (S/N): ').strip().lower()
        if voltar == 's':
            print()
            menu()
            break

        elif voltar == 'n':
            print()
            duvidas()
            break

        else:
            print()
            print('ATENCAO!! [Este dado nao corresponde ao solicitado, digitar somente (S ou N)!]')
            print()
            voltar_menu()
            break


def opcoes_duvidas():
    for i in range(3):  # [0, 1, 2] = 1, 2, 0
        print(duvida[i])


def duvidas():
    linha()
    print('[                DUVIDAS - SEMEAMOS                ]')
    linha()

    print()
    opcoes_duvidas()
    print()

    try:
        opcao_duvida = int(input('Digite o numero da opcao desejada: '))
        while opcao_duvida >= 3 or opcao_duvida < 0:
            opcao_duvida = int(input('Opcao invalida! Digite a opcao desejada: '))

        if opcao_duvida == 1:
            utiliza_program()

        elif opcao_duvida == 2:
            utiliza_cadastro()

        else:
            voltar_menu()


    except ValueError:
        print('ATENCAO!! [Este dado nao corresponde ao solicitado, digitar somente numeros (1,2,3...)!]')
        print()
        duvidas()
