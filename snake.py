import pygame
import cube


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos, rows, width):
        self.color = color
        self.head = cube.cube(pos, color = self.color, rows = rows, width = width)
        self.body.append(self.head)
        self.dirnx = 1
        self.dirny = 0
        self.rows = rows
        self.width = width

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT] and self.dirnx != 1:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]     

            if keys[pygame.K_RIGHT] and self.dirnx != -1:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]     

            if keys[pygame.K_UP] and self.dirny != 1:
                self.dirny = -1
                self.dirnx = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]       

            if keys[pygame.K_DOWN] and self.dirny != -1:
                self.dirny = 1
                self.dirnx = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            break                

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if c.pos[0] < 0: c.pos = (c.rows-1, c.pos[1])
                elif c.pos[0] > c.rows -1: c.pos = (0,c.pos[1])
                elif c.pos[1] > c.rows -1: c.pos = (c.pos[0], 0)
                elif c.pos[1] < 0: c.pos = (c.pos[0], c.rows -1)
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx, c.dirny)
                if c.pos[0] < 0: c.pos = (c.rows-1, c.pos[1])
                elif c.pos[0] > c.rows -1: c.pos = (0,c.pos[1])
                elif c.pos[1] > c.rows -1: c.pos = (c.pos[0], 0)
                elif c.pos[1] < 0: c.pos = (c.pos[0], c.rows -1)

    def reset(self, pos):
        self.head = cube.cube(pos, color = self.color, rows = self.rows, width = self.width)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube.cube((tail.pos[0]-1, tail.pos[1]), color = self.color, rows = self.rows, width = self.width))
        elif dx == -1 and dy == 0:
            self.body.append(cube.cube((tail.pos[0]+1, tail.pos[1]), color = self.color, rows = self.rows, width = self.width))
        elif dx == 0 and dy == 1:
            self.body.append(cube.cube((tail.pos[0], tail.pos[1]-1), color = self.color, rows = self.rows, width = self.width))
        elif dx == 0 and dy == -1:
            self.body.append(cube.cube((tail.pos[0], tail.pos[1]+1), color = self.color, rows = self.rows, width = self.width))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
