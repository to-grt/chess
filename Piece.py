from Square import Square

class Piece:

    def __init__(self, pName, pRole, pColor, pIsAlive, pSquare):

        self.name =     pName
        self.role =     pRole
        self.color =    pColor
        self.isAlive =  pIsAlive
        self.square =   pSquare
        self.nbMoves =  0
        self.squareIsOccuped()

    def squareIsOccuped(self):      # when a piece is moved
        self.square.isOccuped = True
    
    def squareIsUnnoccuped(self):   # when a piece leave a square
        self.square.isOccuped = False

    def pieceDies(self):
        self.squareIsUnnoccuped()
        self.isAlive = False
        self.square = None
    
    def pieceMoves(self, pNewSquare):
        self.squareIsUnnoccuped()
        self.nbMoves += 1
        self.square = pNewSquare
        self.squareIsOccuped()
    
    def getInfos(self):
        infos = "my role : " + self.role + "\nmy color : " + self.color + "\nalive : " + str(self.isAlive) + "\nmy square : " + self.square.name + "\n\n"
        return infos

    def getPossibleMoves(self):

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




    