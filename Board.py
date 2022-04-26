from Square import Square
from Piece import Piece

class Board:

    def __init__(self):

        self.squares = self.createBoard()
        self.pieces =   self.createPieces()


    #creates every square of the board cf Square.py
    def createBoard(self):

        squares = [[0 for x in range(8)] for y in range(8)]

        #column A
        squares[0][0] = ( Square("a1", 1, 1, "black", False) )
        squares[0][1] = ( Square("a2", 1, 2, "white", False) )
        squares[0][2] = ( Square("a3", 1, 3, "black", False) )
        squares[0][3] = ( Square("a4", 1, 4, "white", False) )
        squares[0][4] = ( Square("a5", 1, 5, "black", False) )
        squares[0][5] = ( Square("a6", 1, 6, "white", False) )
        squares[0][6] = ( Square("a7", 1, 7, "black", False) )
        squares[0][7] = ( Square("a8", 1, 8, "white", False) )

        #column B
        squares[1][0] = ( Square("b1", 2, 1, "white", False) )
        squares[1][1] = ( Square("b2", 2, 2, "black", False) )
        squares[1][2] = ( Square("b3", 2, 3, "white", False) )
        squares[1][3] = ( Square("b4", 2, 4, "black", False) )
        squares[1][4] = ( Square("b5", 2, 5, "white", False) )
        squares[1][5] = ( Square("b6", 2, 6, "black", False) )
        squares[1][6] = ( Square("b7", 2, 7, "white", False) )
        squares[1][7] = ( Square("b8", 2, 8, "black", False) )

        #column C
        squares[2][0] = ( Square("c1", 3, 1, "black", False) )
        squares[2][1] = ( Square("c2", 3, 2, "white", False) )
        squares[2][2] = ( Square("c3", 3, 3, "black", False) )
        squares[2][3] = ( Square("c4", 3, 4, "white", False) )
        squares[2][4] = ( Square("c5", 3, 5, "black", False) )
        squares[2][5] = ( Square("c6", 3, 6, "white", False) )
        squares[2][6] = ( Square("c7", 3, 7, "black", False) )
        squares[2][7] = ( Square("c8", 3, 8, "white", False) )

        #column D
        squares[3][0] = ( Square("d1", 4, 1, "white", False) )
        squares[3][1] = ( Square("d2", 4, 2, "black", False) )
        squares[3][2] = ( Square("d3", 4, 3, "white", False) )
        squares[3][3] = ( Square("d4", 4, 4, "black", False) )
        squares[3][4] = ( Square("d5", 4, 5, "white", False) )
        squares[3][5] = ( Square("d6", 4, 6, "black", False) )
        squares[3][6] = ( Square("d7", 4, 7, "white", False) )
        squares[3][7] = ( Square("d8", 4, 8, "black", False) )

        #column E
        squares[4][0] = ( Square("e1", 5, 1, "black", False) )
        squares[4][1] = ( Square("e2", 5, 2, "white", False) )
        squares[4][2] = ( Square("e3", 5, 3, "black", False) )
        squares[4][3] = ( Square("e4", 5, 4, "white", False) )
        squares[4][4] = ( Square("e5", 5, 5, "black", False) )
        squares[4][5] = ( Square("e6", 5, 6, "white", False) )
        squares[4][6] = ( Square("e7", 5, 7, "black", False) )
        squares[4][7] = ( Square("e8", 5, 8, "white", False) )

        #column F
        squares[5][0] = ( Square("f1", 6, 1, "white", False) )
        squares[5][1] = ( Square("f2", 6, 2, "black", False) )
        squares[5][2] = ( Square("f3", 6, 3, "white", False) )
        squares[5][3] = ( Square("f4", 6, 4, "black", False) )
        squares[5][4] = ( Square("f5", 6, 5, "white", False) )
        squares[5][5] = ( Square("f6", 6, 6, "black", False) )
        squares[5][6] = ( Square("f7", 6, 7, "white", False) )
        squares[5][7] = ( Square("f8", 6, 8, "black", False) )

        #column G
        squares[6][0] = ( Square("g1", 7, 1, "black", False) )
        squares[6][1] = ( Square("g2", 7, 2, "white", False) )
        squares[6][2] = ( Square("g3", 7, 3, "black", False) )
        squares[6][3] = ( Square("g4", 7, 4, "white", False) )
        squares[6][4] = ( Square("g5", 7, 5, "black", False) )
        squares[6][5] = ( Square("g6", 7, 6, "white", False) )
        squares[6][6] = ( Square("g7", 7, 7, "black", False) )
        squares[6][7] = ( Square("g8", 7, 8, "white", False) )

        #column H
        squares[7][0] = ( Square("h1", 8, 1, "white", False) )
        squares[7][1] = ( Square("h2", 8, 2, "black", False) )
        squares[7][2] = ( Square("h3", 8, 3, "white", False) )
        squares[7][3] = ( Square("h4", 8, 4, "black", False) )
        squares[7][4] = ( Square("h5", 8, 5, "white", False) )
        squares[7][5] = ( Square("h6", 8, 6, "black", False) )
        squares[7][6] = ( Square("h7", 8, 7, "white", False) )
        squares[7][7] = ( Square("h8", 8, 8, "black", False) )

        return squares


    #creates every piece od the board, cf Piece.py
    def createPieces(self):

        pieces = []
        #WHITE PIECES
        pieces.append( Piece("PW1", "pawn", "white", True, self.squares[0][1]) )
        pieces.append( Piece("PW2", "pawn", "white", True, self.squares[1][1]) )
        pieces.append( Piece("PW3", "pawn", "white", True, self.squares[2][1]) )
        pieces.append( Piece("PW4", "pawn", "white", True, self.squares[3][1]) )
        pieces.append( Piece("PW5", "pawn", "white", True, self.squares[4][1]) )
        pieces.append( Piece("PW6", "pawn", "white", True, self.squares[5][1]) )
        pieces.append( Piece("PW7", "pawn", "white", True, self.squares[6][1]) )
        pieces.append( Piece("PW8", "pawn", "white", True, self.squares[7][1]) )

        pieces.append( Piece("RW1", "rook",     "white", True, self.squares[0][0]) )
        pieces.append( Piece("CW1", "knight",   "white", True, self.squares[1][0]) )
        pieces.append( Piece("BW1", "bishop",   "white", True, self.squares[2][0]) )
        pieces.append( Piece("QW1", "queen",    "white", True, self.squares[3][0]) )
        pieces.append( Piece("KW1", "king",     "white", True, self.squares[4][0]) )
        pieces.append( Piece("BW2", "bishop",   "white", True, self.squares[5][0]) )
        pieces.append( Piece("CW2", "knight",   "white", True, self.squares[6][0]) )
        pieces.append( Piece("RW2", "rook",     "white", True, self.squares[7][0]) )

        #BLACK PIECES
        pieces.append( Piece("PB1", "pawn", "black", True, self.squares[0][6]) )
        pieces.append( Piece("PB2", "pawn", "black", True, self.squares[1][6]) )
        pieces.append( Piece("PB3", "pawn", "black", True, self.squares[2][6]) )
        pieces.append( Piece("PB4", "pawn", "black", True, self.squares[3][6]) )
        pieces.append( Piece("PB5", "pawn", "black", True, self.squares[4][6]) )
        pieces.append( Piece("PB6", "pawn", "black", True, self.squares[5][6]) )
        pieces.append( Piece("PB7", "pawn", "black", True, self.squares[6][6]) )
        pieces.append( Piece("PB8", "pawn", "black", True, self.squares[7][6]) )

        pieces.append( Piece("RB1", "rook",     "black", True, self.squares[0][7]) )
        pieces.append( Piece("CB1", "knight",   "black", True, self.squares[1][7]) )
        pieces.append( Piece("BB1", "bishop",   "black", True, self.squares[2][7]) )
        pieces.append( Piece("QB1", "queen",    "black", True, self.squares[3][7]) )
        pieces.append( Piece("KB1", "king",     "black", True, self.squares[4][7]) )
        pieces.append( Piece("BB2", "bishop",   "black", True, self.squares[5][7]) )
        pieces.append( Piece("CB2", "knight",   "black", True, self.squares[6][7]) )
        pieces.append( Piece("RB2", "rook",     "black", True, self.squares[7][7]) )
        return pieces


    #prints every piece of the board (dead or alive)
    def printAllPieces(self):

        for piece in self.pieces:
            print( piece.name, " : my infos are :\n", piece.getInfos() )


    def print_board_occupation(self):

        for row in self.squares:
            for square in row:
                print("square.name: ", square.name)
                print("square.occupation: ", square.isOccuped)


    #prints every quare of the board
    def printBoard(self):

        x = 0
        y = 7
        for y in range(8):
            for n in range(17):
                print("-",end="")
            print("")
            print("|", end="")
            for x in range(8):
                piece = self.pieceOnSquare(self.squares[x][7-y])
                if piece == None: print(" |", end="")
                else : print(piece.name[0] + "|", end="")
            print("")


    # make the designated move and destroy the enemy piece if there is one
    def makeMove(self, pPiece, pSquare):

        enemy = self.pieceOnSquare(pSquare)
        if enemy != None: enemy.pieceDies()
        pPiece.pieceMoves(pSquare)
        return


    #finds a square from a name
    def findSquare(self, pName):

        for axe in self.squares:
            for square in axe:
                if pName == square.name:
                    return square
    

    #returns a square from coordinates
    def getSquareFromCoords(self, pAbscissa, pOrdinate):

        return self.squares[pAbscissa-1][pOrdinate-1]


    #this function is quite useful, it allows to get a new square from a specific square, a x deviation and a y deviation for exemple:
    #  input =>  square A1, 1, 1   output => square b2
    #return None otherwise
    def getSquareFromSquare(self, pSquare, pX, pY):

        x = pSquare.abscissa
        y = pSquare.ordinate
        xFinal = x + pX
        yFinal = y + pY
        if( xFinal <= 0 or xFinal > 8 or yFinal <= 0 or yFinal > 8): return None
        else: return self.getSquareFromCoords(xFinal, yFinal)


    #returns a the piece present on the given square, otherwise, returns None
    def pieceOnSquare(self, pSquare):

        for piece in self.pieces:
            if piece.square == pSquare: return piece
        return None


    def moveInduceCheck(self, pPiece, pObservedSquare):

        memSquare = pPiece.square
        pPiece.pieceSimMoves(pObservedSquare)
        check = self.kingInCheck(pPiece.color)
        pPiece.pieceSimMoves(memSquare)
        if check: return True
        return False


    def kingInCheck(self, color):

        if color == "white": king = self.pieces[12]                            
        else : king = self.pieces[28]

        for piece in self.pieces:
            if not piece.isAlive: continue
            if piece.color != color and piece.square.nbPiece == 1:
                moves = self.findMoves(piece, False)
                for move in moves:
                    if piece.square.abscissa + move[0] == king.square.abscissa and piece.square.ordinate + move[1] == king.square.ordinate:
                        return True
        return False


    #Finds the moves for a given piece, checkIfCheck diferenciate we check if the move include own-king check
    def findMoves(self, pPiece, checkIfCheck):
       
        if pPiece.role == "pawn":
            return self.pawnMoves(pPiece, checkIfCheck)

        elif pPiece.role == "rook":
            return self.rookMoves(pPiece, checkIfCheck)

        elif pPiece.role == "knight":
            return self.knightMoves(pPiece, checkIfCheck)

        elif pPiece.role == "bishop":
            return self.bishopMoves(pPiece, checkIfCheck)

        elif pPiece.role == "queen":
            return self.queenMoves(pPiece, checkIfCheck)

        elif pPiece.role == "king":
            return self.kingMoves(pPiece, checkIfCheck)

    # as a reminder: definition of checkObservedSquare: 
    # 
    # checkObservedSquare(self, pPiece, pObservedSquare, pCanEat, pNeedsNoPreviousMove, pCheckIfCheck):
    # linked to findMoves(self, pPiece)
    def pawnMoves(self, pPawn, pCheckIfCheck):

        if pPawn.color == "white": signColor = 1
        else: signColor = -1
        movesList = []

        observedSquare = self.getSquareFromSquare(pPawn.square, 0, signColor*1)
        if observedSquare != None:
            if self.checkObservedSquare(pPawn, observedSquare, False, False, pCheckIfCheck)[0]: movesList.append( (0,signColor*1) )

        if movesList != []: #because a pawn can only moves 2 square if the first square ahead of it is available
            observedSquare = self.getSquareFromSquare(pPawn.square, 0, signColor*2)
            if observedSquare != None:
                if self.checkObservedSquare(pPawn, observedSquare, False, True, pCheckIfCheck)[0]: movesList.append( (0,signColor*2) )

        observedSquare = self.getSquareFromSquare(pPawn.square, -1, signColor*1)
        if observedSquare != None:
            if self.checkObservedSquare(pPawn, observedSquare, True, False, pCheckIfCheck)[0] and observedSquare.isOccuped: movesList.append( (-1,signColor*1) )

        observedSquare = self.getSquareFromSquare(pPawn.square, 1, signColor*1)
        if observedSquare != None:
            if self.checkObservedSquare(pPawn, observedSquare, True, False, pCheckIfCheck)[0] and observedSquare.isOccuped: movesList.append( (1,signColor*1) )

        return movesList


    #linked to findMoves(self, pPiece)
    def rookMoves(self, pRook, pCheckIfCheck):

        movesList = []

        compteur = 1
        while(compteur < 8): # I defined the limit to 8 even if it might overflow because once 1 square is overflowing, the loop stops
            observedSquare = self.getSquareFromSquare(pRook.square, compteur, 0)
            if observedSquare != None:
                checkObservedSquare = self.checkObservedSquare(pRook, observedSquare, True, False, pCheckIfCheck)
                if checkObservedSquare[0]: movesList.append( (compteur,0) )
                if not checkObservedSquare[1]: break
            compteur+=1

        compteur = 1
        while(compteur < 8): # I defined the limit to 8 even if it might overflow because once 1 square is overflowing, the loop stops
            observedSquare = self.getSquareFromSquare(pRook.square, -compteur, 0)
            if observedSquare != None:
                checkObservedSquare = self.checkObservedSquare(pRook, observedSquare, True, False, pCheckIfCheck)
                if checkObservedSquare[0]: movesList.append( (-compteur,0) )
                if not checkObservedSquare[1]: break
            compteur+=1

        compteur = 1
        while(compteur < 8): # I defined the limit to 8 even if it might overflow because once 1 square is overflowing, the loop stops
            observedSquare = self.getSquareFromSquare(pRook.square, 0, compteur)
            if observedSquare != None:
                checkObservedSquare = self.checkObservedSquare(pRook, observedSquare, True, False, pCheckIfCheck)
                if checkObservedSquare[0]: movesList.append( (0,compteur) )
                if not checkObservedSquare[1]: break
            compteur+=1

        compteur = 1
        while(compteur < 8): # I defined the limit to 8 even if it might overflow because once 1 square is overflowing, the loop stops
            observedSquare = self.getSquareFromSquare(pRook.square, 0, -compteur)
            if observedSquare != None:
                checkObservedSquare = self.checkObservedSquare(pRook, observedSquare, True, False, pCheckIfCheck)
                if checkObservedSquare[0]: movesList.append( (0,-compteur) )
                if not checkObservedSquare[1]: break
            compteur+=1

        return movesList


    #linked to findMoves(self, pPiece)
    def knightMoves(self, pKnight, pCheckIfCheck):

        movesList = []

        observedSquare = self.getSquareFromSquare(pKnight.square, 1, 2)
        if observedSquare != None:
            if self.checkObservedSquare(pKnight, observedSquare, True, False, pCheckIfCheck)[0]: movesList.append( (1,2) )

        observedSquare = self.getSquareFromSquare(pKnight.square, 2, 1)
        if observedSquare != None:
            if self.checkObservedSquare(pKnight, observedSquare, True, False, pCheckIfCheck)[0]: movesList.append( (2,1) )

        observedSquare = self.getSquareFromSquare(pKnight.square, 2, -1)
        if observedSquare != None:
            if self.checkObservedSquare(pKnight, observedSquare, True, False, pCheckIfCheck)[0]: movesList.append( (2,-1) )

        observedSquare = self.getSquareFromSquare(pKnight.square, 1, -2)
        if observedSquare != None:
            if self.checkObservedSquare(pKnight, observedSquare, True, False, pCheckIfCheck)[0]: movesList.append( (1,-2) )

        observedSquare = self.getSquareFromSquare(pKnight.square, -1, -2)
        if observedSquare != None:
            if self.checkObservedSquare(pKnight, observedSquare, True, False, pCheckIfCheck)[0]: movesList.append( (-1,-2) )

        observedSquare = self.getSquareFromSquare(pKnight.square, -2, -1)
        if observedSquare != None:
            if self.checkObservedSquare(pKnight, observedSquare, True, False, pCheckIfCheck)[0]: movesList.append( (-2,-1) )

        observedSquare = self.getSquareFromSquare(pKnight.square, -2, 1)
        if observedSquare != None:
            if self.checkObservedSquare(pKnight, observedSquare, True, False, pCheckIfCheck)[0]: movesList.append( (-2,1) )

        observedSquare = self.getSquareFromSquare(pKnight.square, -1, 2)
        if observedSquare != None:
            if self.checkObservedSquare(pKnight, observedSquare, True, False, pCheckIfCheck)[0]: movesList.append( (-1,2) )

        return movesList


    #linked to findMoves(self, pPiece)
    def bishopMoves(self, pBishop, pCheckIfCheck):

        movesList = []

        compteur = 1
        while(compteur < 8): #I defined the limit to 8 even if it might overflow because once 1 square is overflowing, the loop stops
            observedSquare = self.getSquareFromSquare(pBishop.square, compteur, compteur)
            if observedSquare != None:
                checkObservedSquare = self.checkObservedSquare(pBishop, observedSquare, True, False, pCheckIfCheck)
                if checkObservedSquare[0]: movesList.append( (compteur,compteur) )
                if not checkObservedSquare[1]: break
            compteur+=1

        compteur = 1
        while(compteur < 8): #I defined the limit to 8 even if it might overflow because once 1 square is overflowing, the loop stops
            observedSquare = self.getSquareFromSquare(pBishop.square, compteur, -compteur)
            if observedSquare != None:
                checkObservedSquare = self.checkObservedSquare(pBishop, observedSquare, True, False, pCheckIfCheck)
                if checkObservedSquare[0]: movesList.append( (compteur,-compteur) )
                if not checkObservedSquare[1]: break
            compteur+=1

        compteur = 1
        while(compteur < 8): #I defined the limit to 8 even if it might overflow because once 1 square is overflowing, the loop stops
            observedSquare = self.getSquareFromSquare(pBishop.square, -compteur, compteur)
            if observedSquare != None:
                checkObservedSquare = self.checkObservedSquare(pBishop, observedSquare, True, False, pCheckIfCheck)
                if checkObservedSquare[0]: movesList.append( (-compteur,compteur) )
                if not checkObservedSquare[1]: break
            compteur+=1

        compteur = 1
        while(compteur < 8): #I defined the limit to 8 even if it might overflow because once 1 square is overflowing, the loop stops
            observedSquare = self.getSquareFromSquare(pBishop.square, -compteur, -compteur)
            if observedSquare != None:
                checkObservedSquare = self.checkObservedSquare(pBishop, observedSquare, True, False, pCheckIfCheck)
                if checkObservedSquare[0]: movesList.append( (-compteur,-compteur) )
                if not checkObservedSquare[1]: break
            compteur+=1

        return movesList


    #linked to findMoves(self, pPiece)
    def queenMoves(self, pQueen, pCheckIfCheck):

        movesList = self.rookMoves(pQueen, pCheckIfCheck) + self.bishopMoves(pQueen, pCheckIfCheck)
        return movesList


    #linked to findMoves(self, pPiece)
    def kingMoves(self, pKing, pCheckIfCheck):

        movesList = []
        list_three = [-1, 0, 1]
        for index_1 in list_three:
            for index_2 in list_three:
                if index_1 != 0 or index_2 != 0:
                    observedSquare = self.getSquareFromSquare(pKing.square, index_1, index_2)
                    if observedSquare != None:
                        if self.checkObservedSquare(pKing, observedSquare, False, False, pCheckIfCheck)[0]: movesList.append((index_1, index_2))
        return movesList

    #this function returns a boolean, true if the piece can go the observedSquare, False otherwise. 
    #pCanEat define the capability of the piece to 'eat' another piece on the given observeSquare.
    #pNeedsNoPreviousMove is used for certain piece : when it's on true, we check if the piece has move already (king's castling or pawn rush)
    #returns 2 boolean, #1 can go on that square, #2 can continue his way?
    #  #2 is used for the loop, for example a bishop, is there is a piece taht blocks it, it can not continue his way, loop will then stops
    def checkObservedSquare(self, pPiece, pObservedSquare, pCanEat, pNeedsNoPreviousMove, pCheckIfCheck):
        if pCheckIfCheck: 
            if self.moveInduceCheck(pPiece, pObservedSquare): return (False, True)
        if pNeedsNoPreviousMove and pPiece.nbMoves != 0: return (False,False)  #for king's castle and pawn's rush
        pieceObservedSquare = self.pieceOnSquare(pObservedSquare)
        if pieceObservedSquare == None: return (True,True)     #check if there a piece on the square, if no, can move
        if pieceObservedSquare.color == pPiece.color or not pCanEat: return (False, False)      #check if the piece on the square has the same color or if the pieceObserved can eat, if so, can't move
        else: return (True,False)     #here, the piece can eat, and the observedPiece hasnt the same color