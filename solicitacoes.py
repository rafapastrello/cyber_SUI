import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

def enviar_solicitacao():
    """
    - Função para inserir a solicitação do cliente na tabela 'solicitacoes';
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> enviar_solicitacao():
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
            cursor.execute('INSERT INTO solicitacoes VALUES (null,?,?,?,null,null)',(descricao_solicitacao,endereco_solicitacao,status_solicitacao))
            conexao_db.commit()
            print(f'\n - SOLICITAÇÃO FEITA!!! - \n')
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def consultar_solicitacao():
    """
    - Função para visualizar a solicitação do cliente na tabela 'solicitacoes';
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> consultar_solicitacao():
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

if __name__ == '__main__':
    consultar_solicitacao()
