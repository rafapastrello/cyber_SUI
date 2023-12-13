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

    Digite [1] para voltar
    Digite [2] para continuar à solicitação
*********************************************************

>>> Digite a opção: """)
        if opcao == '1':
            print('\n - VOLTANDO AO MENU DE OPÇÕES!!! - \n')
            break
        elif opcao == '2':
            descricao_solicitacao = input('Digite a DESCRICAO do problema: ')
            endereco_solicitacao = input('Digite o ENDERECO do problema: ')
            cursor.execute('INSERT INTO clientes VALUES (null,?,?,null,null)',(descricao_solicitacao,endereco_solicitacao,))
            conexao_db.commit()
            print(f'\n - SOLICITAÇÃO FEITA!!! - \n')
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def consultar_solicitacao():
    pass

if __name__ == '__main__':
    enviar_solicitacao()