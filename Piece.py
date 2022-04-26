from Square import Square

class Piece:

    def __init__(self, pName, pRole, pColor, pIsAlive, pSquare):
        self.name =     pName
        self.role =     pRole
        self.color =    pColor
        self.isAlive =  pIsAlive
        self.square =   pSquare
        self.nbMoves =  0
        self.movePattern = self.definePattern()
        self.square.isOccuped = True


    def pieceDies(self):

        self.square.isOccuped = False
        self.square.nbPiece -= 1
        self.isAlive = False
        self.square = None

    # only for the simulation of checks
    def pieceRessurect(self, pSquare):
        
        self.square = pSquare
        self.square.isOccuped = True
        self.square.nbPiece += 1
        self.isAlive = True

    
    # like pieceMoves but without the occupation changements and the number of move, only for simulation of checks and mate
    def pieceSimMoves(self, pNewSquare):
        #self.square.nbPiece -= 1   # might want to add that if problems with checks
        self.square = pNewSquare
        #self.square.nbPiece +=1
    

    def pieceMoves(self, pNewSquare):
        self.square.isOccuped = False
        self.square.nbPiece -= 1
        self.nbMoves += 1
        self.square = pNewSquare
        self.square.nbPiece +=1
        self.square.isOccuped = True

    
    def getInfos(self):
        infos = "my role : " + self.role + "\nmy color : " + self.color + "\nalive : " + str(self.isAlive) + "\nmy square : " + self.square.name + "\n\n"
        return infos


    def definePattern(self): # don't remember what that is probably useless now

        list = []

        if self.role == "pawn":
            list.append( (0,1) )
            if self.nbMoves == 0: list.append( (0,2) )
            return list

        elif self.role == "rook":
            return list

        elif self.role == "knight":
            return list

        elif self.role == "bishop":
            return list

        elif self.role == "queen":
            return list

        elif self.role == "king":
            return list  