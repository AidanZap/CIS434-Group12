# Playlist I was looking at : https://www.youtube.com/watch?v=i6xMBig-pP4
import random
import pygame
from pygame.locals import *
import cube
import snake
import button
import score


pygame.init()
width = 500
rows = 20
on_menu = True
playing = False
two_player = False
surface = pygame.display.set_mode((width, width))
font = pygame.font.SysFont("Arial", 32)
white = (255,255,255)
black = (0, 0, 0)
green = (0,200,30)
aqua= (0, 200, 170)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (150,150,150)

buttons = []
start_button = button.button("Play!",160,210,180,60,aqua,white)
two_player_button = button.button("2-Player Game",140, 280, 230, 60,aqua,white)
settings_button = button.button("Game Settings",140, 350, 230, 60,aqua,white)
quit_button = button.button("Quit", 212, 420, 80, 60, aqua, white)

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
        pygame.draw.line(surface, grey, (x, 0), (x, width))
        pygame.draw.line(surface, grey, (0, y), (width, y))


def redraw_window(surface, s, snack, scr, width, rows):
    surface.fill(black)
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
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def menu(font,clock):
    global on_menu, playing, surface
    surface.fill(black)

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            quit()
        click = (event.type == pygame.MOUSEBUTTONDOWN)                  
        mx, my = pygame.mouse.get_pos()

        if start_button.rect.collidepoint(mx, my):
            start_button.hover = True
            print("start")
            if click:
                print("start")
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
        b.draw(surface,font)
    pygame.display.update()
    clock.tick(60)


def main():
    global on_menu, playing
    
    #surface = pygame.display.set_mode((width, width))
    pygame.display.set_caption("PythonPythonGame")
    clock = pygame.time.Clock()


    # ***** Game Objects ***** #
    s = snake.snake(blue, (10, 5))
    snack = cube.cube(random_snack(rows, s), color=green)
    scr = score.score(0)
    if two_player:
        s2 = snake.snake(red, (10,15))

    # ***** Main Loop ***** #
    main_loop = True

    while main_loop:

        while on_menu:
            menu(font,clock)
            print(on_menu)
            

        while playing: 
            pygame.time.delay(10)
            clock.tick(10)
            s.move()
            if s.body[0].pos == snack.pos:
                s.addCube()
                scr.update()
                snack = cube.cube(random_snack(rows, s), color=green)

            for x in range(len(s.body)):
                if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                    print('Score: ', len(s.body))
                    s.reset((10, 10))
                    scr.score_count = 0
                    playing = False
                    on_menu = True
                    break

            redraw_window(surface, s, snack, scr, width, rows)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
