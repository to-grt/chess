import pygame
from Button import Button


class Interface:


    def __init__(self):

        self.window = None
        self.list_buttons = []
        pygame.init()
        self.create_window()


    def reset_screen(self):
        self.list_buttons = []
        self.window.fill((0,0,0))
        pygame.display.flip()



    def add_text(self, text, color, position, size):

        didot = pygame.font.Font("fonts/didot.ttf", size)
        text_display = didot.render(text, True, color)
        textRect = text_display.get_rect()
        textRect.center = (position[0], position[1])
        self.window.blit(text_display, textRect)


    # note that here position is a tupple (x,y)
    def create_add_button(self, text, text_size, color_text, color_rect, position):

        button = Button(text, text_size, color_text, color_rect, position)
        self.list_buttons.append(button)
        self.add_button(button)
    

    def add_button(self, button):

        didot = pygame.font.Font("fonts/didot.ttf", button.text_size)
        text_display = didot.render(button.text, True, button.color_text)
        textRect = pygame.draw.rect(self.window, button.color_rect, pygame.Rect(button.position[0], button.position[1], button.width, button.height), 0)
        self.window.blit(text_display, textRect)


    def create_window(self):

        white = (250,250,250)
        black = (0,0,0)
        grey = (100,100,100)
        dark_grey = (50,50,50)
        my_color = (54, 1, 25) # great red


        # setting the window name
        pygame.display.set_caption('chess')

        # setting dimensions for the dimension of the monitor
        infos = pygame.display.Info()
        dimensions = (infos.current_w, infos.current_h)
        print("dimensions = ", dimensions)
        self.window = pygame.display.set_mode(dimensions)

        # setting a background color for now, grey backrgound because I like grey
        self.window.fill(grey)

        # adding text
        self.add_text('chess', my_color, (dimensions[0]*0.15, dimensions[1]*0.15), 200)
        #self.add_text('play', my_color, (dimensions[0]*0.2, dimensions[1]*0.6), 90)
        #self.add_text('exit', my_color, (dimensions[0]*0.2, dimensions[1]*0.8), 90)

        # add border
        pygame.draw.rect(self.window, (0,0,0), pygame.Rect(5, 5, dimensions[0]-10, dimensions[1]-10), 5)

        # add button
        self.create_add_button("play", 90, my_color, grey, (dimensions[0]*0.1, dimensions[1]*0.4))
        self.create_add_button("clear", 90, my_color, grey, (dimensions[0]*0.1, dimensions[1]*0.6))
        self.create_add_button("exit", 90, my_color, grey, (dimensions[0]*0.1, dimensions[1]*0.8))

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
                    for button in self.list_buttons:
                        if button.position[0] <= mouse[0] <= button.position[0]+button.width and button.position[1] <= mouse[1] <= button.position[1]+button.height:
                            if button.text=="play":
                                print("Launching a new game :)")
                            elif button.text=="clear":
                                print("Clearing the screen")
                                self.reset_screen()
                            elif button.text=="exit":
                                print("Exiting the game, bye bye")
                                truth=False
        pygame.quit



fenetre = Interface()
fenetre.game_loop()