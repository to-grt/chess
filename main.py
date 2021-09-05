from GameEngine import GameEngine

def main():
    print("WELCOME IM MY CHESS GAME  ---- by Theo GUEURET")
    myGame = GameEngine()
    #myGame.printAllPieces()
    #myGame.printAllSquares()
    #test de feature
    myGame.printBoard()
    for piece in myGame.board.pieces:
        print(piece.name + " : " + str(myGame.findMoves(piece)) )

main()
