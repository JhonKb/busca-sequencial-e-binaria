import random

def gerador1000():
    lista = random.sample(range(0,10000), 10000)
    lista.sort()
    return lista