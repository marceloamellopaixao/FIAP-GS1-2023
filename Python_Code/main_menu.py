from functions.bd import file_reader
from functions.utilidades import *
from functions.cadastro_main import cadastro
from functions.duvida_main import duvidas
from functions.donate_main import doacao

file_reader(bdUsuarios, bdAgroindustria, bdEmpFertilizante, bdProdRural, bdResiduoDisp, bdTransacao, bdRegistro)
user()
menu()

while True:
    try:

        opcaoMenu = int(input('Digite o número da opção desejada: '))
        print()

        while (opcaoMenu >= 4) or (opcaoMenu < 0):
            opcao = int(input("[Erro, Tente Novamente!] Digite o número de uma opção válida: "))
            print()

        # Opção 1 / Menu inicial _ Cadastro
        if opcaoMenu == 1:
            cadastro()

        # Opção 2 / Menu inicial _ Dúvidas
        elif opcaoMenu == 2:
            duvidas()

        # Opção 3 / Menu inicial _ Doação
        elif opcaoMenu == 3:
            doacao()

        # Opção 0 / Menu inicial _ Sair
        else:
            print('[Programa encerrado com Sucesso!]')
            print('')
            break

    except ValueError:
        print()
        print('ATENÇÃO!! [Este dado não corresponde ao solicitado, digitar somente números (1,2,3...)!]')
        print()
        menu()
