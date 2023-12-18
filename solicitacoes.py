import tela_cliente
import sqlite3
import servicos

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_sui.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

"""
- O CLIENTE possui autorização apenas de enviar sua(s) solicitação(ções) e consultar(-las), para verificar o status, por exemplo;
"""

# ----- TELA DE SOLICITAÇÕES DO > CLIENTE < -----

def menu_solicitacao_cliente(cpf_cliente):
    """
    - Função para exibir o menu principal do arquivo, que possui opções de Voltar ao menu principal, enviar ou consultar solicitação;
    - Recebe 'cpf_cliente' como parâmetro;
    - Exemplo de uso:
    >>> menu_solicitacao_cliente(cpf_cliente):
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
            enviar_solicitacao_cliente(cpf_cliente)
        elif opcao == '2':
            print('\n - CONSULTAR SOLICITAÇÃO - \n')
            consultar_solicitacao_cliente()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def enviar_solicitacao_cliente(cpf_cliente):
    """
    - Função para inserir a solicitação do cliente na tabela 'solicitacoes';
    - Recebe 'cpf_cliente' como parâmetro;
    - Exemplo de uso:
    >>> enviar_solicitacao_cliente(cpf_cliente):
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
            status_solicitacao = 'recebido'
            id_cliente = tela_cliente.obtem_id_cliente(cpf_cliente)
            tabela_servicos_disponiveis = servicos.visualizar_servicos()
            id_servico_desejado = input('Digite o ID do serviço desejado: ')
            cursor.execute('INSERT INTO solicitacoes VALUES (null,?,?,?,?,?)',(descricao_solicitacao,endereco_solicitacao,status_solicitacao,id_cliente,id_servico_desejado,))
            conexao_db.commit()
            print(f'\n - SOLICITAÇÃO FEITA!!! - \n')
            menu_solicitacao_cliente(cpf_cliente)
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
    - Obtem os valores da tabela 'solicitacoes';
    - É usada na função 'consultar_solicitacao_cliente'
    - Não recebe parâmetros;
    - Exemplo de uso:
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

def visualizar_servico_cliente():
    """
    - Visualiza os valores da tabela 'servicos';
    - É usada na função 'enviar_solicitacao_cliente'
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> obter_solicitacao()
    """
    ver_servico = servicos.obter_servicos()

    print(f"|{'ID':<3}|{'nome do serviço':<30}|{'tipo de serviço':<40}|")
    print('-'*60)

    for servico in ver_servico:
        print(f"|{servico[0]:<3}|{servico[1]:<30}|{servico[2]:<40}|")

if __name__ == '__main__':
    menu_solicitacao_cliente()
