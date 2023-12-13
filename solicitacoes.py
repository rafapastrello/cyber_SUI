import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

def enviar_solicitacao():
    """
    - Função para exibir o menu de enviar a solicitação do cliente;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_solicitacao_cliente():
    """

    while True:
        

        opcao = input("""
*********************************************************
    ______________ DADOS DA SOLICITAÇÃO _____________

    [v] ...................................... Voltar
    [1] .......................... DESCRICAO solicitação
    [2] ....................... ENDERECO solicitação
*********************************************************

>>> Digite a opção: """)
        if opcao == 'v':
            print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
            break
        elif opcao == '1':
            print('\n - ENVIAR SOLICITAÇÃO - \n')
            enviar_solicitacao()
        elif opcao == '2':
            print('\n - CONSULTAR SOLICITAÇÃO - \n')
            consultar_solicitacao()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def consultar_solicitacao():
    pass
