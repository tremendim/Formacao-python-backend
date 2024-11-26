
# Recebe a cidade de interesse da entrada do usuário e remove espaços em branco nas extremidades
cidade_interesse = input().strip()

# Recebe a lista de clientes da entrada do usuário e remove espaços em branco nas extremidades
clientes = input().strip()


# Função que filtra os clientes que moram na cidade especificada
def filtrar_clientes(lista_clientes, cidade_interesse):
    # Se a lista de clientes estiver vazia, retorna uma lista vazia
    if not lista_clientes:
        return []

    # Inicializa uma lista vazia para armazenar os clientes filtrados
    clientes_filtrados = []
    lista_clientes = clientes.split(';')


    for cliente in lista_clientes:
        nomeCliente, cidadeCliente = cliente.split(':')

        if cidadeCliente == cidade_interesse:
            clientes_filtrados.append( nomeCliente + "," + cidadeCliente )
        resultado = [tuple(item.split(',')) for item in clientes_filtrados]
            
    return resultado

# Processa a entrada de clientes para converter a string de clientes em uma lista de tuplas (nome, cidade)
lista_clientes = [tuple(cliente.split(':')) for cliente in clientes.split(';')]

# Imprime a lista de clientes filtrados
print(filtrar_clientes(lista_clientes, cidade_interesse))