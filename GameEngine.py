from Board import Board

class GameEngine:

    def __init__(self):

        self.board =    Board()

    def printAllSquares(self):

        for axe in self.board.squares:
            for square in axe:
                print( square.name, " : my infos are : \n", square.getInfos() )

    def printBoard(self):
        self.board.printBoard()

    def waitInput(self):
        return    

    def findMoves(self, pPiece):
        return self.board.findMoves(pPiece, True)

    def changePlayer(self, pPlayer):
        if( pPlayer == "white"): return "black"
        else: return "white"

    def makeMove(self, mMove):
        return

    def message(pString):
        print(pString)

    def turn(self):

        end = False
        player = "white"
        piece = None

        while end != True:

            self.message(player + " to move !")
            self.message("Select the piece to move")

            while piece == None:
                piece = self.waitInput()

            possibleMoves = self.findMoves(piece)
            self.message("Where do yo want to move that piece ?")
            move = self.waitInput()
            self.makeMove(move, possibleMoves)
            player = self.changePlayer(player)

