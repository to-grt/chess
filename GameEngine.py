from Board import Board
from Piece import Piece

class GameEngine:

    def __init__(self):

        self.board =    Board()
        self.pieces =   self.createPieces()

    def createPieces(self):

        pieces = []
        #WHITE PIECES
        pieces.append( Piece("PW1", "pawn", "white", True, self.board.squares[0][1]) )
        pieces.append( Piece("PW2", "pawn", "white", True, self.board.squares[1][1]) )
        pieces.append( Piece("PW3", "pawn", "white", True, self.board.squares[2][1]) )
        pieces.append( Piece("PW4", "pawn", "white", True, self.board.squares[3][1]) )
        pieces.append( Piece("PW5", "pawn", "white", True, self.board.squares[4][1]) )
        pieces.append( Piece("PW6", "pawn", "white", True, self.board.squares[5][1]) )
        pieces.append( Piece("PW7", "pawn", "white", True, self.board.squares[6][1]) )
        pieces.append( Piece("PW8", "pawn", "white", True, self.board.squares[7][1]) )

        pieces.append( Piece("RW1", "rook",     "white", True, self.board.squares[0][0]) )
        pieces.append( Piece("KW1", "knight",   "white", True, self.board.squares[1][0]) )
        pieces.append( Piece("BW1", "bishop",   "white", True, self.board.squares[2][0]) )
        pieces.append( Piece("QW1", "queen",    "white", True, self.board.squares[3][0]) )
        pieces.append( Piece("KW1", "king",     "white", True, self.board.squares[4][0]) )
        pieces.append( Piece("BW2", "bishop",   "white", True, self.board.squares[5][0]) )
        pieces.append( Piece("KW2", "knight",   "white", True, self.board.squares[6][0]) )
        pieces.append( Piece("RW2", "rook",     "white", True, self.board.squares[7][0]) )

        #BLACK PIECES
        pieces.append( Piece("PB1", "pawn", "black", True, self.board.squares[0][6]) )
        pieces.append( Piece("PB2", "pawn", "black", True, self.board.squares[1][6]) )
        pieces.append( Piece("PB3", "pawn", "black", True, self.board.squares[2][6]) )
        pieces.append( Piece("PB4", "pawn", "black", True, self.board.squares[3][6]) )
        pieces.append( Piece("PB5", "pawn", "black", True, self.board.squares[4][6]) )
        pieces.append( Piece("PB6", "pawn", "black", True, self.board.squares[5][6]) )
        pieces.append( Piece("PB7", "pawn", "black", True, self.board.squares[6][6]) )
        pieces.append( Piece("PB8", "pawn", "black", True, self.board.squares[7][6]) )

        pieces.append( Piece("RB1", "rook",     "black", True, self.board.squares[0][7]) )
        pieces.append( Piece("KB1", "knight",   "black", True, self.board.squares[1][7]) )
        pieces.append( Piece("BB1", "bishop",   "black", True, self.board.squares[2][7]) )
        pieces.append( Piece("QB1", "queen",    "black", True, self.board.squares[3][7]) )
        pieces.append( Piece("KB1", "king",     "black", True, self.board.squares[4][7]) )
        pieces.append( Piece("BB2", "bishop",   "black", True, self.board.squares[5][7]) )
        pieces.append( Piece("KB2", "knight",   "black", True, self.board.squares[6][7]) )
        pieces.append( Piece("RB2", "rook",     "black", True, self.board.squares[7][7]) )
        return pieces

    def printAllPieces(self):

        for piece in self.pieces:
            print( piece.name, " : my infos are :\n", piece.getInfos() )

    def printAllSquares(self):

        for axe in self.board.squares:
            for square in axe:
                print( square.name, " : my infos are : \n", square.getInfos() )

    def printBoard(self):
        self.board.printBoard()

    def waitInput(self):
        return    

    def findMoves(self, pPiece):
        return self.board.findMoves(pPiece)

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

        while end != True:

            self.message(player + " to move !")
            self.message("Select the piece to move")
            piece = self.waitInput()
            possibleMoves = self.findMoves(piece)
            self.message("Where do yo want to move that piece ?")
            move = self.waitInput()
            self.makeMove(move, possibleMoves)
            player = self.changePlayer(player)

