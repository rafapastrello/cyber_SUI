#servicos_requeridos#
def requisitar_servico():
    lista_servicos = ['Vazamentos', 'Esgotos a céu aberto', 'Buracos nas vias', 'Fiação elétrica', 'Lixo acumulado',
                        'Falta de internet', 'Poda de árvores']
    print("Bem-vindo! Por favor, escolha um dos serviços disponíveis:")
    for index, servico in enumerate(lista_servicos, start=1):
        print(f"{index}. {servico}")

    escolha = int(input("Digite o número correspondente ao serviço desejado: "))
    if 1 <= escolha <= len(lista_servicos):
        servico_escolhido = lista_servicos[escolha - 1]
        print(f"Você escolheu o serviço de {servico_escolhido}.")
        endereco = input("Por favor, digite o endereço onde o serviço é necessário: ")
        return (servico_escolhido, endereco)
    else:
        print("Escolha inválida. Por favor, tente novamente.")
        return None, None

# Lista para armazenar os serviços escolhidos junto com os endereços
lista_servicos_enderecos = []

# Loop para requisitar os serviços até que o usuário decida parar
while True:
    servico, endereco = requisitar_servico()
    if servico and endereco:
        lista_servicos_enderecos.append((servico, endereco))
    continuar = input("Deseja requisitar outro serviço? (s/n): ")
    if continuar.lower() != 's':
        break

print("Lista de serviços requisitados:")
for servico, endereco in lista_servicos_enderecos:
    print(f"Serviço: {servico}, Endereço: {endereco}")