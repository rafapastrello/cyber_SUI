import tela_administrador
import tela_cliente

def menu_principal():
    """
    Função responsável por exibir um menu de opções para o sistema da Cyber Soluções.

    - A função entra em um loop, exibindo o menu e aguardando a entrada do usuário;
    - Com base na escolha do usuário, a função direciona para a função correspondente ou encerra o programa;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_principal()
    """

    while True:
        opcao = input("""
            ------------- CYBER SOLUÇÕES ---------------
             ******************************************
               ----------- MENU PRINCIPAL -----------
    
                [s] ............... ENCERRAR SISTEMA
                [1] ........................ Cliente
                [2] .................. Administrador

            ********************************************
                
            >>> Digite seu estado(cliente/administrador): """)

        if opcao == 's':
            print('\n - PROGRAMA ENCERRADO COM SUCESSO! - \n')
            break
        elif opcao == '1':
            print('\n - TELA CLIENTE - \n')
            tela_cliente.menu_cliente()
        elif opcao == '2':
            print('\n - TELA ADMINISTRADOR - \n')
            tela_administrador.menu_administrador()
        else:
            print('\n - OPÇÃO INVÁLIDA! - \n')

if __name__ == '__main__':
    menu_principal()
