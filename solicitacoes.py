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
        print("""
*********************************************************
    ______________ DADOS DA SOLICITAÇÃO _____________

    [v] ...................................... Voltar
    [1] .......................... DESCRICAO solicitação
    [2] ....................... ENDERECO solicitação
*********************************************************
""")
        descricao_solicitacao = input('Digite a descrição do problema: ')
        endereco_solicitacao = input('Digite o endereço do problema: ')

def consultar_solicitacao():
    pass
