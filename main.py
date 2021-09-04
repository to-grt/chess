from GameEngine import GameEngine

def main():
    print("WELCOME IM MY CHESS GAME  ---- by Theo GUEURET")
    myGame = GameEngine()
    #myGame.printAllPieces()
    #myGame.printAllSquares()
    #test de feature
    myGame.printBoard()
    piece0 = myGame.board.pieces[0]
    piece1 = myGame.board.pieces[1]
    piece7 = myGame.board.pieces[7]
    piece8 = myGame.board.pieces[8]
    piece9 = myGame.board.pieces[9]
    piece10 = myGame.board.pieces[10]
    piece11 = myGame.board.pieces[11]
    piece0.nbMoves += 1
    print(piece0.name + " : " + str(myGame.findMoves(piece0)) )
    print(piece1.name + " : " + str(myGame.findMoves(piece1)) )
    print(piece7.name + " : " + str(myGame.findMoves(piece7)) )
    print(piece8.name + " : " + str(myGame.findMoves(piece8)) )
    print(piece9.name + " : " + str(myGame.findMoves(piece9)) )
    print(piece10.name + " : " + str(myGame.findMoves(piece10)) )
    print(piece11.name + " : " + str(myGame.findMoves(piece11)) )

main()
