from random import randrange, random
from old import funcs as f


class algoritimoGenetico():
    def __init__(self):
        self.itens = list()
        self.peso = int
        self.pontos = int
        self.porcentagem = float
        self.population = list()

# Inicialização dos individuos
populations = [[1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1]]
maxWeight = 30

itens = [
    {"name": "Saco de dormir", "weight": 15, "points": 15},
    {"name": "Corda", "weight": 3, "points": 7},
    {"name": "Canivete", "weight": 2, "points": 10},
    {"name": "Tocha", "weight": 5, "points": 5},
    {"name": "Garrafa", "weight": 9, "points": 8},
    {"name": "Comida", "weight": 20, "points": 17}
]

# Avaliação de cada individuo
def computeFitness(populations):
    itensMochila = list()
    for population in populations:
        pontosSobrevivencia = 0
        peso = 0
        Class = algoritimoGenetico()
        for index in range(len(population)):
            if population[index]:
                peso = peso + itens[index]['weight']
                pontosSobrevivencia = pontosSobrevivencia + itens[index]['points']
                Class.itens.append(itens[index])
        Class.population = population
        Class.peso = peso
        Class.pontos = pontosSobrevivencia
        itensMochila.append(Class)
    return itensMochila


# Escolhe o individuo melhor adaptado pelo método da roleta
def select(itensMochila, maxWeight):
    ItensLowWeight = list()
    somaFitnees = 0
    selecionados = []
    tour = 3

    # Adiciona na lista peso se o valor do fitnees peso é menor que 30kg
    for index in range(len(itensMochila)):
        if itensMochila[index].peso < maxWeight:
            ItensLowWeight.append(itensMochila[index])

    # Soma os pontos de sobrevivencia
    for index in range(len(ItensLowWeight)):
        somaFitnees += ItensLowWeight[index].pontos

    # Calcula a probabilidade de um cromossomo ser escolhido
    for index in range(len(ItensLowWeight)):
        valor = round(((ItensLowWeight[index].pontos / somaFitnees) * 100), 2)
        ItensLowWeight[index].porcentagem = valor

    # Gera um número aleatório no intervalo de 0 até a SomaFitnees
    # Busca os melhores 2 individuos usando o metodo da roleta
    limite = 0
    quant = 2
    while limite < quant:
        valorAleatorio = randrange(0, 100)
        print(valorAleatorio)
        soma = 0
        index = 0
        for index in range(len(ItensLowWeight)):
            if soma < valorAleatorio:
                soma += ItensLowWeight[index].porcentagem
            else:
                break
        selecionados.append(ItensLowWeight[index])
        limite += 1

    print("Peso " + str([item.peso for item in selecionados]) + "    Pontos de sobrevivencia  " + str(
        [item.pontos for item in selecionados]) +
          "    Soma Fitnees  " + str(somaFitnees) + "      Porcentagem " + str(
        [item.porcentagem for item in selecionados]))

    # Printa os itens escolhidos para levar na bolsa
    for item in selecionados:
        key = ""
        for keys in item.itens:
            key = key + ", " + list(keys.items())[0][1]
        print(key[2:])

    return selecionados

# Crossover multiplo
def crossover(itensSelecionados):
    populacao = []
    index = 0

    for index in range(len(itensSelecionados)):
        populacao.append(itensSelecionados[index].population)

    tamanhoMax = (len(itensSelecionados[index].population))
    corte1 = randrange(0, tamanhoMax)
    corte2 = randrange(0, tamanhoMax)

    print("População antes do crossover" + str(populacao))
    filho1 = itensSelecionados[0].population
    filho1[corte1], filho1[corte2] = filho1[corte2], filho1[corte1]

    filho2 = itensSelecionados[1].population
    filho2[corte1], filho2[corte2] = filho2[corte2], filho2[corte1]
    populacao.append(filho1)
    populacao.append(filho2)

    print("População depois do crossover" + str(populacao))
    return populacao


def showResult(selecionados):
    # Printa os itens selecionados
    print("Vamos levar na mochila os seguintes itens: ")
    key = ""
    for keys in selecionados[0].itens:
        key = key + ", " + list(keys.items())[0][1]
    print(key[2:])
    print("Qtd de loops: ", loops)


def mutation(selected, txReplace = 25):
    print("Antes mutação %s" % selected)

    valueRandom = randrange(0, (len(selected) - 1))
    selected[valueRandom] = f.changeBit(selected[valueRandom])

    print("Depois da mutação: %s" % selected)

    return selected



'''
Critérios de parada:
    - (1) predefinir o número absoluto de gerações que o algoritmo realizará,
    - (2) não há melhoras na população a x iterações,
    - (3) quando a avaliação de um indivíduo atingir um valor predefinido.
'''
# a partir da população e a pontuação de cada item, verifica se um elemento da população atinge
#   a faixa de valor estipulada para parada, que é 10% (padrão, variável txValid) do valor
#   máximo da pontuação com carga de 30kg.
def stopped(population, itens, txValid=10.0):
    maxValue = 39 # valor de pontuação max. obtido manualmente verificando as possibilidades
    selected = str()

    txValid = txValid / 100
    minPoints = maxValue / txValid

    # obtém pontuação de toda população #list()
    populationPoints = f.calcPointsPopulation(population, itens)

    # obtém maior valor da pontuação da população #int()
    biggerValue = f.biggerValue(populationPoints)

    # retorna o elemento selecionado com pontuação mais alta
    #   com o conteúdo da sua bolsa #list()
    for i in range(len(populationPoints)):
        if populationPoints[i] == biggerValue:
            selected = population[i]

    # @return True se o valor maior obtido é >= minimo de pontos requerido =
    #   pontuação_max * taxa %
    return (False, True) [biggerValue >= minPoints]





if __name__ == '__main__':
    stop = False
    itensMochila = computeFitness(populations)
    loops = 0

    while not stop:
        loops = loops +1
        print("\n\n###########################################\n"
              "###########################################\n\n")

        selecionados = select(itensMochila, maxWeight)
        populacao = crossover(selecionados)
        populacao[2] = mutation(populacao[2])

        itensMochila = computeFitness(populacao)

        print("\nPopulação atual: ", populacao)
        stop = stopped(populacao, itens)

    showResult(selecionados)



'''
1a - Geração 

A1 -> {1,0,0,1,1,0} 
A2 -> {0,0,1,1,1,0}
A3 -> {0,1,0,1,0,0}
A4 -> {0,1,1,0,0,1}

 +---------------+------+--------+----+----+----+----+
 | Item          | Peso | Pontos | A1 | A2 | A3 | A4 |  A5  |  A6
 +---------------+------+--------+----+----+----+----+
 | Saco de dormir| 15   |     15 | 1  |  0 | 0  | 0  |  1   |  0
 +---------------+------+--------+----+----+----+----+
 | Corda         | 3    |      7 | 0  |  0 | 1  | 1  |  1   |  1
 +---------------+------+--------+----+----+----+----+
 | Canivete      | 2    |     10 | 0  |  1 | 0  |  1 |  1   |  1
 +---------------+------+--------+----+----+----+----+
 | Tocha         | 5    |      5 | 1  |  1 |  1 |  0 |  1   |  1
 +---------------+------+--------+----+----+----+----+
 | Garrafa       | 9    |      8 | 1  |  1 |  0 |  0 |  0   |  0
 +---------------+------+--------+----+----+----+----+
 | Comida        | 20   |     17 | 0  |  0 |  0 |  1 |  0   |  1
 +---------------+------+--------+----+----+----+----+
                        | Peso   | 29 | 16 |  8 | 25 |  25  |  30
                        +--------+----+----+----+----+
                        | Pontos | 28 | 23 | 12 | 34 |  37  |  39
                        +--------+----+----+----+----+

'''
