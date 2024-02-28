from functions.utilidades import *
from functions.bd import insere_valor
from functions.personalizacao import linha

# Opções de Cadastro / (Opção 1 do MENU)
opcoesCadastro = ['[1] - Agroindustrias', '[2] - Empresas de Fertilizante', '[3] - Produtor Rural',
                  '[4] - Resíduos Disponíveis', '[5] - Transação', '[0] - Voltar ao Menu']


def new_agroindustria():
    while True:
        print()
        linha()
        print('[            Agroindustrias -- SEMEAMOS            ]')
        linha()

        print()
        print('Nesta guia será efetuada o cadastro de Agroindustrias.')
        agro_continuar = input('Gostaria de continuar? (S/N): ').strip().lower()
        print()
        if agro_continuar == 's':
            # Nome da Lista
            newAgroind = []
            # Nome do Conteúdo à adicionar.
            agroind = {'Razao Social': input('Digite a razão social da Agroindustria: ').strip().capitalize(),
                       'CNPJ': input('Digite o cnpj da Agroindustria: ').strip().lower()}

            # Esta função insere os dados na lista acima
            bdAgroindustria.append(agroind)
            newAgroind.append(agroind)

            # Esta função salva todos os dados no arquivo "txt"
            agroind_mais = input('Deseja fazer um novo cadastro? (S/N): ').strip().lower()
            if agroind_mais == 's':
                insere_valor('./banco_dados/bdAgroindustria.txt', newAgroind)
                ''' 
                Versão Anterior:
                    with open(str('./banco_dados/bdAgroindustria.txt'), 'a+') as file:
                        for agroindInsert in newAgroind:
                            file.write(str(agroindInsert) + '\n')
                '''
                continue

            else:
                insere_valor('./banco_dados/bdAgroindustria.txt', newAgroind)
                # Retorna a página de Cadastros e Trava a repetição atual.
                print()
                cadastro()
                break
        else:
            print('Obrigado por tentar nosso serviço!')
            print()
            cadastro()
            break


def new_empresa_fertilizante():
    while True:
        linha()
        print('[        Empresa de Fertilizante - SEMEAMOS        ]')
        linha()

        print()
        print('Nesta guia será efetuada o cadastro de empresa de fertilizante.')
        empFertilizante_continuar = input('Gostaria de continuar? (S/N): ').strip().lower()
        print()
        if empFertilizante_continuar == 's':
            # Nome da Lista
            newEmpFertilizante = []

            # Nome do Conteúdo à adicionar.
            empFert = {'Razao Social': input('Digite a razão social da empresa de fertilizante: ').strip().capitalize(),
                       'CNPJ': input('Digite o cnpj da empresa de fertilizante: ').strip().lower()}

            # Esta função insere os dados na lista acima
            bdEmpFertilizante.append(empFert)
            newEmpFertilizante.append(empFert)

            # Esta função salva todos os dados no arquivo "txt"
            agroind_mais = input('Deseja fazer um novo cadastro? (S/N): ').strip().lower()
            if agroind_mais == 's':
                insere_valor('./banco_dados/bdEmpFertilizante.txt', newEmpFertilizante)
                continue

            else:
                insere_valor('./banco_dados/bdEmpFertilizante.txt', newEmpFertilizante)
                # Retorna a página de cadastros e para a repetição atual.
                print()
                cadastro()
                break
        else:
            print('Obrigado por tentar nosso serviço!')
            print()
            cadastro()
            break


def new_produtor_rural():
    while True:
        linha()
        print('[            Produtor Rural -- SEMEAMOS            ]')
        linha()

        print()
        print('Nesta guia será efetuada o cadastro do produtor rural.')
        prodRural_continuar = input('Gostaria de continuar? (S/N): ').strip().lower()
        print()
        if prodRural_continuar == 's':
            # Nome da Lista
            newProdRural = []
            newProdRuralReg = []

            # Nome do Conteúdo à adicionar.
            prodRural = {'Nome Completo': input('Digite o nome completo do produtor rural: ').strip().capitalize(),
                         'CPF': input('Digite o CPF do produtor rural: ').strip().lower(),
                         'RG': input('Digite o RG do produtor rural: ').strip().lower()}

            prodRuralRegistro = {'Tipo da Produção': input('Digite o tipo da produção: ').strip().lower(),
                                 'Quantidade Produzida': float(input('Digite a quantidade produzida: ')),
                                 'Preço Avaliado': float(input('Digite o preço avaliado: '))}

            # As variáveis abaixo recebe os dados de prodRural, separando cada valor para seu determinado arquivo.

            # Registro do Produtor Rural
            prodRuralReg = ['Nome do Produtor: ', prodRural['Nome Completo'], 'CPF: ', prodRural['CPF'],
                            'Tipo de Produção: ', prodRuralRegistro['Tipo da Produção'],
                            'Quantidade Produzida: ', prodRuralRegistro['Quantidade Produzida'], 'Preço Avaliado: ',
                            prodRuralRegistro['Preço Avaliado']]
            # Estas funções abaixo inserem os dados na lista acima, pulando uma linha a cada cadastro novo
            # Armazena no arquivo.txt
            bdProdRural.append(prodRural)
            bdRegistro.append(prodRuralReg)

            # Armazenamento Temporário.
            newProdRural.append(prodRural)  # Armazena o cadastro do produtor
            newProdRuralReg.append(prodRuralReg)  # Armazena o registro e a identificação do produtor.

            # Esta função abaixo salva todos os dados no arquivo.txt
            print()
            prodRural_mais = input('Deseja fazer um novo cadastro? (S/N): ').strip().lower()
            print()
            if prodRural_mais == 's':
                insere_valor('./banco_dados/bdProdRural.txt', newProdRural)
                insere_valor('./banco_dados/bdRegistro.txt', newProdRuralReg)
                continue

            else:
                insere_valor('./banco_dados/bdProdRural.txt', newProdRural)
                insere_valor('./banco_dados/bdRegistro.txt', newProdRuralReg)
                # Retorna a página de cadastros e para a repetição atual.
                print()
                cadastro()
                break
        else:
            print('Obrigado por tentar nosso serviço!')
            print()
            cadastro()
            break


def new_residuos_disponiveis():
    while True:
        linha()
        print('[         Resíduos Disponíveis -- SEMEAMOS         ]')
        linha()

        print()
        print('Nesta guia será efetuada o cadastro dos residuos disponíveis.')
        residuoDisp_continuar = input('Gostaria de continuar? (S/N): ').strip().lower()
        print()
        if residuoDisp_continuar == 's':
            # Nome da Lista
            newResiduoDisponivel = []

            # Nome do Conteúdo à adicionar.
            residuoDispContent = {'Tipo': input('Digite o tipo do resíduo disponível: ').strip().capitalize(),
                                  'Lote': input('Digite o lote do resíduo disponível: ').strip().lower(),
                                  'Peso': float(input('Digite o peso do resíduo disponível (somente números): ')),
                                  'Preço kg': float(input('Digite o preço da kilograma (somente números): '))}

            precoResiduo = {'Cálculo do Preço': residuoDispContent['Peso'] * residuoDispContent['Preço kg']}

            residuoDisp = [residuoDispContent, precoResiduo]
            # Esta função insere os dados na lista acima
            # Armazena na lista.txt
            bdResiduoDisp.append(residuoDisp)

            # Armazena na lista temporária
            newResiduoDisponivel.append(residuoDisp)

            # Esta função salva todos os dados no arquivo "txt"
            print()
            residuoDisp_mais = input('Deseja fazer um novo cadastro? (S/N): ').strip().lower()
            print()
            if residuoDisp_mais == 's':
                insere_valor('./banco_dados/bdResiduoDisp.txt', newResiduoDisponivel)
                continue

            else:
                insere_valor('./banco_dados/bdResiduoDisp.txt', newResiduoDisponivel)
                # Retorna a página de cadastros e para a repetição atual.
                print()
                cadastro()
                break
        else:
            print('Obrigado por tentar nosso serviço!')
            print()
            cadastro()
            break


def new_transacao():
    while True:
        linha()
        print('[               Transação -- SEMEAMOS              ]')
        linha()

        print()
        print('Nesta guia será efetuada o cadastro da transação.')
        transacao_continuar = input('Gostaria de continuar? (S/N): ').strip().lower()
        print()
        if transacao_continuar == 's':
            # Nome da Lista
            newTransacao = []

            # Nome do Conteúdo à adicionar.
            transacao = {'Valor': float(input('Digite o valor para a transação ser concluída: ')),
                         'Forma de Pagamento': input('Digite a forma de pagamento: ').strip().lower()}

            # Esta função insere os dados na lista acima
            bdTransacao.append(transacao)
            newTransacao.append(transacao)

            # Esta função salva todos os dados no arquivo "txt"
            print()
            transacao_mais = input('Deseja fazer um novo cadastro? (S/N): ').strip().lower()
            print()
            if transacao_mais == 's':
                insere_valor('./banco_dados/bdTransacao.txt', newTransacao)
                continue

            else:
                insere_valor('./banco_dados/bdTransacao.txt', newTransacao)
                # Retorna a página de cadastros e para a repetição atual.
                print()
                cadastro()
                break
        else:
            print('Obrigado por tentar nosso serviço!')
            print()
            cadastro()
            break


def voltar_menu():
    while True:
        linha()
        print('[            VOLTAR AO MENU - SEMEAMOS!            ]')
        linha()

        print()
        voltar = input('Gostaria de voltar realmente ao Menu? (S/N): ').strip().lower()
        if voltar == 's':
            print()
            menu()
            break

        elif voltar == 'n':
            print()
            cadastro()
            break

        else:
            print()
            print('ATENCAO!! [Este dado nao corresponde ao solicitado, digitar somente (S ou N)!]')
            print()
            voltar_menu()
            break


def opcoes_cadastro():
    """
        Esta função imprime todas as opções de Cadastro:

        [1] - Agroindustrias /
        [2] - Empresas de Fertilizante /
        [3] - Produtor Rural /
        [4] - Resíduos Disponíveis /
        [5] - Transação /
        [6] - Voltar ao Menu
    """

    for i in range(6):  # [0, 1, 2, 3, 4, 5] = 1, 2, 3, 4, 5, 6
        print(opcoesCadastro[i])


def cadastro():
    linha()
    print('[               CADASTRO -- SEMEAMOS               ]')
    linha()

    print()
    opcoes_cadastro()
    print()

    try:
        opcao_cadastro = int(input('Digite o número da opção desejada: '))
        print()
        while opcao_cadastro >= 6 or opcao_cadastro < 0:
            opcao_cadastro = int(input('Opção inválida! Digite a opção desejada: '))

        if opcao_cadastro == 1:
            new_agroindustria()

        elif opcao_cadastro == 2:
            new_empresa_fertilizante()


        elif opcao_cadastro == 3:
            new_produtor_rural()


        elif opcao_cadastro == 4:
            new_residuos_disponiveis()


        elif opcao_cadastro == 5:
            new_transacao()

        else:
            voltar_menu()

    except ValueError:
        print('ATENÇÃO!! [Este dado não corresponde ao solicitado, digitar somente números (1,2,3...)!]')
        print()
        cadastro()
