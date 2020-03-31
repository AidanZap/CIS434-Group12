import pygame

class game(object):
    def __init__(self):
        pygame.init()
        #Game Vars
        width = 800
        row_width = 25
        rows = width//row_width
        banner_height = 50
        on_menu = True
        playing = False
        two_player = False

        # PyGame vars
        surface = pygame.display.set_mode((width, width + banner_height))
        font = pygame.font.SysFont("Arial", 32)
        clock = pygame.time.Clock()
        # Scores
        scr = score.score(1, width)
        h_scr = score.score(d['score'],width)

    class color(object):
        white = (255, 255, 255)
        black = (0, 0, 0)
        green = (0, 200, 30)
        dark_grey = (50, 50, 50)
        light_green =  (70, 255, 70)
        aqua= (10, 200, 150)
        blue = (0, 0, 255)
        purple = (125, 0, 125)
        red = (255, 0, 0)
        grey = (150, 150, 150)
        brown = (139, 69, 19)
       

                

    