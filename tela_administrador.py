import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

def menu_administrador():
    """
    - Função para exibir o menu principal do arquivo, que possui opções de : [v] Voltar ao menu principal, [1] , [2] , [3] ;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_administrador():
    """

    while True:
        opcao = input("""
*********************************************************
    _____________________ OPÇÕES ____________________

    [v] .................... Voltar ao menu principal
    [1] .................... Visualizar solicitacoes
    [2] .................... Editar clientes
    [3] .................... 
*********************************************************

>>> Digite a opção: """)
        if opcao == 'v':
            print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
            break
        elif opcao == '1':
            print('\n -  - \n')
            visualizar_solicitacoes()
        elif opcao == '2':
            print('\n -  - \n')
            editar_clientes()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def visualizar_solicitacoes():
    pass

def editar_clientes():
    pass

if __name__ == '__main__':
    menu_administrador()
