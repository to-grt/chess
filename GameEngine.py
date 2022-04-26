from Board import Board
import os

class GameEngine:

    def __init__(self):

        self.board =    Board()

    def printAllSquares(self):

        for axe in self.board.squares:
            for square in axe:
                print( square.name, " : my infos are : \n", square.getInfos() )

    def printBoard(self):
        self.board.printBoard()

    def switch_column(self, pColumn):
        if pColumn == 'a': return 1
        elif pColumn == 'b': return 2
        elif pColumn == 'c': return 3
        elif pColumn == 'd': return 4
        elif pColumn == 'e': return 5
        elif pColumn == 'f': return 6
        elif pColumn == 'g': return 7
        elif pColumn == 'h': return 8
        else: return None

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def waitInput(self, pMessage):
        square = input(pMessage).lower()
        if len(square) != 2: return None
        column = square[0]
        column = self.switch_column(column)
        try:
            lign = int(square[1])
        except :
            return None
        if column == None or lign < 1 or lign > 8: return None
        final_square = self.board.getSquareFromCoords(column, lign)
        return final_square

    def findMoves(self, pPiece):
        return self.board.findMoves(pPiece, True)

    def changePlayer(self, pPlayer):
        if( pPlayer == "white"): return "black"
        else: return "white"

    def makeMove(self, pPiece, pSquare):
        self.board.makeMove(pPiece, pSquare)
        return

    def message(self, pString):
        print(pString)

    def gameLoop(self):

        end = False
        player = "white"

        while end != True:

            piece= None
            self.cls()
            self.printBoard()
            if player == "white": king = self.board.pieces[12]
            else : king = self.board.pieces[28]
            if self.board.kingInCheck(king, king.square): self.message('CHECKKK')
            self.message(player + " to move !")
            while piece == None:
                square = self.waitInput("Select the piece to move by selecting the square\n=> ")
                if square == None:
                    self.message("That square does not exist lol")
                    continue
                piece = self.board.pieceOnSquare(square)
                if piece == None: self.message("No piece on that square duh")
                if piece != None and piece.color != player:
                    self.message("You cannot select your opponent's pieces")
                    piece = None
            possibleMoves = self.findMoves(piece)
            print(possibleMoves)
            self.message("piece selected : " + piece.name)
            destination_square = self.waitInput("Where do yo want to move that piece ?\n=> ")
            print("destination_square : " + str(destination_square))
            if destination_square == None:
                print("you can't move there sir")
                continue
            print("now in sim")
            for possibleMove in possibleMoves:
                if piece.square.abscissa + possibleMove[0] == destination_square.abscissa and piece.square.ordinate + possibleMove[1] == destination_square.ordinate:
                    self.makeMove(piece, destination_square)
                    player = self.changePlayer(player)