import sqlite3
import modificacoes

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

# ----- TELA ADMINISTRADOR -----

def cadastrar_administrador():
    global id_usuario

    opcao = input("""
********************************************************
    ____________ CADASTRO ADMINISTRADOR ____________

        Digite [1] para administrador já cadastrado
        Digite [2] para administrador sem cadastro
        
******************************************************** 

>>> Digite a opção: """)

    while( opcao!= '1' and opcao!='2' ):
        opcao = input("Escolha a alternativa correta:")

    while True:
        if (opcao =='1'):
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
        elif opcao == '2':
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

def editar_administrador():
    item = input("[1]nome\n[2]email\n[3]telefone\n O que deseja mudar:")
    mudar = input('para que dejesa mudar:')
    dicionario = {'1':'nome_administrador','2':'email_administrador','3':'telefone_administrador'}
    cursor.execute(f'UPDATE administradores SET {dicionario[item]} =? where id_administrador=?',(mudar,id_usuario))
    conexao_db.commit()


# **** MODIFICAÇÕES *****

def modificacoes_administrador():
    modificacoes.modificacoes(servico,administrador,nome)

def listar_modificacao_administrador():
    modificacoes.listar_modificacao()


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

    print(f"|{'ID':<3}|{'nome do serviço':<20}|{'tipo de serviço':<20}|")
    print('-'*43)

    for servico in ver_servico:
        print(f"|{servico[0]:<3}|{servico[1]:<20}|{servico[2]:<20}|")


# ***** SOLICITAÇÃO *****
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

def rank_soliciação_servico():
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

def rank_soliciação_local():
    cursor.execute(""" SELECT endereco_solicitacao, COUNT(id_solicitacao)  AS quandidade_soliciacoes FROM solicitacao
                    INNER JOIN servicos on id_servico = fk_id_servico
                    GROUP BY endereco_solicitacao
                    ORDER BY endereco_solicitacao DESC""")

    resultados = cursor.fetchall()
    print(f"|{'local':<20}|{'Quantidade de solicitações':<30}|")
    print('-'*50)
    for resultado in resultados:
        servico = list(resultado)
        print(f'|{servico[0]:<20}|{servico[1]:<30}|')

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
    [1] .............. Visualizar solicitações
    [2] .............. Visualizar serviços
    [3] .............. Criar serviço
    [4] .............. Editar serviço
    [5] .............. Deletar serviço
    [6] .............. Ver histórico     
    [7] .............. Modificar cadastro  
    [8] .............. Ver rank                  
****************************************************

>>> Digite a opção: """)
        if opcao == 'v':
            print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
            break
        elif opcao == '1':
            print('\n - VISUALIZAR SOLICITAÇÕES - \n')
            visualizar_solicitacoes_administrador()
        elif opcao == '2':
            print('\n - VISUALIZAR SERVIÇOS - \n')
            visualizar_servico_administrador()
        elif opcao == '3':
            print('\n - CRIAR SERVIÇO - \n')
            cadastrar_servico_administrador()
        elif opcao == '4':
            print('\n - EDITAR SERVIÇO - \n')
            editar_servico_administrador()
        elif opcao == '5':
            print('\n - DELETAR SERVIÇO - \n')
            excluir_servico_administrador()
        elif opcao == '6':
            print('\n - VISUALIZAR HISTÓRICO - \n')
            ...
        elif opcao == '7':
            print('\n - MODIFICAR PERFIL - \n')
            editar_administrador()
        elif opcao == '8':
            print('\n - RANKING SHOW - \n')
            rank()
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

if __name__ == '__main__':
    menu_administrador()