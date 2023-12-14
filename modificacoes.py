import sqlite3
import tela_administrador

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

# **** MODIFICAÇÕES *****

def modificacoes(servico,administrador,nome):
    # Insere os valores em modificação ( Como se fosse um histórico do adminstrador )
    cursor.execute(f"INSERT INTO modificacoes VALUES( NULL,?,?,?)",(servico,administrador,nome))

def listar_modificacao():
    # Lista modificação
    cursor.execute(""" SELECT id_modificacao,nome_administrador,email_administrador,nome_modificacoes FROM modificacoes 
                INNER JOIN administradores on fk_id_administrador = id_administrador 
                INNER JOIN servicos on fk_id_servico = id_servico """)
    resultados = cursor.fetchall()
    
    print(f"|{'ID':<3}|{'Nome ':<20}|{'Email do administrador':<30}|{'Modificação':<20}|")
    print('-'*70)
    for resultado in resultados:
        modificacao = list(resultado)
        print(f"|{modificacao[0]:<3}|{modificacao[1]:<20}|{modificacao[2]:<30}|{modificacao[3]:<20}|")
