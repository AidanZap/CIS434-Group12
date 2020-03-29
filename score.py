import pygame

class score(object):
    score_count = 0
    
    def __init__(self, score):
        self.score_count = score
       
    def update(self):
        self.score_count = self.score_count + 1

    def draw(self, surface):
        font = pygame.font.SysFont("Arial", 32)
        text = font.render("Score: "+ str(self.score_count), 1, (255, 255, 255))
        surface.blit(text, [0,0])
                

    
