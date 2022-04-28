from GameEngine import GameEngine


def main():

    myGame = GameEngine()
    play = True
    
    while play:
        play = myGame.gameLoop()
    print("Thanks for playing !")
main()