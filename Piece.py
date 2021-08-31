from Square import Square

class Piece:

    def __init__(self, pName, pRole, pColor, pIsAlive, pSquare):

        self.name =     pName
        self.role =     pRole
        self.color =    pColor
        self.isAlive =  pIsAlive
        self.square =   pSquare
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
        self.square = pNewSquare
        self.squareIsOccuped()
    
    def getInfos(self):
        infos = "my role : " + self.role + "\nmy color : " + self.color + "\nalive : " + str(self.isAlive) + "\nmy square : " + self.square.name + "\n\n"
        return infos



    