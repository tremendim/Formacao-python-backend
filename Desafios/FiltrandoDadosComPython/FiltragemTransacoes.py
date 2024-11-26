from decimal import Decimal
# Recebe o valor limite como entrada do usuário e converte para float
limite = float(input())
# Recebe a string de transações como entrada do usuário
transacoes = input()

# Define a função para filtrar transações acima do limite especificado
def filtrar_transacoes_acima_do_limite(limite, transacoes):
    if not transacoes:
        return []

    transacoes_filtradas = []
    lista_transacoes = transacoes.split(';')
    
    # Itera sobre cada transação na lista de transações
    for transacao in lista_transacoes:
        id_transacao, valor_str = transacao.split(':')
        valor = float(valor_str)
        if valor >= limite:
            valor_formatado = f"{valor:.1f}" if valor % 1 == 0 else str(valor)
            transacoes_filtradas.append(id_transacao + ":" + valor_formatado)

    return transacoes_filtradas
    
# Imprime as transações com valores acima do limite
print(filtrar_transacoes_acima_do_limite(limite, transacoes))
