from random import randrange, random

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
    ItensLowWeight = itensMochila
    somaFitnees = 0
    selecionados = []
    tour = 2

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
    while limite < tour:
        valorAleatorio = randrange(0, 100)
        print(valorAleatorio)
        soma = 0
        index = 0
        for index in range(len(ItensLowWeight)):
            if soma < valorAleatorio:
                soma += ItensLowWeight[index].porcentagem
            else:
                break
        if len(ItensLowWeight) > index:
            selecionados.append(ItensLowWeight[index])
        limite += 1

    print("Peso " + str([item.peso for item in selecionados]) + "    Pontos de sobrevivencia  " + str(
        [item.pontos for item in selecionados]) +
          "    Soma Fitnees  " + str(somaFitnees) + "      Porcentagem " + str(
        [item.porcentagem for item in selecionados]))

    # Printa os itens selecionados
    for item in selecionados:
        key = ""
        for keys in item.itens:
            key = key + ", " + list(keys.items())[0][1]
        print(key[2:])

    return selecionados


# Crossover multiplo: define um ponto de corte no elemento e faz a trocar/inversão para gerar filho
def crossover(itensSelecionados):
    populacao = []
    index = 0
    childrens = list()

    for index in range(len(itensSelecionados)):
        populacao.append(itensSelecionados[index].population)

    lenMax = len(itensSelecionados[0].population)
    cut = randrange(1, lenMax)

    print("Corte em: ", cut)
    print("População antes do crossover" + str(populacao))
    children = list()

    # varre elemento por elemento
    for i in range(len(populacao)):
        bitBeforeCut = list() # armazena bits de [i] até o corte
        bitAfterCut = list() # armazena bits de [i] após o corte

        # varre bit a bit do elemento
        for j in range(lenMax):
            # armazena bits até o indice definido como corte
            if ( j < cut ):
                bitBeforeCut.append(populacao[i][j])
            else:
                bitAfterCut.append(populacao[i][j])

        # armazena sequencialmente bits anteriores e
        #   posteriores ao corte
        children.append(bitBeforeCut)
        children.append(bitAfterCut)

    # faz o cross efetivamente
    #   merge do elemento 1 (bitAfterCut) com elemento 2 (bitBeforeCut)
    index = 0
    while ( index < len(populacao)*2 ):
        childrens.append(children[index] + children[ (len(children)-1) - index])

        index += 2

    # adiciona os filhos a população
    populacao.append(childrens[0])
    populacao.append(childrens[1])

    print("População depois do crossover" + str(populacao))
    return populacao


def stopFunc(itensMochila):
    minPoints = 39
    biggerValue = 0
    itensSelect = None
    for item in itensMochila:
        if item.pontos > biggerValue and item.peso <=30:
            biggerValue = item.pontos
            itensSelect = item

    return biggerValue >= minPoints, itensSelect

def showResult(selecionados):
    # Printa os itens selecionados
    print("Vamos levar na mochila os seguintes itens: ")
    key = ""
    for keys in selecionados.itens:
        key = key + ", " + list(keys.items())[0][1]
    print(key[2:])

    print("Peso  " + str(selecionados.peso))
    print("Pontos  " + str(selecionados.pontos))

    print("itens" + str(selecionados.itens))
    print("\nQuantidade de loops: ", loops)

def mutation(selected, txReplace = 25):
    def changeBit(bit):
        if bit == 1:
            bit = 0
        else:
            bit = 1
        return bit

    print("Antes mutação %s" % selected)

    valueRandom = randrange(0, (len(selected) - 1))
    selected[valueRandom] = changeBit(selected[valueRandom])
    if 1 in selected:
        print("Depois da mutação: %s" % selected)
        return selected

    return mutation(selected, txReplace)

if __name__ == '__main__':
    stop = False
    itensMochila = computeFitness(populations)
    loops = 0

    while not stop:
        loops = loops + 1
        print("-----------------------------------------------------------------")
        selecionados = select(itensMochila, maxWeight)
        populacao = crossover(selecionados)
        populacao[2] = mutation(populacao[2])
        itensMochila = computeFitness(populacao)
        stop, itensSelect = stopFunc(itensMochila)

    print("-----------------------------------------------------------------")
    print("\nResposta do algoritmo Genetico\n")
    showResult(itensSelect)


'''
1a - Geração 

A1 -> {1,0,0,1,1,0} 
A2 -> {0,0,1,1,1,0}
A3 -> {0,1,0,1,0,0}
A4 -> {0,1,1,0,0,1}

 +---------------+------+--------+----+----+----+----+
 | Item          | Peso | Pontos | A1 | A2 | A3 | A4 |
 +---------------+------+--------+----+----+----+----+
 | Saco de dormir| 15   |     15 | 1  |  0 | 0  | 0  |
 +---------------+------+--------+----+----+----+----+
 | Corda         | 3    |      7 | 0  |  0 | 1  | 1  |
 +---------------+------+--------+----+----+----+----+
 | Canivete      | 2    |     10 | 0  |  1 | 0  |  1 |
 +---------------+------+--------+----+----+----+----+
 | Tocha         | 5    |      5 | 1  |  1 |  1 |  0 |
 +---------------+------+--------+----+----+----+----+
 | Garrafa       | 9    |      8 | 1  |  1 |  0 |  0 |
 +---------------+------+--------+----+----+----+----+
 | Comida        | 20   |     17 | 0  |  0 |  0 |  1 |
 +---------------+------+--------+----+----+----+----+
                        | Peso   | 29 |    |    |    |
                        +--------+----+----+----+----+
                        | Pontos | 28 | 23 | 12 | 34 |
                        +--------+----+----+----+----+

'''
