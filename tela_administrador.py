import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_sui.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

# ----- TELA ADMINISTRADOR -----

def cadastrar_administrador():
    global id_usuario

    print( " (1) login            (2) Criar conta")
    print('='*20)
    entrada = input("escolha:")

    while( entrada!= '1' and entrada!='2' ):
        entrada = input("Escolha a alternativa correta:")

    while True:
        if (entrada =='1'):
            email = input("Digite seu email:")
            cursor.execute(f" SELECT * FROM administradores WHERE email_administrador = ? ",(email,))
            resposta = cursor.fetchone()
            if resposta:  
                print("usuario autentificado!")
                id_usuario = resposta[0]
                break  
            else:
                print(resposta)
                print("usuario não encontrado")
        elif entrada == '2':
            nome = input("Digite seu nome:")
            cpf = input("digite o seu CPF:")
            email = input("digite o seu email:")
            telefone = input("digite o seu telefone:")
            cursor.execute(" INSERT INTO administradores (nome_administrador,cpf_administrador,email_administrador,telefone_administrador) values (?,?,?,?)",(nome,cpf,email,telefone))
            id_usuario = cursor.lastrowid
            conexao_db.commit()
            break
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def menu_administrador():
    cadastrar_administrador()
    """
    - Função para exibir o menu principal do arquivo;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_administrador():
    """
    while True:
        opcao = input("""
****************************************************
    __________________ OPÇÕES __________________

    [v] .............. Voltar ao menu principal
    
    [1] .............. Visualizar serviços
    [2] .............. Criar serviço
    [3] .............. Editar serviço
    [4] .............. Deletar serviço
    [5] .............. Ver histórico     
    [6] .............. Modificar cadastro  
    [7] .............. Ver rank 
    [8] .............. Visualizar solicitações
    [9] .............. Editar solicitação 
    [10] ............. Excluir solicitação  

****************************************************

>>> Digite a opção: """)
        if opcao == 'v':
            print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
            break
        elif opcao == '1':
            print('\n - VISUALIZAR SERVIÇOS - \n')
            visualizar_servico_administrador()
        elif opcao == '2':
            print('\n - CRIAR SERVIÇO - \n')
            cadastrar_servico_administrador()
        elif opcao == '3':
            print('\n - EDITAR SERVIÇO - \n')
            editar_servico_administrador()
        elif opcao == '4':
            print('\n - DELETAR SERVIÇO - \n')
            excluir_servico_administrador()
        elif opcao == '5':
            print('\n - VISUALIZAR HISTÓRICO - \n')
            listar_modificacao_administrador()
        elif opcao == '6':
            print('\n - MODIFICAR PERFIL - \n')
            editar_administrador()
        elif opcao == '7':
            print('\n - RANKING SHOW - \n')
            rank()
        elif opcao == '8':
            print('\n - VISUALIZAR SOLICITAÇÕES - \n')
            visualizar_solicitacoes_administrador()
        elif opcao == '9':
            print('\n - EDITAR SOLICITAÇÕES - \n')
            editar_solicitacoes_status()
        elif opcao == '10':
            print('\n - DELETAR SOLICITAÇÕES - \n')
            deletar_solicitacoes()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def editar_administrador():
    item = input("[1]nome\n[2]email\n[3]telefone\n O que deseja mudar:")
    mudar = input('para que dejesa mudar:')
    dicionario = {'1':'nome_administrador','2':'email_administrador','3':'telefone_administrador'}
    cursor.execute(f'UPDATE administradores SET {dicionario[item]} =? where id_administrador=?',(mudar,id_usuario))
    conexao_db.commit()


# **** MODIFICAÇÕES *****

def modificacoes_administrador(servico,administrador,nome):
    # Insere os valores em modificação ( Como se fosse um histórico do adminstrador )
    cursor.execute(f"INSERT INTO modificacoes VALUES( NULL,?,?,?)",(administrador,servico,nome))

def listar_modificacao_administrador():
    # Lista modificação
    cursor.execute(""" SELECT id_modificacao,nome_administrador,email_administrador,nome_modificacao,id_servico FROM modificacoes 
                INNER JOIN administradores on fk_id_administrador = id_administrador 
                INNER JOIN servicos on fk_id_servico = id_servico """)
    resultados = cursor.fetchall()
    
    
    print(f"|{'ID':<3}|{'Nome ':<20}|{'Email do administrador':<30}|{'Modificação':<20}|{'ID serviço':<10}|")
    print('-'*80)
    for resultado in resultados:
        modificacao = list(resultado)
        print(f"|{modificacao[0]:<3}|{modificacao[1]:<20}|{modificacao[2]:<30}|{modificacao[3]:<20}|{modificacao[4]:<10}|")


# ***** SERVIÇOS *****

def cadastrar_servico_administrador():
    nome_servico = input("Digite o nome do serviço:")
    tipo_servico = input("Digite o tipo do serviço:")

    cursor.execute(" INSERT INTO servicos VALUES (NULL,?, ?)",(nome_servico,tipo_servico))
    id_servico = cursor.lastrowid
    modificacoes_administrador(id_servico, id_usuario,'cadastrou serviço')
    conexao_db.commit()

def editar_servico_administrador():
    id_servico = input("digite o id do serviço:")
    print('[1] nome\n[2] tipo')
    atributo = input("Qual atributo você dejesa editar:")
    troca = input("Qual dejesa colocar:")
    dicionario = {'1':'nome_servico','2':'tipo_servico'}

    cursor.execute(f" UPDATE servicos SET {dicionario[atributo]}=? WHERE id_servico = ?", (troca,id_servico))
    modificacoes_administrador(id_servico,id_usuario,'editou serviço')

    print("ESSE SERVIÇO FOI EDITADO !")
    conexao_db.commit()

def excluir_servico_administrador():
    id_servico = input("Digite o id do serviço:")

    cursor.execute(" DELETE FROM servicos WHERE id_servico = ?",(id_servico))
    print('-'*50)
    print(' ESSE SERVIÇO FOI DELETADO')
    conexao_db.commit()

def obter_servico_administrador():
    # obter os valores de serviços
    cursor.execute(""" SELECT * FROM servicos """)

    resultados = cursor.fetchall()
    servicos = []
    for resultado in resultados:
        servico = list(resultado)
        servicos.append(servico)
    return servicos

def visualizar_servico_administrador():
    ver_servico = obter_servico_administrador()

    print(f"|{'ID':<3}|{'nome do serviço':<30}|{'tipo de serviço':<40}|")
    print('-'*60)

    for servico in ver_servico:
        print(f"|{servico[0]:<3}|{servico[1]:<30}|{servico[2]:<40}|")


# ***** SOLICITAÇÃO *****
'''
- O ADMINISTRADOR possui autorização de visualizar todas as solicitações que foram feitas, editar ou excluir alguma solicitação.
'''

def obter_solicitacao_administrador():
    # Obter os valores da tabela solicitação
    cursor.execute(""" SELECT id_solicitacao,nome_cliente,status_solicitacao,nome_servico,tipo_servico,endereco_solicitacao status_solicitacao  FROM solicitacoes
                    INNER JOIN servicos on id_servico = fk_id_servico
                    INNER JOIN clientes on id_cliente = fk_id_cliente  """)
    resultados = cursor.fetchall()
    
    solicitacoes = []
    for resultado in resultados:
        
        #transforma a tupla em uma lista
        solicitacao = list(resultado)
        #agrupa listas
        solicitacoes.append(solicitacao)
    return solicitacoes

def visualizar_solicitacoes_administrador():
    # Função para visualizar os valores 
    ver_solicitacao = obter_solicitacao_administrador()
    
    print(f"| {'ID':<2} | {'cliente':<25} | {'status':<15} | {'serviço':<25} |{'tipo de serviço':<40} |{'local':<27} |")
    print('='* 150)

    for solicitacao in ver_solicitacao:
        print(f"| {solicitacao[0]:<2} | {solicitacao[1]:<25} | {solicitacao[2]:<15} | {solicitacao[3]:25} |{solicitacao[4]:<40} |{solicitacao[5]:<27} |")


def editar_solicitacoes_status():
    id_solocitacao = input('Digite o id da solicitação:')
    status = input("[1]Recebido\n[2]Em analise\n[3]Em andamento\n[4]Concluido\n[5]Cancelado \nEscolha:")
    dicionario = {'1':'Recebido','2':'Em análise','3':'Em andamento','4':'Concluido','5':'Cancelado'}

    cursor.execute('UPDATE solicitacoes SET status_solicitacao = ? WHERE id_solicitacao=?',(dicionario[status],id_solocitacao))

    conexao_db.commit()

def deletar_solicitacoes():
    
    id_solicitacao = input('Digite o id da solicitacao:')
    cursor.execute("DELETE FROM solicitacoes WHERE id_solicitacao = ?",(id_solicitacao,))
    conexao_db.commit()

# *********** RANK *************

def rank():
    while True:
        print(""" ****************************************************
        __________________ OPÇÕES __________________

        [v] .............. Voltar 
        [1] .............. SERVIÇO
        [2] .............. LOCAL"""
        )
        escolha = input("Escolha: ")

        if( escolha =='1'):
            rank_soliciação_servico()
        elif(escolha =='2'):
            rank_soliciação_local()
        elif escolha == 'v':
            break
        else:
            print("Escolha uma alternativa válida")

def rank_soliciação_servico():
    cursor.execute(""" SELECT nome_servico, COUNT(id_solicitacao) AS quantidade_soliciacoes FROM solicitacoes
                    INNER JOIN servicos on id_servico = fk_id_servico
                    GROUP BY nome_servico
                    ORDER BY quantidade_soliciacoes DESC""")

    resultados = cursor.fetchall()
    print(f"|{'serviço':<40}|{'Quantidade de solicitações':<40}|")
    print('-'*60)
    for resultado in resultados:
        servico = list(resultado)
        print(f'|{servico[0]:<40}|{servico[1]:<40}|')

def rank_soliciação_local():
    cursor.execute(""" SELECT endereco_solicitacao, COUNT(id_solicitacao) AS quantidade_soliciacoes FROM solicitacoes
                    INNER JOIN servicos on id_servico = fk_id_servico
                    GROUP BY endereco_solicitacao
                    ORDER BY quantidade_soliciacoes DESC""")

    resultados = cursor.fetchall()
    print(f"|{'local':<30}|{'Quantidade de solicitações':<40}|")
    print('-'*70)
    for resultado in resultados:
        servico = list(resultado)
        print(f'|{servico[0]:<30}|{servico[1]:<40}|')

if __name__ == '__main__':
    menu_administrador()