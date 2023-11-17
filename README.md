# Busca Sequencial e Binária

Tarefa apresentada em sala de aula na disciplina de Estruturas de Dados

## 📊 Objetivo

A presente tarefa tem como objetivo analisar as diferenças de usabilidade entre a busca binária e a busca sequencial em estruturas de dados.

##

## 📃 Descrição da Tarefa

Você recebe uma lista de números inteiros ordenada em ordem crescente. Sua tarefa é implementar tanto a
busca sequencial quanto a busca binária para encontrar a posição de um determinado número na lista, ou
indicar se o número não está presente.

- Implemente uma função chamada busca_sequencial(lista, alvo) que realiza uma busca sequencial
na lista e retorna a posição do alvo ou -1 se não estiver presente.
- Implemente uma função chamada busca_binaria(lista, alvo) que realiza uma busca binária na lista e
retorna a posição do alvo ou -1 se não estiver presente. A lista deve estar ordenada para que a
busca binária funcione corretamente.
- Crie uma lista de números inteiros ordenados para testar suas implementações.
- Realize testes com diferentes casos, incluindo casos em que o número alvo está presente e casos
em que não está.
- Compare a eficiência das duas abordagens em termos de número de comparações realizadas.

##

## 🔍 Análise

### Metodologia

- Para realização desta atividade, foram divididas quatro sessões de testes.
- Cada sessão representa um números alvo diferente.
- Os alvos procurados são, respectivamente: primeiro elemento da lista, elemento central (no centro da lista), ultimo elemento da lista e elemento não existente na lista.
- Cada sessão é executada obtendo o resultado de quatro listas com tamanhos diferentes:
    1. Primeira lista com números entre 0 a 100 (cem).
    1. Segunda lista com números entre 0 e 10000 (dez mil).
    1. Terceira lista com números entre 0 e 1000000 (um milhão).
    1. Quata lista com números entre 0 e 100000000 (cem milhões).

### Algoritmos

A tabela a seguir apresenta os algoritmos utilizados nesta atividade:

| Nome | Local |
|-|-|
| Busca Sequencial | [BuscaSequencial.py](/Algoritmos/BuscaSequencial.py) |
| Busca Binária | [BuscaBinaria.py](/Algoritmos/BuscaBinaria.py) |
| Listas de Números | [ListasNumeros.py](/Algoritmos/ListasNumeros.py) |
| Algoritmo Principal | [ProgramTest.py](/Algoritmos/ProgramTest.py) |


## 📊 Resultados:

Diante dos dados apresentados, foram obtidos os resultados presentees nas tabelas a seguir:

- Sessão 1 (Primeiro elemento):

| Tipo de busca | Tempo Lista 1 | Lista 2 | Lista 3 | Lista 4 |
|-|-|-|-|-|-|-|
| Busca Binária | 0.0 | 0.006020307540893555 | 0.016322851181030273 | 0.0 |
| Busca Sequancial | 0.0 | 0.0 | 0.0 | 0.0 |

- Sessão 2 (Elemento central):

| Tipo de busca | Tempo Lista 1 | Lista 2 | Lista 3 | Lista 4 |
|-|-|-|-|-|-|-|
| Busca Binária | 0.0 | 0.015421867370605469 | 0.0 | 0.0 |
| Busca Sequancial | 0.0 | 0.0 | 0.08406305313110352 | 3.22605562210083 |

- Sessão 3 (Último elemento):

| Tipo de busca | Tempo Lista 1 | Lista 2 | Lista 3 | Lista 4 |
|-|-|-|-|-|-|-|
| Busca Binária | 0.0 | 0.0 | 0.01541447639465332 | 0.0 |
| Busca Sequancial | 0.0 | 0.0 | 0.09178566932678223 | 10.211485385894775 |

- Sessão 4 (Elemento Inexistente):

| Tipo de busca | Tempo Lista 1 | Lista 2 | Lista 3 | Lista 4 |
|-|-|-|-|-|-|-|
| Busca Binária | 0.0 | 0.0 | 0.0 | 0.0 |
| Busca Sequancial | 0.0 | 0.0 | 0.04962515830993652 | 6.514232397079468 |

## ✅ Conclusão



##

## 📚 Referências


##
