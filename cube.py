import pygame


class cube(object):

    def __init__(self, gs,  start, dirnx = 1, dirny = 0, color = (255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        self.rows = gs.rows
        self.w = gs.width
        self.gs = gs
    
    def setGS(self, gs):
        self.gs = gs
        self.rows = gs.rows
        self.w = gs.width
        print(gs.rows)


    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(self.gs.surface, self.color, (i*dis + 1,j*dis + 1, dis-2, dis-2))

        if eyes:
            center = dis//2
            radius = 3
            circleMiddle = (i*dis + center-radius, j* dis + 8)
            circleMiddle2 = (i*dis + dis-radius * 2, j* dis + 8)
            pygame.draw.circle(self.gs.surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(self.gs.surface, (0,0,0), circleMiddle2, radius)
