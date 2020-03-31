import pygame

class score(object):
    
    def __init__(self, score,  gs):
        self.score_count = score
        self.game_height = gs.width
        self.gs = gs
       
    def update(self):
        self.score_count = self.score_count + 1

    def draw(self, text):
        text = self.gs.font.render(text + str(self.score_count), 1, (255, 255, 255))
        self.gs.surface.blit(text, [0 , self.game_height + 5])
                

    
