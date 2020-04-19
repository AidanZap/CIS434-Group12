import pygame
import cube


class snake(object):
    body = []
    turns = {}
    counter = 0

    def __init__(self, gs, player):
        self.gs = gs
        self.player = player
        self.color = gs.s_colors[self.player - 1]
        self.start_pos = gs.s_starts[player - 1]
        self.width = gs.width
        self.rows = gs.rows
        self.grow = False

        self.head = cube.cube(self.gs, self.start_pos, color=self.color)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 1
        self.dirny = 0

    def setGS(self, gs):
        self.gs = gs
        for c in self.body:
            c.setGS(gs)

    def move(self,gs):
        if self.grow:
            self.counter += 1
            if self.counter >= 10:
                self.counter = 0
                self.addCube()
                if self == gs.snake1:
                    gs.scr.add_score(1)
                if self == gs.snake2:
                    gs.scr.add_score(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        keys = pygame.key.get_pressed()

        if ((keys[pygame.K_LEFT] and self.player == 1) or (keys[pygame.K_a] and self.player == 2)) and self.dirnx != 1:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif ((keys[pygame.K_RIGHT] and self.player == 1) or (
                keys[pygame.K_d] and self.player == 2)) and (self.dirnx != -1 and self.dirnx != 1):
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif ((keys[pygame.K_UP] and self.player == 1) or (keys[pygame.K_w] and self.player == 2)) and self.dirny != 1:
            self.dirny = -1
            self.dirnx = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif ((keys[pygame.K_DOWN] and self.player == 1) or (
                keys[pygame.K_s] and self.player == 2)) and self.dirny != -1:
            self.dirny = 1
            self.dirnx = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if c.pos[0] < 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.pos[0] > c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.pos[1] > c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.pos[1] < 0:
                    c.pos = (c.pos[0], c.rows - 1)
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx, c.dirny)
                if c.pos[0] < 0:
                    c.pos = (c.rows - 1, c.pos[1])
                    if self.gs.borders_on:
                        return True
                elif c.pos[0] > c.rows - 1:
                    c.pos = (0, c.pos[1])
                    if self.gs.borders_on:
                        return True
                elif c.pos[1] > c.rows - 1:
                    c.pos = (c.pos[0], 0)
                    if self.gs.borders_on:
                        return True
                elif c.pos[1] < 0:
                    c.pos = (c.pos[0], c.rows - 1)
                    if self.gs.borders_on:
                        return True
        return False  # False signifies no collision for borders is needed

    def reset(self):
        self.head = cube.cube(self.gs, self.start_pos, color=self.color)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 1
        self.dirny = 0

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube.cube(self.gs, (tail.pos[0] - 1, tail.pos[1]), color=self.color))
        elif dx == -1 and dy == 0:
            self.body.append(cube.cube(self.gs, (tail.pos[0] + 1, tail.pos[1]), color=self.color))
        elif dx == 0 and dy == 1:
            self.body.append(cube.cube(self.gs, (tail.pos[0], tail.pos[1] - 1), color=self.color))
        elif dx == 0 and dy == -1:
            self.body.append(cube.cube(self.gs, (tail.pos[0], tail.pos[1] + 1), color=self.color))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(True)
            else:
                c.draw()