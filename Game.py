from Board import Board
from Piece import Piece

class Game:

    def __init__(self):

        self.board =    Board()
        self.pieces =   self.createPieces()

    def createPieces(self):

        pieces = []
        pieces.append( Piece("PB1", "pion", "white", True, self.board.squares[0][1]) )
        pieces.append( Piece("PB2", "pion", "white", True, self.board.squares[1][1]) )
        pieces.append( Piece("PB3", "pion", "white", True, self.board.squares[2][1]) )
        pieces.append( Piece("PB4", "pion", "white", True, self.board.squares[3][1]) )
        pieces.append( Piece("PB5", "pion", "white", True, self.board.squares[4][1]) )
        pieces.append( Piece("PB6", "pion", "white", True, self.board.squares[5][1]) )
        pieces.append( Piece("PB7", "pion", "white", True, self.board.squares[6][1]) )
        pieces.append( Piece("PB8", "pion", "white", True, self.board.squares[7][1]) )
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