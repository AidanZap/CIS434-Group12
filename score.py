import pygame

class score(object):
    _mode = 1
    score_count = []
    highScore = 0 
    
    def __init__(self, score,  gs):
        for s in gs.snakes:
            self.score_count.append(1)
        self.game_height = gs.width
        self.gs = gs
       
    def update(self, playerIndex):
        if len(self.score_count) <= 0:
            for s in self.gs.snakes:
                self.score_count.append(1)
        self.score_count[playerIndex] += 1

    def setGS(self, gs):
        self.game_height = gs.width
        self.gs = gs
        if len(gs.snakes) > 1:
            self._mode = 2
            for s in self.gs.snakes:
                self.score_count.append(1)
            
    def draw(self, text):
        if len(score.score_count) > 0:
            if len(self.gs.snakes) > 1:
                text = self.gs.font.render("Player 1 Score: " + str(self.score_count[0]) + "     Player 2 Score: " + str(self.score_count[1]) , 1, self.gs.color.red)
            else:
                text = self.gs.font.render("Score: " + str(self.score_count[0]), 1, self.gs.color.red)
        else:
            text = self.gs.font.render("Score: 1", 1, self.gs.color.green)
        self.gs.surface.blit(text, [0 , self.game_height + 5])
        
                

    
