from random import randint
from copy import deepcopy

citiesDist = [
    [0, 30, 84, 56, -1, -1, -1, 75, -1, 80],
    [30, 0, 65, -1, -1, -1, 70, -1, -1, 40],
    [84, 65, 0, 74, 52, 55, -1, 60, 143, 48],
    [56, -1, 74, 0, 135, -1, -1, 20, -1, -1],
    [-1, -1, 52, 135, 0, 70, -1, 122, 98, 80],
    [70, -1, 55, -1, 70, 0, 63, -1, 82, 35],
    [-1, 70, -1, -1, -1, 63, 0, -1, 120, 57],
    [75, -1, 135, 20, 122, -1, -1, 0, -1, -1],
    [-1, -1, 143, -1, 98, 82, 120, -1, 0, -1],
    [80, 40, 48, -1, 80, 35, 57, -1, -1, 0]
]

cities = {
    0: "C1", 1: "C2", 2: "C3", 3: "C4", 4: "C5", 5: "C6", 6: "C7", 7: "C8", 8: "C9", 9: "C10"
}

def printPath(solution):
    path = []
    for city in solution:
        path.append(cities[city])
    print(*path, sep=" -> ")

def genStartPath(nCities):
    path = []
    cities = [i for i in range(nCities)]

    for i in range(nCities):
        randomCity = cities[randint(0, len(cities) - 1)]
        path.append(randomCity)
        cities.remove(randomCity)
    path.insert(0, path[nCities-1])
    return path

def isValid(path):
    for i in range(0, len(path)-1):
        dist = citiesDist[path[i]][path[i+1]]
        if dist == -1:
            return False
    return True

def calcPathCost(path: list, citiesDist: list):
    cost = 0
    for i in range(0, len(path)-1):
        dist = citiesDist[path[i]][path[i+1]]
        cost += dist
    return cost

def genChildren(path: list):
    children = []
    for i in range(0, len(path)-1):
        for j in range(i + 1, len(path)-1):
            child = deepcopy(path[:-1])
            child[i], child[j] = path[j], path[i]
            child.insert(0, child[len(child)-1])
            if isValid(child):
                children.append(child)
    return children

def pickBest(children: list, path: list, pathCost, citiesDist: list):
    best, bestCost = path, pathCost
    if children:
        for child in children:
            childCost = calcPathCost(child, citiesDist)
            if childCost < bestCost:
                best = child
                bestCost = childCost
    return best, bestCost

def hillClimbing(citiesDist: list, nCities):
    startingPoint = 0
    localMin = None
    localMinCost = None
    #Gerando os pais
    while startingPoint < 1000:
        path = genStartPath(nCities)
        pathCost = calcPathCost(path, citiesDist)
        #Escolhendo o melhor filho
        newPath, newPathCost = pickBest(genChildren(path), path, pathCost, citiesDist)

        #Procurando o mínimo local de cada pai
        while newPathCost < pathCost:
            path, pathCost = newPath, newPathCost
            if localMin == None or localMinCost > pathCost:
                localMin, localMinCost = path, pathCost
            newPath, newPathCost = pickBest(genChildren(path), path, pathCost, citiesDist)
        startingPoint += 1
    return (localMin, localMinCost)

print("""
                                  ___    _    
                                 |_ _|  / \   
                                  | |  / _ \  
                                  | | / ___ \ 
                                 |___/_/   \_\
                                              
""")
print("Problema do caixeiro viajante")

solution, solutionCost = hillClimbing(citiesDist, len(citiesDist))

print("\nO caixeiro pode seguir a rota\n")
printPath(solution)
print(f"\npercorrendo um total de {solutionCost}km")