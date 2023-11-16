import random

def gerador1000():
    lista = random.sample(range(0,1000), 1000)
    lista.sort()
    return lista