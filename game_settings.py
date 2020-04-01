import pygame
import cube
import snake

class game:


    def __init__(self):
        pygame.init()
        self.color = self.color()
        #Game Vars
        self.menu_width = 600
        self.width = 500
        self.row_width = 25
        self.rows = self.width//self.row_width
        self.banner_height = 100
        self.two_player = False
        self.playing = False
        self.on_menu = True
        self.snacks = []
        self.snakes = []
        self.obstacles = []
        #images
        self.exp_image= pygame.image.load('img/explosion3.png')

        # PyGame vars
        self.surface = pygame.display.set_mode((self.menu_width, self.menu_width + self.banner_height))
        self.font = pygame.font.SysFont("Arial", 32)
        self.clock = pygame.time.Clock()
        #snake vars
        self.s_colors = [self.color.purple ,self.color.red]  #[0] = player 1, [1] is player 2 etc
        self.s_starts = [(10,5), (10,15)]
        

    
    class color:
        def __init__(self):
            self.white = (255, 255, 255)
            self.black = (0, 0, 0)
            self.green = (0, 200, 30)
            self.dark_grey = (50, 50, 50)
            self.light_green =  (70, 255, 70)
            self.aqua= (10, 200, 150)
            self.blue = (0, 0, 255)
            self.purple = (125, 0, 125)
            self.red = (255, 0, 0)
            self.grey = (150, 150, 150)
            self.brown = (139, 69, 19)
       

                

    