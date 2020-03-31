from random import randrange

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
    fitnessPeso = []
    fitnessPontosSobrevivencia = []
    for population in populations:
        pontosSobrevivencia = 0
        peso = 0
        for index in range(len(population)):
            if population[index]:
                peso = peso + itens[index]['weight']
                pontosSobrevivencia = pontosSobrevivencia + itens[index]['points']
        fitnessPeso.append(peso)
        fitnessPontosSobrevivencia.append(pontosSobrevivencia)
    return fitnessPeso, fitnessPontosSobrevivencia


# Escolhe o individuo melhor adaptado pelo método da roleta
def select(fitnessPeso, fitnessPontosSobrevivencia, maxWeight):
    peso=[]
    pontosSobrevivencia=[]
    somaFitnees = 0
    porcentagem = []
    selecionados = []
    tour = 3
    #Adiciona na lista peso se o valor do fitnees peso é menor que 30kg
    for index in range(len(fitnessPeso)):
        if fitnessPeso[index] < maxWeight:
            peso.append(fitnessPeso[index])
            pontosSobrevivencia.append(fitnessPontosSobrevivencia[index])

    #Soma os pontos de sobrevivencia
    for index in range(len(pontosSobrevivencia)):
        somaFitnees += pontosSobrevivencia[index]

    #Calcula a probabilidade de um cromossomo ser escolhido
    for index in range(len(pontosSobrevivencia)):
        valor = round((((pontosSobrevivencia[index])/somaFitnees)*100),2)
        porcentagem.append(valor)

    #Ordena em ordem crescente os valores em porcentagem dos pontos de sobrevivencia
    porcentagem.sort()

    #Gera um número aleatório no intervalo de 0 até a SomaFitnees
    #Busca os melhores 2 individuos usando o metodo da roleta
    limite = 0
    while limite < 2:
        valorAleatorio = randrange(0, 100)
        print(valorAleatorio)
        soma = 0
        index = 0
        for index in range(len(porcentagem)):
            if soma < valorAleatorio:
                soma += porcentagem[index]
            else:
                break
        selecionados.append(porcentagem[index])
        limite += 1

    print("Peso " + str(peso) + "    Pontos de sobrevivencia  " + str(pontosSobrevivencia) +
          "    Soma Fitnees  " + str(somaFitnees) + "      Porcentagem " + str(porcentagem))

    print("Os individuos selecionados foram   " + str(selecionados))

if __name__ == '__main__':
    fitnessPeso, fitnessPontosSobrevivencia = computeFitness(populations)
    select(fitnessPeso, fitnessPontosSobrevivencia, maxWeight)


