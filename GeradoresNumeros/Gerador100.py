import random

def gerador1000():
    lista = random.sample(range(0,100), 100)
    lista.sort()
    return lista