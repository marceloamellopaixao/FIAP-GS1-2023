from functions.utilidades import *
from functions.personalizacao import linha

donates = ['[1] - Caridade com Valores', '[2] - Caridade com Insumos', '[0] - Voltar ao Menu']


def caridade_value():
    while True:
        linha()
        print('[                DONATE -- SEMEAMOS                ]')
        linha()

        print()
        doar = input('Gostaria de doar para a caridade com dinheiro? (S/N): ')
        if doar == 's':
            value = float(input('Informe o valor a ser doado: '))
            print('Formas de Pagamento: Pix, Dinheiro, Cartao de Credito ou Debito')
            forma_pagamento = input('Digite a forma de pagamento: ')

            print(f'O valor doado foi de R$ {value:.2f} - Forma de Pagamento: {forma_pagamento}')
            print()
            voltar_menu()

        else:
            print()
            doacao()
            break


def caridade_insumos():
    while True:
        linha()
        print('[                DONATE -- SEMEAMOS                ]')
        linha()

        print()
        doar_insumo = input('Gostaria de doar para a caridade com insumos? (S/N): ')
        if doar_insumo == 's':
            insumo = input('Informe o insumo a ser doado: ')
            print(f'O valor doado foi de R$ {insumo}')
            print()
            voltar_menu()

        else:
            print()
            doacao()
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
            doacao()
            break

        else:
            print()
            print('ATENCAO!! [Este dado nao corresponde ao solicitado, digitar somente (S ou N)!]')
            print()
            voltar_menu()
            break


def opcoes_donates():
    for i in range(3):  # [0, 1, 2] = 1, 2, 0
        print(donates[i])


def doacao():
    linha()
    print('[                DONATE -- SEMEAMOS                ]')
    linha()

    print()
    opcoes_donates()
    print()

    try:
        opcao_duvida = int(input('Digite o numero da opcao desejada: '))
        while opcao_duvida >= 3 or opcao_duvida < 0:
            opcao_duvida = int(input('Opcao invalida! Digite a opcao desejada: '))

        if opcao_duvida == 1:
            caridade_value()

        elif opcao_duvida == 2:
            caridade_insumos()

        else:
            voltar_menu()

    except ValueError:
        print('ATENCAO!! [Este dado nao corresponde ao solicitado, digitar somente numeros (1,2,3...)!]')
        print()
        doacao()
