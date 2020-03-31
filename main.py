#HighScore : 36 DW

import random
import pygame
from pygame.locals import *
import cube
import snake
import button
import score
import shelve

# Shelve anf PyGame startup
d = shelve.open('score.txt')
pygame.init()

#Game Vars
width = 800
row_width = 25
rows = width//row_width
banner_height = 50
on_menu = True
playing = False
two_player = False

# PyGame vars
surface = pygame.display.set_mode((width, width + banner_height))
font = pygame.font.SysFont("Arial", 32)
clock = pygame.time.Clock()
# Scores
scr = score.score(1, width)
h_scr = score.score(d['score'],width)
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 30)
dark_grey = (50, 50, 50)
light_green =  (70, 255, 70)
aqua= (10, 200, 150)
blue = (0, 0, 255)
purple = (125, 0, 125)
red = (255, 0, 0)
grey = (150, 150, 150)
brown = (139, 69, 19)

buttons = []
start_button = button.button("Play!", (width-180)/2, 251, 180, 60, brown, light_green)
two_player_button = button.button("Game Mode", (width-230)/2, 314, 230, 60, brown, light_green)
settings_button = button.button("Game Settings", (width-230)/2, 377, 230, 60, brown, light_green)
quit_button = button.button("Quit", (width-80)/2, 440, 80, 60, brown, light_green)

buttons.append(start_button)
buttons.append(two_player_button)
buttons.append(settings_button)
buttons.append(quit_button)


def draw_grid(width, rows, surface):
    row_width = width // rows
    x = 0
    y = 0

    for i in range(rows):
        x += row_width
        y += row_width
        pygame.draw.line(surface, dark_grey, (x, 0), (x, width))
        pygame.draw.line(surface, dark_grey, (0, y), (width, y))


def redraw_window(surface, s, snack, scr, width, rows):
    surface.fill(black)
    s.draw(surface)
    snack.draw(surface)
    scr.draw(surface, "Score: ")
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
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def menu(font, clock):
    global on_menu, playing, surface
    surface.fill(black)
    h_scr.draw(surface, "High Score: ")
    image = pygame.image.load('Snake-icon.png')
    surface.blit(image,((width-256)/2,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            d.close()
            pygame.quit()
            quit()
        click = (event.type == pygame.MOUSEBUTTONDOWN)                  
        mx, my = pygame.mouse.get_pos()

        if start_button.rect.collidepoint(mx, my):
            start_button.hover = True
            if click:
                on_menu = False
                playing = True
        else:
            start_button.hover = False
        if two_player_button.rect.collidepoint((mx, my)):
            two_player_button.hover = True
            if click:
                two_player = True
        else:
            two_player_button.hover = False
    
        if settings_button.rect.collidepoint(mx, my):
            settings_button.hover = True
        else:
            settings_button.hover = False
            
        if quit_button.rect.collidepoint(mx, my):
            quit_button.hover = True
            if click:
                pygame.quit()
        else:
            quit_button.hover = False
    for b in buttons:
        b.draw(surface, font)

    pygame.display.update()
    clock.tick(60)


def main():
    global on_menu, playing
    pygame.display.set_caption("PythonPythonGame")

    # ***** Game Objects ***** #
    s = snake.snake(purple, (10, 5), rows = rows, width = width)
    snack = cube.cube(random_snack(rows, s), color=green, rows = rows, width = width)
    
    if two_player:
        s2 = snake.snake(red, (10,15), rows = rows, width = width)

    # ***** Main Loop ***** #
    main_loop = True

    while main_loop:

        while on_menu:
            menu(font, clock)

        while playing: 
            
            s.move()
            if s.body[0].pos == snack.pos:
                s.addCube()
                scr.update()
                snack = cube.cube(random_snack(rows, s), color=green, rows = rows, width = width)

            for x in range(len(s.body)):
                if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                    print('Score: ', len(s.body))
                    s.reset((10, 10))
                    if scr.score_count > h_scr.score_count:
                        d['score'] = scr.score_count
                        h_scr.score_count = scr.score_count
                    scr.score_count = 0
                    playing = False
                    on_menu = True
                    break
            clock.tick(10)
            redraw_window(surface, s, snack, scr, width, rows)
    d.close()
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
