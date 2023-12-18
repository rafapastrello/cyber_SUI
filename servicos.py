import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_sui.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

# Obter os valores de serviço

def obter_servicos():
    cursor.execute(""" SELECT * FROM servicos """)

    resultados = cursor.fetchall()
    servicos = []
    for resultado in resultados:
        servico = list(resultado)
        servicos.append(servico)
    return servicos

# Listar os valores de serviço

def visualizar_servicos():
    ver_servico = obter_servicos()
    print('-'*93)
    print(f"| {'ID':<3} | {'nome do serviço':<40} | {'tipo de serviço':<40} |")
    print('-'*93)
    for servico in ver_servico:
        print(f"| {servico[0]:<3} | {servico[1]:<40} | {servico[2]:<40} |")
    print('-'*93)

def servicos():
    visualizar_servicos()
    id_servico = input('Digite o id do serviço que deseja:')

    return id_servico

if __name__ == '__main__':
    servicos()