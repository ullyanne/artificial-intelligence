# LEFT: (3, 3, 1); RIGHT: (0, 0, -1). 
# Primeiro elemento = canibais
# Segundo = missionários
# Terceiro = barco (-1 está presente no lado, 1 não está presente no lado)

class Node():
    moves = [(1, 0, 1), (2, 0, 1), (1, 1, 1), (0, 1, 1), (0, 2, 1)]
    solutions = []

    def __init__(self, parent, leftState, rightState, steps):
        self.DFSqueue = []
        self.parent = parent
        self.children = []
        self.steps = steps
        self.left = leftState
        self.right = rightState

    def appendDFSQueue(self, child):
        self.DFSqueue.append(child)
    
    def addChild(self, child):
        self.children.append(child)
    
    def isValid(self):
        if self.left[0] < 0 or self.left[1] < 0 or self.right[0] < 0 or self.right[1] < 0 or self.left[0] > 3 or self.left[1] > 3 or self.right[0] > 3 or self.right[1] > 3 or self.isRepeated() or self.isGameOver():
            return False
        return True

    def isRepeated(self):
        currentParent = self.parent
        while currentParent != "NULL":
            if self.left == currentParent.left and self.right == currentParent.right:
                return True
            currentParent = currentParent.parent
        return False
    
    def isGameOver(self):
        leftDiff = self.left[0] - self.left[1]
        rightDiff = self.right[0] - self.right[1]
        
        if (leftDiff > 0 and leftDiff < self.left[0]) or (rightDiff > 0 and rightDiff < self.right[0]):
            return True
        return False

    def isSolution(self):
        if self.left == (0, 0, -1) and self.right == (3, 3, 1):
            return True
        return False

def path(node):
    if node.parent == "NULL":
        return
    path(node.parent)
    print(f"{node.left} - {node.right}")

def DFS(state):
    state.appendDFSQueue(state)
    while len(state.DFSqueue) > 0:
        for move in state.moves:
            left = ( (state.left[0] + (move[0] * -state.left[2])), (state.left[1] + (move[1]) * -state.left[2]), (-state.left[2]))
            right = ( (state.right[0] + (move[0]* state.left[2])), (state.right[1] + (move[1]* state.left[2])), (state.left[2]))

            child = Node(state, left, right, state.steps+1)

            if child.isValid():
                state.addChild(child)
                
                if child.isSolution():
                    child.solutions.append(child)
                else:
                    state.appendDFSQueue(state)
                    DFS(child)
                    state.DFSqueue.pop()
        state.DFSqueue.pop()

if __name__ == "__main__":
    left = (3, 3, 1)
    right = (0, 0, -1)
    root = Node("NULL", left, right, 0)
    print("""
                                  ___    _    
                                 |_ _|  / \   
                                  | |  / _ \  
                                  | | / ___ \ 
                                 |___/_/   \_\
                                              
    """)
    print("Problema dos missionários e canibais")
    print("O estado inicial é", root.left, root.right)

    DFS(root)

    print(f"\nForam encontradas {len(root.solutions)} soluções!\n")

    for index, solution in enumerate(root.solutions, start=1):
        print(f"Solução {index}")
        print(f"Custo: {solution.steps}")
        print("(canibais, missionários, barco)")
        print("ESQUERDO - DIREITO")
        path(solution)
        print("\n")



