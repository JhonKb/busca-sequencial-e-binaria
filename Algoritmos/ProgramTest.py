import time

from ListasNumeros import *
from BuscaBinaria import busca_binaria
from BuscaSequencial import busca_sequencial

# Matriz com as listas de números
lista = [cem(), dezMil(), umMilhao(), cemMilhoes()]

# Estabelecendo quantidade de sessões
for j in range(4):

    # Printando sessão atual
    print("Sessão "+str(j+1)+":")

    # Percorrendo as listas de números
    for i,numeros in enumerate(lista):

        # Iniciando rodada para cada lista 
        print("\nRodada " + str(i+1))
    
        # Alvo que deseja procurar
        alvo = float(input("Digite o número que deseja procurar:"))

        # Registrando tempo de busca
        tempoInicial = time.time()
        busca_binaria(numeros, alvo)
        tempoFinal = time.time()

        # Calculando tempo
        tempo_binaria = tempoFinal-tempoInicial

        # Registrando tempo de busca
        tempoInicial = time.time()
        busca_sequencial(numeros, alvo)
        tempoFinal = time.time()

        # Calculando tempo
        tempo_sequencial = tempoFinal-tempoInicial

        # Printando tempos finais da rodada
        print("Tempo Busca Binária: " + str(tempo_binaria))
        print("Tempo Busca Sequêncial: " + str(tempo_sequencial))


