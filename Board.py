from Square import Square

class Board:

    def __init__(self):
        self.squares = self.createBoard()

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

    def printBoard(self):
        n = 25
        i = 0
        while i < n:
            print("-",end="")
            i+=1
        print("\n")
        for axe in self.squares:
            for square in axe:
                print("|", end="")
                if square.color == "black": print("B|",end="")
                else: print("W|", end="")
            print("")
            i = 0
            while i < n:
                print("-",end="")
                i+=1
            print("\n")

    def findSquare(self, pName):
        for axe in self.squares:
            for square in axe:
                if pName == square.name:
                    return self.squares[axe][square]
    
    def getSquare(self, pAbscissa, pOrdinate):
        return self.squares[pAbscissa-1][pOrdinate-1]
