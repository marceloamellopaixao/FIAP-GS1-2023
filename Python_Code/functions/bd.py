# Função que verifica se o arquivo é existente
def verifica_arquivo(arquivo, banco):
    with open(str(arquivo), 'r', encoding='utf-8') as file:
        content = file.readlines()
    content = [x.strip('\n') for x in content]

    lenght = len(content)

    if lenght > 0:
        for i in range(lenght):
            banco.append(content[i])


def cria_arquivo(nome_arquivo_ext):
    open(nome_arquivo_ext, 'a+', encoding='utf-8').close()

    # Versão Anterior
    # with open(nome_arquivo_ext, 'w', encoding='utf-8') as file:
    #     file.write()


# Esta função vai ler o arquivo (Banco de dados) no início da execução
def file_reader(bd_usuarios, bd_agroindustria, bd_emp_fertilizante, bd_produtor_rural, bd_residuo_disp, bd_transacao,
                bd_registro):
    """
    Esta função irá verificar se os arquivos utilizados como banco de dados estão disponíveis na pasta,
    caso a pasta estiver vazia será criada todas as bases de dados, para poderem ser utilizadas.

    Se houver a possibilidade de apagar um dos arquivos,
     ao executar o programa irá criar novamente somente o arquivo faltante

    O retorno abaixo, faz a conexão da lista com o arquivo.txt:
    :return: bdUsuarios, bdAgroindustria, bdEmpFertilizante, bdProdRural, bdResiduoDisp, bdRegistro
    """
    try:
        verifica_arquivo('./banco_dados/bdUsuarios.txt', bd_usuarios)
    except FileNotFoundError:
        cria_arquivo('./banco_dados/bdUsuarios.txt')

    try:
        verifica_arquivo('./banco_dados/bdAgroindustria.txt', bd_agroindustria)
    except FileNotFoundError:
        cria_arquivo('./banco_dados/bdAgroindustria.txt')

    try:
        verifica_arquivo('./banco_dados/bdEmpFertilizante.txt', bd_emp_fertilizante)
    except FileNotFoundError:
        cria_arquivo('./banco_dados/bdEmpFertilizante.txt')

    try:
        verifica_arquivo('./banco_dados/bdProdRural.txt', bd_produtor_rural)
    except FileNotFoundError:
        cria_arquivo('./banco_dados/bdProdRural.txt')

    try:
        verifica_arquivo('./banco_dados/bdResiduoDisp.txt', bd_residuo_disp)
    except FileNotFoundError:
        cria_arquivo('./banco_dados/bdResiduoDisp.txt')

    try:
        verifica_arquivo('./banco_dados/bdTransacao.txt', bd_transacao)
    except FileNotFoundError:
        cria_arquivo('./banco_dados/bdTransacao.txt')

    try:
        verifica_arquivo('./banco_dados/bdRegistro.txt', bd_registro)
    except FileNotFoundError:
        cria_arquivo('./banco_dados/bdRegistro.txt')

    finally:
        return bd_usuarios, bd_agroindustria, bd_emp_fertilizante, bd_produtor_rural, bd_residuo_disp, bd_transacao, \
            bd_registro


def insere_valor(arquivo, lista_tmp):
    with open(arquivo, 'a+', encoding='utf-8') as file:
        for insert in lista_tmp:
            file.write(str(insert) + '\n')
