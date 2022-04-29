import pygame


class Interface:


    def __init__(self):

        pygame.init()
        self.create_window()

    
    def create_window(self):

        infos = pygame.display.Info()
        dimensions = (infos.current_w, infos.current_h)
        print("dimensions = ", dimensions)
        pygame.display.set_mode(dimensions)


    def game_loop(self):

        truth = True
        while truth:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    truth = False

        pygame.quit



fenetre = Interface()
fenetre.game_loop()