class Square:

    def __init__(self, pName, pAbscissa, pOrdinate, pColor, pIsOccuped):

        self.name =         pName
        self.abscissa =     pAbscissa
        self.ordinate =     pOrdinate
        self.color =        pColor
        self.isOccuped =    pIsOccuped
        self.nbPiece =      0

    def getInfos(self):
        infos = "my abscissa : " + str(self.abscissa) + "\nmy ordinate : " + str(self.ordinate) + "\nmy color : " + self.color + "\noccupated : " + str(self.isOccuped) + "\n\n"
        return infos