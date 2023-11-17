import time

from ListasNumeros import *
from BuscaBinaria import busca_binaria
from BuscaSequencial import busca_sequencial

lista = [cem(), dezMil(), umMilhao(), cemMilhoes()]

for j in range(4):
    print("Sessão "+str(j+1)+":")
    for i,numeros in enumerate(lista):
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

        print("Tempo Busca Binária: " + str(tempo_binaria))
        print("Tempo Busca Sequêncial: " + str(tempo_sequencial))


