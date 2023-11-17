import random

# Obtem uma lista ordenda de cem numeros
def cem():
    lista = random.sample(range(0,100), 100)
    lista.sort()
    return lista

# Obtem uma lista ordenada de dez mil numeros
def dezMil():
    lista = random.sample(range(0,10000), 10000)
    lista.sort()
    return lista

# Obtem uma lista ordenada de um milhão de números
def umMilhao():
    lista = random.sample(range(0,1000000), 1000000)
    lista.sort()
    return lista

# Obtem uma lista ordenada de cem milhões de números
def cemMilhoes():
    lista = random.sample(range(0,100000000), 100000000)
    lista.sort()
    return lista