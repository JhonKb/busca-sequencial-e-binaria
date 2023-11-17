# Método da busca binária
# O método percorre a lista fragmentando-a em partes menores
# Posicionando-se no centro de cada fragmento e comparando sua igualdade
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor_meio = lista[meio]

        if valor_meio == alvo:
            return meio
        elif valor_meio < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1