from random import randrange


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
    while limite < 2:
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

    print("Peso " + str([item.peso for item in selecionados]) + "    Pontos de sobrevivencia  " + str([item.pontos for item in selecionados]) +
          "    Soma Fitnees  " + str(somaFitnees) + "      Porcentagem " + str([item.porcentagem for item in selecionados]))

    #Printa os itens selecionados
    for item in selecionados:
        key = ""
        for keys in item.itens:
            key = key + ", " + list(keys.items())[0][1]
        print(key[2:])

    #return selecionados

def croosover(pai1, pai2):
    pass


if __name__ == '__main__':
    itensMochila = computeFitness(populations)
    select(itensMochila, maxWeight)
    #croosover()
