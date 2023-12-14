import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_solucoes.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

# Obter os valores de serviço

def obter_servicos():
    cursor.execute(""" SELECT * FROM servico """)

    resultados = cursor.fetchall()
    servicos = []
    for resultado in resultados:
        servico = list(resultado)
        servicos.append(servico)
    return servicos


# Listar os valores de serviço

def visualizar_servicos():
    ver_servico = obter_servicos()
    print(f"|{'ID':<3}|{'nome do serviço':<20}|{'tipo de serviço':<20}|")
    print('-'*43)
    for servico in ver_servico:
        print(f"|{servico[0]:<3}|{servico[1]:<20}|{servico[2]:<20}|")

def servicos():
    visualizar_servicos()
    print('-'*43)
    id_servico = input('Digite o id do serviço que deseja:')

    return id_servico

if __name__ == '__main__':
    servicos()