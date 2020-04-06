

def changeBit(bit):
    if bit == 1:
        bit = 0
    else:
        bit = 1
    return bit


def selectedPopulationInfo(selecteds):
    print("")



# Retorna pontuação de um elemento #int() passado como parametro;
def calculatePoints(element,  itens):
    itemPoint = pointByItem(itens)
    elementPoints = 0

#    print("\n\n\tElemento: ", element)

    # obtem qtd de bit do elemento
    for bit, item in zip( range(len(element)), range(len(itemPoint)) ):
        if element[bit] == 1:
            elementPoints = elementPoints + itemPoint[item]
        #for key in range(len(itens[2])):
         #   print("Calculando potuação de cada pessoa selecionada")

#    print("\tPontuação do elemento: ", elementPoints)
    return elementPoints



# varre a lista de dicionário e gera uma #list() com a pontuação
#   de cada item em ordem
def pointByItem(itens):
    pointByItem = list()

    for i in range(len(itens)):
        pointByItem.append(itens[i]['points'])

    return pointByItem



# calcula a pontuação de uma população #list() passada como parâmetro
#   retorna a potuação de cada elemento da população em #list()
def calcPointsPopulation(selecteds, itens):
    populationPoints = list()

    for index in range(len(selecteds)):
        populationPoints.append( calculatePoints(selecteds[index], itens) )

    print("\tPontuação da população eleita: ", populationPoints)
    return populationPoints


# procura o maior valor entre os valores #list() passado como parâmetro
#   @return o maior valor encontrado
def biggerValue(values):
    bigger = 0

    for index in range(len(values)):
        if values[index] > bigger:
            bigger = values[index]

    print("Bigger: ", bigger)

    return bigger