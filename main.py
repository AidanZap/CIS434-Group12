#HighScore : 36 DW

import random
import pygame
from pygame.locals import *
import cube
import snake
import button
import score
import shelve
import game_settings as g

# Shelve anf PyGame startup
d = shelve.open('score.txt')
gs = g.game()
scr = score.score(1, gs)
h_scr = score.score(d['score'],gs)


buttons = []
start_button = button.button(gs, "Play!", (gs.width-180)/2, 251, 180, 60, gs.color.brown, gs.color.light_green)
two_player_button = button.button(gs, "Game Mode", (gs.width-230)/2, 314, 230, 60,gs.color.brown, gs.color.light_green)
settings_button = button.button(gs, "Game Settings", (gs.width-230)/2, 377, 230, 60, gs.color.brown, gs.color.light_green)
quit_button = button.button(gs, "Quit", (gs.width-80)/2, 440, 80, 60, gs.color.brown, gs.color.light_green)

buttons.append(start_button)
buttons.append(two_player_button)
buttons.append(settings_button)
buttons.append(quit_button)


def draw_grid():
    x = 0
    y = 0

    for i in range(gs.rows):
        x += gs.row_width
        y += gs.row_width
        pygame.draw.line(gs.surface, gs.color.dark_grey, (x, 0), (x, gs.width))
        pygame.draw.line(gs.surface, gs.color.dark_grey, (0, y), (gs.width, y))


def redraw_window():
    gs.surface.fill(gs.color.black)
    for s in gs.snakes:
        s.draw()
    for snack in gs.snacks:
        snack.draw()
    for obs in gs.obstacles:
        obs.draw()
    scr.draw("Score: ")
    draw_grid()
    pygame.display.update()


def random_snack():
    positions = []
    for s in gs.snakes:
        positions.extend(s.body)

    while True:
        x = random.randrange(gs.rows)
        y = random.randrange(gs.rows)

        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else: 
            break

    return x, y


def draw_text(text, text_color, x, y):
    text_obj = gs.font.render(text, 1, text_color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    gs.surface.blit(text_obj, text_rect)

def reset_game():
    for s in gs.snakes:
        s.reset()


def menu():
    global gs
    gs.surface.fill(gs.color.black)
    h_scr.draw("High Score: ")
    image = pygame.image.load('Snake-icon.png')
    gs.surface.blit(image,((gs.width-256)/2,0))

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
                gs.on_menu = False
                gs.playing = True
        else:
            start_button.hover = False
        if two_player_button.rect.collidepoint((mx, my)):
            two_player_button.hover = True
            if click:
                gs.two_player = True
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
        b.draw()

    pygame.display.update()
    gs.clock.tick(60)


def main():
    global gs
    pygame.display.set_caption("PythonPythonGame")

    # ***** Game Objects ***** #
    gs.snakes.append(snake.snake(gs, 1))
    gs.snacks.append(cube.cube(gs, random_snack(), color=gs.color.green))
    
    if gs.two_player or True:
        gs.snakes.append(snake.snake(gs, 2))
    print(gs.snakes)
    # ***** Main Loop ***** #
    main_loop = True

    while main_loop:

        while gs.on_menu:
            menu()

        while gs.playing: 
            for s in gs.snakes:
                s.move()
                for snack in gs.snacks:         
                    if s.body[0].pos == snack.pos:
                        s.addCube()
                        scr.update()
                        gs.snacks.remove(snack)
                        gs.snacks.append(cube.cube(gs, random_snack(), color=gs.color.green))

                for x in range(len(s.body)):
                    if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                        print('Score: ', len(s.body))
                        reset_game()
                        if scr.score_count > h_scr.score_count:
                            d['score'] = scr.score_count
                            h_scr.score_count = scr.score_count
                        scr.score_count = 0
                        gs.playing = False
                        gs.on_menu = True
                        break
            
            redraw_window()
            gs.clock.tick(10)
    d.close()
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
