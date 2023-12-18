import sqlite3
import solicitacoes

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('cyber_sui.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

def menu_cliente():
    """
    - Função para verificar se o cliente já está cadastrado ou não, se não estiver cadastrado, ele é redirecionado à função 'menu_cadastro_cliente';
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_cliente()
    """

    while True:
        menu = input("""
********************************************************
    _______________ CADASTRO CLIENTE _______________

        Digite [1] para cliente já cadastrado
        Digite [2] para cliente sem cadastro
        
******************************************************** 

>>> Digite a opção: """)
        if menu == '1':
            # Cliente informa que possui cadastro, então digita o CPF para verificarmos se é existente no banco de dados
            # Se o cliente for existente no banco de dados, ele recebe a mensagem "cadastrado como >Nome do Cliente<" e é redirecionado às funcionalidades de solicitações do usuário
            # Se não estiver cadastrado no banco de dados, ele recebe a mensagem de "CPF inexistente"
            cpf_cliente = input('\n>>> Informe seu CPF: ')

            cursor.execute('SELECT cpf_cliente FROM clientes WHERE cpf_cliente = ?', (cpf_cliente,))
            verifica_cpf_cliente = cursor.fetchone()  # Verifica se o CPF que o cliente informou é existente no DB

            id_cliente = obtem_id_cliente(cpf_cliente)

            cursor.execute('SELECT nome_cliente FROM clientes WHERE cpf_cliente = ?', (cpf_cliente,))
            nome_cliente_cadastrado = cursor.fetchone()  # Obtém o NOME do cliente, filtrado pelo CPF que foi informado pelo cliente

            # Se a variável 'verifica_cpf_cliente' estiver vazia, significa que o CPF que o cliente informou não existe no DB, e se existir algum valor nela, significa que o CPF é existente:
            if verifica_cpf_cliente is not None:
                # Se for diferente de vazia, ele é logado e redirecionado ao menu de solicitações
                print(f"""
- CADASTRADO COMO > {nome_cliente_cadastrado[0]} < !!! -
=-=-=-=-=-=-=-=-=-=-=-=-
>>> Seu ID é: {obtem_id_cliente(cpf_cliente)}
=-=-=-=-=-=-=-=-=-=-=-=-
""")
                menu_solicitacao_cliente(cpf_cliente)
            else:  # E se for vazia, imprime que o CPF é inexistente
                print('\n - CPF INEXISTENTE!!! - \n')
        elif menu == '2':
            # Ao informar que o cliente não possui cadastro, ele decide se quer ser cadastrado ou não
            opcao = input("""
***********************************************
    ____ DESEJA REALIZAR SEU CADASTRO? ____

            Digite [1] para SIM
            Digite [2] para NÃO
*********************************************** 

>>> Digite a opção: """)
            if opcao == '1':
                menu_cadastro_cliente()
            elif opcao == '2':
                menu_cliente()
            else:
                print('\n - OPÇÃO INVÁLIDA!!! - \n')
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')

def menu_cadastro_cliente():
    """
    - Função para cadastrar cliente no DB;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_cadastro_cliente()
    """

    while True:
        cpf_cliente = int(input('Digite seu CPF: '))
        email_cliente = input('Digite seu email: ')
        nome_cliente = input('Digite seu nome completo: ')
        telefone_cliente = int(input('Digite seu telefone: '))
        cursor.execute(" INSERT INTO clientes VALUES (null,?,?,?,?) ", (cpf_cliente, email_cliente, nome_cliente, telefone_cliente,))
        conexao_db.commit()
        print(f'\n - CLIENTE > {nome_cliente} < CADASTRADO!!! - \n')
        menu_cliente()

def menu_solicitacao_cliente(cpf_cliente):
    """
    - Função para o cliente receber as funcionalidades das solicitações do cliente;
    - Recebe 'cpf_cliente' como parâmetro;
    - Exemplo de uso:
    >>> menu_solicitacao_cliente(cpf_cliente)
    """
    solicitacoes.menu_solicitacao_cliente(cpf_cliente)

def obtem_id_cliente(cpf_cliente):
    """
    - Função para obter o ID do cliente cadastrado;
    - Recebe o parâmetro 'cpf_cliente', que é a variável onde é armazenado o CPF pelo qual iremos filtrar;
    - Se o parâmetro 'cpf_cliente' for vazio, logo, a variável 'id_cliente' deverá retornar vazia também;
    - Exemplo de uso:
    >>> obtem_id_cliente(cpf_cliente)
    """
    cursor.execute("SELECT id_cliente FROM clientes WHERE cpf_cliente = ?", (cpf_cliente,))
    id_cliente = cursor.fetchone()  # Obtém o ID do cliente, filtrado pelo CPF que foi informado pelo cliente
    return id_cliente[0]

if __name__ == '__main__':
    menu_cliente()
