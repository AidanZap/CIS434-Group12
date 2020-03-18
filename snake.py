import pygame

GRID_SQUARE = 50


class App:

    def __init__(self):
        pygame.init()
        self.window_width = 12 * GRID_SQUARE
        self.window_height = 16 * GRID_SQUARE
        self.win = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("PythonPythonGame")
        self.time_delay = 100
        self.snake = Snake()
        self.running = True

    def start_game(self):
        while self.running:
            pygame.time.delay(self.time_delay)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # ***** Player input ***** #
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.snake.face_left()
            if keys[pygame.K_RIGHT]:
                self.snake.face_right()
            if keys[pygame.K_UP]:
                self.snake.face_up()
            if keys[pygame.K_DOWN]:
                self.snake.face_down()

            self.snake.update()

            app.win.fill((0, 0, 0))
            pygame.draw.rect(app.win, (255, 0, 0), (self.snake.x, self.snake.y, self.snake.width, self.snake.height))
            pygame.display.update()


class Snake:

    def __init__(self):
        self.x = 6 * GRID_SQUARE
        self.y = 8 * GRID_SQUARE
        self.width = GRID_SQUARE
        self.height = GRID_SQUARE
        self.vel = GRID_SQUARE
        self.facing = "RIGHT"

    def face_left(self):
        if self.facing is not "RIGHT":
            self.facing = "LEFT"

    def face_right(self):
        if self.facing is not "LEFT":
            self.facing = "RIGHT"

    def face_up(self):
        if self.facing is not "DOWN":
            self.facing = "UP"

    def face_down(self):
        if self.facing is not "UP":
            self.facing = "DOWN"

    def update(self):
        if self.facing == "UP":
            self.y -= self.vel
        elif self.facing == "DOWN":
            self.y += self.vel
        elif self.facing == "LEFT":
            self.x -= self.vel
        elif self.facing == "RIGHT":
            self.x += self.vel


# ***** Start ***** #
app = App()
app.start_game()
