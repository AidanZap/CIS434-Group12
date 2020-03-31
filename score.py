import pygame

class score(object):
    score_count = 1
    
    def __init__(self, score, game_height):
        self.score_count = score
        self.game_height = game_height
       
    def update(self):
        self.score_count = self.score_count + 1

    def draw(self, surface, text):
        font = pygame.font.SysFont("Arial", 32)
        text = font.render(text + str(self.score_count), 1, (255, 255, 255))
        surface.blit(text, [0 , self.game_height + 5])
                

    
