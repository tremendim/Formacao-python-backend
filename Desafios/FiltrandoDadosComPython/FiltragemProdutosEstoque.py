




entrada = input()

# Função responsável por filtrar produtos em estoque
def filtrar_produtos_em_estoque(entrada):
    if not entrada:
        return []
        
    produtos = entrada.split(';')

    produtos_disponiveis = []
    
    for produto_str in produtos:
        nome, preco, quantidade = produto_str.split(":")
        quantidadeInt = int(quantidade)
        if quantidadeInt > 0:
            produtos_disponiveis.append(produto_str)


    return produtos_disponiveis

# Imprime a lista de produtos em estoque
print(filtrar_produtos_em_estoque(entrada))