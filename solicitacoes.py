import sqlite3
import servicos
from tela_administrador import obter_servico_administrador

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

"""
- O CLIENTE possui autorização apenas de enviar sua(s) solicitação(ções) e consultar(-las), para verificar o status, por exemplo;
"""

# ----- TELA DE SOLICITAÇÕES DO > CLIENTE < -----

def menu_solicitacao_cliente():
    """
    - Função para exibir o menu principal do arquivo, que possui opções de : [v] Voltar ao menu principal, [1] , [2] ;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_solicitacao_cliente():
    """

    while True:
        opcao = input("""
*********************************************************
    _____________________ OPÇÕES ____________________

    [v] ...................................... Voltar
    [1] .......................... Enviar solicitação
    [2] ....................... Consultar solicitação
*********************************************************

>>> Digite a opção: """)
        if opcao == 'v':
            print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
            break
        elif opcao == '1':
            print('\n - ENVIAR SOLICITAÇÃO - \n')
            enviar_solicitacao_cliente()
        elif opcao == '2':
            print('\n - CONSULTAR SOLICITAÇÃO - \n')
            consultar_solicitacao_cliente()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def enviar_solicitacao_cliente():
    """
    - Função para inserir a solicitação do cliente na tabela 'solicitacoes';
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> enviar_solicitacao_cliente():
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
            descricao_solicitacao = input('Digite a DESCRIÇÃO do problema: ')
            endereco_solicitacao = input('Digite o ENDEREÇO do problema: ')
            print()
            id_servico=servicos.servicos() 
            print()
            status_solicitacao = 'recebido'
            cursor.execute('INSERT INTO solicitacoes VALUES (null,?,?,?,null,?)',(descricao_solicitacao,endereco_solicitacao,status_solicitacao,id_servico))
            conexao_db.commit()
            print(f'\n - SOLICITAÇÃO FEITA!!! - \n')
            menu_solicitacao_cliente()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def consultar_solicitacao_cliente():
    """
    - Função para visualizar a solicitação do cliente na tabela 'solicitacoes';
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> consultar_solicitacao_cliente():
    """
    ver_solicitacao = obter_solicitacao()

    print(f"|{'ID':<3}|{'ENDEREÇO':<50}|{'DESCRIÇÃO':<50}|{'STATUS':<20}|{'ID CLIENTE':<15}|{'ID SERVIÇO':<15}|")
    print('-'*160)

    for solicitacao in ver_solicitacao:
        print(f"|{solicitacao[0]:<3}|{solicitacao[1]:<50}|{solicitacao[2]:<50}|{solicitacao[3]:<20}|{solicitacao[4]:<15}|{solicitacao[5]:<15}|")

def obter_solicitacao():
    """
    Obtem os valores da tabela 'solicitacoes';
    Não recebe parâmetros;
    Exemplo de uso:
    >>> obter_solicitacao()
    """
    cursor.execute(""" SELECT * FROM solicitacoes """)

    resultados = cursor.fetchall()
    solicitacoes = []
    for resultado in resultados:
        solicitacao = list(resultado)
        solicitacoes.append(solicitacao)
    return solicitacoes
    conexao_db.commit()




# ----- TELA DE SOLICITAÇÕES DO > ADMINISTRADOR < -----

'''
- O ADMINISTRADOR possui autorização de visualizar todas as solicitações que foram feitas, editar ou excluir alguma solicitação.
'''

def obter_solicitacao_administrador():
    # Obter os valores da tabela solicitação
    cursor.execute(""" SELECT id_solicitacao,nome_cliente,email_cliente,nome_servico,tipo_servico,endereco_solicitacao FROM solicitacao
                    INNER JOIN servicos on id_servico = fk_id_servico
                    INNER JOIN clientes on id_cliente = fk_id_cliente  """)
    resultados = cursor.fetchall()

    for resultado in resultados:
        solicitacoes = []
        #transforma a tupla em uma lista
        solicitacao = list(resultado)
        #agrupa listas
        solicitacoes.append(solicitacao)
        return solicitacoes

def visualizar_solicitacoes_administrador():
    # Função para visualizar os valores 
    ver_solicitacao = obter_servico_administrador()
    print(ver_solicitacao)
    
    print(f"| {'ID':<3} | {'cliente':<20} | {'email':<20} | {'serviço':<20} |{'tipo de serviço':<20} |{'local':<20} |")
    print('='* 130)

    for solicitacao in ver_solicitacao:
        print(f"| {solicitacao[0]:<3} | {solicitacao[1]:<20} | {solicitacao[2]:<20} | {solicitacao[3]:<20} |{solicitacao[4]:<20} |{solicitacao[5]:<20} |")

if __name__ == '__main__':
    menu_solicitacao_cliente()
