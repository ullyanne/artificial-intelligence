class PriorityQueue():
    def __init__(self):
        self.queue = []
    
    def put(self, newNode):
        for index, node in enumerate(self.queue):
            if newNode.hCost <= node.hCost:
                self.queue.insert(index, newNode)
                return
        self.queue.append(newNode)

    def get(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

class Node():
    def __init__(self, station, line):
        self.station = station
        self.line = line
        self.visited = False
        self.adjList = {}
        self.cost = 0
        self.hCost = 0
        self.parent = None

class Graph():
    heuristic = [
        [0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32],
        [11, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24],
        [20, 9, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18],
        [27, 16, 7, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17],
        [40, 29, 20, 13, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20],
        [43, 32, 22, 16, 3, 0, 4, 23, 28, 33, 41, 30, 17, 20],
        [39, 28, 19, 12, 2, 4, 0, 22, 25, 29, 38, 28, 13, 17],
        [28, 19, 15, 13, 21, 23, 22, 0, 9, 22, 18, 7, 25, 30],
        [18, 11, 10, 13, 25, 28, 25, 9, 0, 13, 12, 12, 23, 28],
        [10, 4, 11, 18, 31, 33, 29, 22, 13, 0, 20, 27, 20, 23],
        [18, 17, 21, 26, 38, 41, 38, 18, 12, 20, 0, 15, 35, 39],
        [30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 0, 31, 37],
        [30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 0, 5],
        [32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5 , 0]
    ]

    def __init__(self, start, goal):
        self.nodes = {}
        self.start = start
        self.goal = goal
        self.totalCost = 0
        self.path = []
        self.intersec = None
    
    def addNode(self, station, lines):
        node = Node(station, lines)
        self.nodes[station] = node

    def addEdge(self, current, next):
        to = self.getNode(current)
        frm = self.getNode(next)
        to.adjList[frm] = 0
        frm.adjList[to] = 0
    
    def getNode(self, station):
        return self.nodes[station]

    def calcCost(self, current: Node, next: Node):
        h = self.heuristic[next.station -1][self.goal-1] *2
        c = self.totalCost + (self.heuristic[current.station -1][next.station -1] * 2)
        
        if self.changeLine(next):
            c = c + 4
        
        next.cost = c
        next.hCost = c + h

    def changeLine(self, next: Node):
        childIntersec = list(set(next.line).intersection(self.intersec))

        if len(childIntersec) == 0:
            return True
        return False


    def isGoal(self, node):
        if node.station == self.goal:
            return True
        return False
    
    def drawPath(self):
        current = self.getNode(self.goal)
        while current != None:
            self.path.append("E" + str(current.station))
            current = current.parent
        return self.path.reverse()

def aStar(graph: Graph):
    frontier = PriorityQueue()
    current = graph.getNode(graph.start)
    frontier.put(current)
    current.visited = True
    graph.intersec = current.line

    while frontier.size():
        current = frontier.get()
        graph.totalCost = current.cost
        
        if current.parent != None:
            graph.intersec = list(set(current.line).intersection(current.parent.line))

        if graph.isGoal(current):
            g.drawPath()
            break
        
        for next in current.adjList:
            if not next.visited:
                next.visited = True
                next.parent = current
                graph.calcCost(current, next)
                current.adjList[next] = next.cost
                frontier.put(next)
    return (graph.totalCost, graph.path)

print("""
                                  ___    _    
                                 |_ _|  / \   
                                  | |  / _ \  
                                  | | / ___ \ 
                                 |___/_/   \_\
                                              
""")
print("Problema do metrô de Paris\n")
print("Linhas operantes: Vermelha, Azul, Amarela e Verde")
print("Estações disponíves: E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, E13, E14\n")
start = int(input("Onde você está? E"))
goal = int(input("Para onde quer ir? E"))

g = Graph(start, goal)

g.addNode(1, ["B"])
g.addNode(2, ["B", "Y"])
g.addNode(3, ["B", "R"])
g.addNode(4, ["B", "G"])
g.addNode(5, ["B", "Y"])
g.addNode(6, ["B"])

g.addNode(10, ["Y"])
g.addNode(9, ["Y", "R"])
g.addNode(8, ["Y", "G"])
g.addNode(7, ["Y"])

g.addNode(11, ["R"])
g.addNode(13, ["R", "G"])

g.addNode(12, ["G"])
g.addNode(14, ["G"])


g.addEdge(1, 2)
g.addEdge(2, 10)
g.addEdge(2, 9)
g.addEdge(2, 3)
g.addEdge(3, 9)
g.addEdge(3, 4)
g.addEdge(3, 13)
g.addEdge(9, 11)
g.addEdge(9, 8)
g.addEdge(8, 12)
g.addEdge(8, 5)
g.addEdge(8, 4)
g.addEdge(4, 5)
g.addEdge(4, 13)
g.addEdge(5, 6)
g.addEdge(5, 7)
g.addEdge(13, 14)

data = aStar(g)

print(f"\nVocê está em E{g.start}")
print(f"O melhor trajeto para chegar ao destino E{g.goal} é:\n")
print(*data[1], sep=" -> ")
print(f"\nLevando aproximadamente {data[0]} minutos\n")