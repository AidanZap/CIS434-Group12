# Playlist I was looking at : https://www.youtube.com/watch?v=i6xMBig-pP4
import random
import pygame
from pygame.locals import *
import cube
import snake
import score

def draw_grid(width, rows, surface):
    row_width = width // rows
    x = 0
    y = 0

    for i in range(rows):
        x += row_width
        y += row_width
        pygame.draw.line(surface, (150, 150, 150), (x, 0), (x, width))
        pygame.draw.line(surface, (150, 150, 150), (0, y), (width, y))


def redraw_window(surface, s, snack, scr, width, rows):
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    scr.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else: 
            break

    return x, y


def draw_text(text, font, text_color, surface, x, y):
    text_obj = font.render(text, 1, text_color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def main():
    pygame.init()
    width = 500
    rows = 20
    surface = pygame.display.set_mode((width, width))
    pygame.display.set_caption("PythonPythonGame")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 32)

    # ***** Game Objects ***** #
    s = snake.snake((255, 0, 0), (10, 10))
    snack = cube.cube(random_snack(rows, s), color=(0, 255, 0))
    scr = score.score(0) 

    # ***** Main Loop ***** #
    on_menu = True
    playing = False
    main_loop = True

    while main_loop:

        while on_menu:
            surface.fill((0, 0, 0))

            start_button = pygame.Rect(160, 210, 180, 60)
            pygame.draw.rect(surface, (0, 128, 0), start_button)
            draw_text("Start Game", font, (255, 255, 255), surface, 170, 220)

            two_player_button = pygame.Rect(140, 280, 230, 60)
            pygame.draw.rect(surface, (0, 128, 0), two_player_button)
            draw_text("2-Player Game", font, (255, 255, 255), surface, 150, 290)

            settings_button = pygame.Rect(140, 350, 230, 60)
            pygame.draw.rect(surface, (0, 128, 0), settings_button)
            draw_text("Game Settings", font, (255, 255, 255), surface, 150, 360)

            quit_button = pygame.Rect(212, 420, 80, 60)
            pygame.draw.rect(surface, (0, 128, 0), quit_button)
            draw_text("Quit", font, (255, 255, 255), surface, 220, 430)

            mx, my = pygame.mouse.get_pos()
            if start_button.collidepoint(mx, my):
                if click:
                    on_menu = False
                    playing = True
            if two_player_button.collidepoint((mx, my)):
                if click:
                    pass
            if settings_button.collidepoint(mx, my):
                if click:
                    pass
            if quit_button.collidepoint(mx, my):
                if click:
                    on_menu = False
                    main_loop = False

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    click = True

            pygame.display.update()
            clock.tick(60)

        while playing: 
            pygame.time.delay(50)
            clock.tick(10)
            s.move()
            if s.body[0].pos == snack.pos:
                s.addCube()
                scr.update()
                snack = cube.cube(random_snack(rows, s), color=(0, 255, 0))

            for x in range(len(s.body)):
                if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                    print('Score: ', len(s.body))
                    playing = False
                    on_menu = True
                    break

            redraw_window(surface, s, snack, scr, width, rows)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
