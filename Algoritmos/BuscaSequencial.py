# Método de busca sequencial
# O método percorre a lista comumente do inicio ao fim
def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1