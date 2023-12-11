import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

def menu_cliente():
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
    [1] ........................... Enviar reclamação
    [2] ........................ Consultar reclamação
*********************************************************

>>> Digite a opção: """)
        if opcao == 'v':
            print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
            break
        elif opcao == '1':
            print('\n -  - \n')
            enviar_reclamacao()
        elif opcao == '2':
            print('\n -  - \n')
            consultar_reclamacao()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def enviar_reclamacao():
    pass

def consultar_reclamacao():
    pass

if __name__ == '__main__':
    menu_cliente()
