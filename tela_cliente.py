import sqlite3
import solicitacoes

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

def menu_cliente():
    """
    - Função para verificar se o cliente já está cadastrado ou não, se não estiver cadastrado, ele é redirecionado à função 'menu_cadastro_cliente';
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_cliente():
    """

    while True:
        menu = input("""
********************************************************
    _______________ CADASTRO CLIENTE _______________

        Digite [1] para cliente já cadastrado
        Digite [2] para cliente sem cadastro
        
******************************************************** 

>>> Digite a opção: """)
        if menu == '1':
            # Cliente informa que possui cadastro, então digita o CPF para verificarmos se é existente no banco de dados
            # Se o cliente for existente no banco de dados, ele recebe a mensagem "cadastrado como >Nome do Cliente<" e é redirecionado às funcionalidades de solicitações do usuário
            # Se não estiver cadastrado no banco de dados, ele recebe a mensagem de "CPF inexistente"
            cpf_cliente = input('\n>>> Informe seu CPF: ')

            print('cpf_cliente: ',cpf_cliente)

            cursor.execute('SELECT cpf_cliente FROM clientes WHERE cpf_cliente = ?', (cpf_cliente,))
            verifica_cpf_cliente = cursor.fetchone()

            cursor.execute('SELECT nome_cliente FROM clientes WHERE cpf_cliente = ?', (cpf_cliente,))
            nome_cliente_cadastrado = cursor.fetchone()

            if verifica_cpf_cliente != None:
                print(f'\n - CADASTRADO COMO > {nome_cliente_cadastrado} < !!! - \n')
                menu_solicitacao_cliente()
            else:
                print('\n - CPF INEXISTENTE!!! - \n')
        elif menu == '2':
            # Ao informar que o cliente não possui cadastro, ele decide se quer ser cadastrado ou não
            opcao = input("""
***********************************************
    ____ DESEJA REALIZAR SEU CADASTRO? ____

            Digite [1] para SIM
            Digite [2] para NÃO
*********************************************** 

>>> Digite a opção: """)
            if opcao == '1':
                menu_cadastro_cliente()
            if opcao == '2':
                menu_cliente()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def menu_cadastro_cliente():
    """
    - Função para cadastrar cliente;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_cadastro_cliente():
    """

    while True:
        menu = input("""
*********************************************************
    __________________ CADASTRE-SE __________________

        Digite [1] para voltar ao menu de cadastramento
        Digite [2] para continuar ao cadastro de cliente
        
********************************************************* 

>>> Digite a opção: """)
        if menu == '1':
            print('\n - VOLTANDO AO MENU DE CADASTRO!!! - \n')
            break
        elif menu == '2':
            cpf_cliente = input('Digite seu CPF: ')
            email_cliente = input('Digite seu email: ')
            nome_cliente = input('Digite seu nome completo: ') 
            telefone_cliente = input('Digite seu telefone: ')
            print(f'\n - CLIENTE > {nome_cliente} < CADASTRADO - \n')
            menu_cliente()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def menu_solicitacao_cliente():
    """
    - Função para exibir o menu principal do arquivo, que possui opções de : [v] Voltar ao menu principal, [1] , [2] , [3] ;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_cliente():
    """

    while True:
        opcao = input("""
*********************************************************
    _____________________ OPÇÕES ____________________

    [v] .................... Voltar ao menu principal
    [1] .......................... Enviar solicitação
    [2] ....................... Consultar solicitação
*********************************************************

>>> Digite a opção: """)
        if opcao == 'v':
            print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
            break
        elif opcao == '1':
            print('\n - ENVIAR SOLICITAÇÃO - \n')
            solicitacoes.enviar_solicitacao()
        elif opcao == '2':
            print('\n - CONSULTAR SOLICITAÇÃO - \n')
            consultar_solicitacao()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def consultar_solicitacao():
    pass

if __name__ == '__main__':
    menu_cliente()
