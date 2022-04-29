import pygame


class Interface:


    def __init__(self):

        self.window = None
        pygame.init()
        self.create_window()


    def add_text(self, text, color, position, size):

        didot = pygame.font.Font("fonts/didot.ttf", size)
        text_display = didot.render(text, True, color)
        textRect = text_display.get_rect()
        textRect.center = (position[0], position[1])
        self.window.blit(text_display, textRect)


    def create_window(self):

        # setting the window name
        pygame.display.set_caption('chess')

        # setting dimensions for the dimension of the monitor
        infos = pygame.display.Info()
        dimensions = (infos.current_w, infos.current_h)
        print("dimensions = ", dimensions)
        self.window = pygame.display.set_mode(dimensions)

        # setting a background color for now, grey backrgound because I like grey
        self.window.fill((100,100,100)) # grey

        # adding text
        my_color = (54, 1, 25)
        self.add_text('chess', my_color, (dimensions[0]*0.15, dimensions[1]*0.15), 200)
        self.add_text('play', my_color, (dimensions[0]*0.2, dimensions[1]*0.6), 90)
        self.add_text('exit', my_color, (dimensions[0]*0.2, dimensions[1]*0.8), 90)

        # add border
        pygame.draw.rect(self.window, (0,0,0), pygame.Rect(5, 5, dimensions[0]-10, dimensions[1]-10), 5)




        pygame.display.flip()


    def game_loop(self):

        infos = pygame.display.Info()
        dimensions = (infos.current_w, infos.current_h)

        truth = True
        while truth:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    truth = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if dimensions[0]*0.2 <= mouse[0] <= dimensions[0]*0.2+140 and dimensions[1]*0.6 <= mouse[1] <= dimensions[1]*0.6+40:
                        print("Launching a game haha")
                    if dimensions[0]*0.2 <= mouse[0] <= dimensions[0]*0.2+140 and dimensions[1]*0.8 <= mouse[1] <= dimensions[1]*0.8+40:
                        truth = False
        pygame.quit



fenetre = Interface()
fenetre.game_loop()