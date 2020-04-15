import pygame


class score(object):
    highScore = 0 
    
    def __init__(self, gs, two_player):
        self.two_player = two_player
        self.player1_score = 1
        self.player2_score = None
        if two_player:
            self.player2_score = 1
        self.gs = gs
       
    def add_score(self, player):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1
            
    def draw(self):
        if self.two_player:
            text = self.gs.font.render(
                f"Player 1 Score: {self.player1_score}     Player 2 Score: {self.player2_score}", 1, self.gs.color.red)
        else:
            text = self.gs.font.render(f"Score: {self.player1_score}", 1, self.gs.color.red)
        self.gs.surface.blit(text, [0, self.gs.width + 5])


        # if len(score.score_count) > 0:
        #     if len(self.gs.snakes) > 1:
        #         text = self.gs.font.render("Player 1 Score: " + str(self.score_count[0]) + "     Player 2 Score: " + str(self.score_count[1]) , 1, self.gs.color.red)
        #     else:
        #         text = self.gs.font.render("Score: " + str(self.score_count[0]), 1, self.gs.color.red)
        # else:
        #     text = self.gs.font.render("Score: 1", 1, self.gs.color.green)
        # self.gs.surface.blit(text, [0 , self.game_height + 5])
