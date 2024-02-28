from functions.personalizacao import linha
from functions.bd import insere_valor
import getpass

# Lista de Opções no Menu:
opcoesMenu = ['[1] - Cadastros', '[2] - Duvidas', '[3] - Doacao', '[0] - Sair']

#  Banco de Dados dos Utilizadores.
bdUsuarios = []

# Banco de Dados do Cadastro
bdAgroindustria = []
bdEmpFertilizante = []
bdProdRural = []
bdResiduoDisp = []
bdTransacao = []

# Banco de Dados de registros.
bdRegistro = []


def user():
    linha()
    print('[               BEM VINDO AO SEMEAMOS              ]')
    linha()

    print()
    print('Antes de iniciarmos, vamos criar um cadastro?')

    newUser = []

    # Nome do Conteúdo a adicionar.
    usuario = {'Nome': input('Digite seu nome inicial: ').strip(),
               'Username': input('Digite seu username para logar futuramente: ').strip().lower(),
               'E-mail': input('Digite seu e-mail: ').strip().lower(),
               'Senha': input("Crie sua senha: "),
               'Confirma Senha': input("Confirme sua senha: ")}

    print()
    while usuario['Confirma Senha'] != usuario['Senha']:
        usuario['Confirma Senha'] = input('As senhas nao correspondem, Confirme sua senha: ')
        print()
    # Esta função insere os dados na lista acima
    bdUsuarios.append(usuario)
    newUser.append(usuario)
    insere_valor('./banco_dados/bdUsuarios.txt', newUser)

    # Imprime um agradecimento ao usuário pelo cadastro efetuado.
    print(usuario['Nome'] + ', Obrigado pelas informacoes')
    print()



# Opções do Menu
def opcoes_menu():
    for i in range(4):
        print(opcoesMenu[i])


def menu():
    linha()
    print('[              MENU INICIAL - SEMEAMOS             ]')
    linha()
    print()

    opcoes_menu()
    print()
