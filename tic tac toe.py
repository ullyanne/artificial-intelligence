from abc import ABC, abstractmethod
import random, math, time

class JogoDaVelha():
    def __init__(self):
        self.board = [' ' for i in range(0, 9)]
        self.winner = None
        self.maxPlayer = None
        self.minPlayer = None
    def printBoard(self):
        print("\n", end="")
        for position in range(0, 3):
            print("|", self.board[position * 3], "|", self.board[position * 3 + 1], "|", self.board[position * 3 + 2], "|")
        print("\n", end="")
    def isValidMove(self, move):
        if self.board[move] == " ":
            return True
        return False
    def makeAMove(self, move, player):
        self.board[move] = player.player
        if self.isWinner(player.player):
            self.winner = player
    def isWinner(self, player):
        for i in range(0, 3):
            horizontal = [self.board[i * 3], self.board[i * 3 + 1], self.board[i * 3 + 2]]
            vertical = [self.board[i + 0 * 3], self.board[i + 1 * 3], self.board[i + 2 * 3]]
            if all(position == player for position in horizontal):
                return True 
            if all(position == player for position in vertical):
                return True
        princDiag = self.board[slice(2, 7, 2)] 
        secDiag = self.board[slice(0, 9, 4)]
        if all(position == player for position in princDiag):
            return True
        if all(position == player for position in secDiag):
            return True
        return False
    def isDraw(self):
        if self.movesLeft()[1] > 0:
            return False
        return True
    def movesLeft(self):
        moves = []
        for index, position in enumerate(self.board):
            if self.isValidMove(index):
                moves.append(index)
        return moves, len(moves)
    def undo(self, move):
        self.board[move] = ' '
        self.winner = None
    def startGame(self, human, pc):
        player = random.choice([human, pc])
        self.maxPlayer = pc
        self.minPlayer = human
        self.printBoard()
        while self.movesLeft()[1] > 0:
            player.play(self)
            if self.winner:
                time.sleep(0.6)
                if self.winner == human:
                    print("Parabéns! Você venceu o jogo da velha. \N{crown}")
                else:
                    print("O PC venceu o jogo da velha!! \N{alien monster}")
                break
            if self.isDraw():
                print("Deu velha!")
                break
            player = pc if player == human else human

class Player(ABC):
    def __init__(self, player):
        self.player = player

    def play(self, game: JogoDaVelha):
        print(self)
        time.sleep(0.7)
        move = self.chooseMove(game)
        if game.isValidMove(move):
            game.makeAMove(move, self)
        else:
            print("Jogada inválida!!\n")
            self.play(game)
        game.printBoard()
    
    @abstractmethod
    def chooseMove(game):
        pass

class PC(Player):
    def __str__(self):
        return "Turno do PC"
    def minimax(self, game: JogoDaVelha, isMax):
        if game.winner == game.maxPlayer:
            return game.movesLeft()[1] + 1
        elif game.winner == game.minPlayer:
            return -(game.movesLeft()[1] + 1)
        if game.isDraw():
            return 0
        
        scores = []
        for move in game.movesLeft()[0]:
            game.makeAMove(move, game.maxPlayer if isMax else game.minPlayer)
            score = self.minimax(game, not isMax)
            scores.append(score)
            game.undo(move)
        return max(scores) if isMax else min(scores)
    def chooseMove(self, game: JogoDaVelha):
        if game.movesLeft()[1] == 9:
            return random.randint(0, 8)
        
        bestScore = -math.inf
        bestMove = None
        for move in game.movesLeft()[0]:
            game.makeAMove(move, game.maxPlayer)
            score = self.minimax(game, False)
            game.undo(move)
            if score > bestScore:
                bestMove = move
                bestScore = score
        return bestMove

class Human(Player):
    def __str__(self):
        return "Seu turno"

    def chooseMove(self, game):
        move = int(input("Onde você quer jogar? [0...8]\n"))
        return move

print("""
                                  ___    _    
                                 |_ _|  / \   
                                  | |  / _ \  
                                  | | / ___ \ 
                                 |___/_/   \_\
                                              
""")
print("Jogo da Velha \U0001F60C \N{joystick}  VS \N{alien monster}\n")
game = JogoDaVelha()
humanPlay = input("Escolha entre x e o\n").upper()
human = Human(humanPlay)
pc = PC("X") if humanPlay == "O" else PC("O")
game.startGame(human, pc)