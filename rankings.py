import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

def menu_rank():
    while True:
        escolha = input("""
****************************************************
    __________________ OPÇÕES __________________

    [v] .............. Voltar 
    [1] .............. SERVIÇO
    [2] .............. LOCAL
                        
Escolha: """)

        if( escolha =='1'):
            rank_solicitacao_servico()
        elif(escolha =='2'):
            rank_solicitacao_local()

def rank_solicitacao_servico():
    cursor.execute(""" SELECT nome_servico, COUNT(id_solicitacao)  AS quandidade_soliciacoes FROM solicitacao
                    INNER JOIN servico on id_servico = fk_id_servico
                    GROUP BY nome_servico
                    ORDER BY nome_servico DESC""")

    resultados = cursor.fetchall()
    print(f"|{'serviço':<20}|{'Quantidade de solicitações':<30}|")
    print('-'*50)
    for resultado in resultados:
        servico = list(resultado)
        print(f'|{servico[0]:<20}|{servico[1]:<30}|')

def rank_solicitacao_local():
    cursor.execute(""" SELECT endereco_solicitacao, COUNT(id_solicitacao) AS quandidade_soliciacoes FROM solicitacao
                    INNER JOIN servicos on id_servico = fk_id_servico
                    GROUP BY endereco_solicitacao
                    ORDER BY endereco_solicitacao DESC """)

    resultados = cursor.fetchall()
    print(f"|{'local':<20}|{'Quantidade de solicitações':<30}|")
    print('-'*50)
    for resultado in resultados:
        servico = list(resultado)
        print(f'|{servico[0]:<20}|{servico[1]:<30}|')
