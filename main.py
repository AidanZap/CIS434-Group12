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


menu_buttons = []
start_button = button.button(gs, "Play!", (gs.menu_width-180)/2, 280, 180, 60, gs.color.brown, gs.color.light_green)
settings_button = button.button(gs, "Game Settings", (gs.menu_width-230)/2, 360, 230, 60, gs.color.brown, gs.color.light_green)
quit_button = button.button(gs, "Quit", (gs.menu_width-80)/2, 440, 80, 60, gs.color.brown, gs.color.light_green)
menu_buttons.append(start_button)
menu_buttons.append(settings_button)
menu_buttons.append(quit_button)

# ***** Settings Buttons *****#
back_button = button.button(gs, "<-- back", 0, 0, 130, 45, gs.color.brown, gs.color.light_green)
settings_active = []
settings_inactive = []
mode_classic = button.button(gs, "Classic", (gs.menu_width-230), 90, 200, 60, gs.color.brown, gs.color.light_green)
mode_race = button.button(gs, "2-P Race", (gs.menu_width-230), 90, 200, 60, gs.color.brown, gs.color.light_green)
mode_melee = button.button(gs, "2-P Melee", (gs.menu_width-230), 90, 200, 60, gs.color.brown, gs.color.light_green)

size_mini = button.button(gs, "Mini", (gs.menu_width-230), 180, 200, 60, gs.color.brown, gs.color.light_green)
size_regular = button.button(gs, "Regular", (gs.menu_width-230), 180, 200, 60, gs.color.brown, gs.color.light_green)
size_large = button.button(gs, "Large", (gs.menu_width-230), 180, 200, 60, gs.color.brown, gs.color.light_green)
size_ludicrous = button.button(gs, "Ludicrous", (gs.menu_width-230), 180, 200, 60, gs.color.brown, gs.color.light_green)

fruit_one = button.button(gs, "One Fruit", (gs.menu_width-230), 270, 200, 60, gs.color.brown, gs.color.light_green)
fruit_two = button.button(gs, "Two Fruit", (gs.menu_width-230), 270, 200, 60, gs.color.brown, gs.color.light_green)
fruit_three = button.button(gs, "Three Fruit", (gs.menu_width-230), 270, 200, 60, gs.color.brown, gs.color.light_green)
fruit_five = button.button(gs, "Five Fruit", (gs.menu_width-230), 270, 200, 60, gs.color.brown, gs.color.light_green)

border_on = button.button(gs, "Borders On", (gs.menu_width-230), 360, 200, 60, gs.color.brown, gs.color.light_green)
border_off = button.button(gs, "Borders Off", (gs.menu_width-230), 360, 200, 60, gs.color.brown, gs.color.light_green)

obstacle_on = button.button(gs, "Obstacles On", (gs.menu_width-230), 450, 200, 60, gs.color.brown, gs.color.light_green)
obstacle_off = button.button(gs, "Obstacles Off", (gs.menu_width-230), 450, 200, 60, gs.color.brown, gs.color.light_green)

settings_active.append(mode_classic)
settings_active.append(size_regular)
settings_active.append(fruit_one)
settings_active.append(obstacle_off)
settings_active.append(border_on)
settings_inactive.append(mode_race)
settings_inactive.append(mode_melee)
settings_inactive.append(size_mini)
settings_inactive.append(size_large)
settings_inactive.append(size_ludicrous)
settings_inactive.append(fruit_two)
settings_inactive.append(fruit_three)
settings_inactive.append(fruit_five)
settings_inactive.append(obstacle_on)
settings_inactive.append(border_off)


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
    gs.surface.blit(image,((gs.menu_width-256)/2,0))

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

        if settings_button.rect.collidepoint(mx, my):
            settings_button.hover = True
            if click:
                gs.on_menu = False
                gs.on_settings = True
        else:
            settings_button.hover = False

        if quit_button.rect.collidepoint(mx, my):
            quit_button.hover = True
            if click:
                pygame.quit()
        else:
            quit_button.hover = False
    for b in menu_buttons:
        b.draw()

    pygame.display.update()
    gs.clock.tick(60)


def update_settings_buttons(remove, add):
    global settings_active, settings_inactive
    settings_inactive.append(remove)
    settings_active.append(add)
    settings_active.remove(remove)
    settings_inactive.remove(add)


def settings_menu():
    gs.surface.fill(gs.color.black)
    back_button.draw()
    draw_text("Settings Menu", gs.color.white, gs.menu_width/2, 20)
    draw_text("Game mode", gs.color.white, 120, 120)
    draw_text("Board Size", gs.color.white, 120, 210)
    draw_text("Number of Fruit", gs.color.white, 120, 300)
    draw_text("Toggle Borders", gs.color.white, 120, 390)
    draw_text("Toggle Obstacles", gs.color.white, 120, 480)

    for event in pygame.event.get():
        if event.type == QUIT:
            d.close()
            pygame.quit()
            quit()
        click = (event.type == pygame.MOUSEBUTTONDOWN)
        mx, my = pygame.mouse.get_pos()

        if back_button.rect.collidepoint(mx, my):
            back_button.hover = True
            if click:
                gs.on_settings = False
                gs.on_menu = True
        else:
            back_button.hover = False
        for a in settings_active:
            if a.rect.collidepoint(mx, my):
                a.hover = True
            else:
                a.hover = False

        if mode_classic.rect.collidepoint(mx, my) and click:
            if mode_classic in settings_active:
                gs.mode = "race"
                update_settings_buttons(mode_classic, mode_race)
                continue
        if mode_race.rect.collidepoint(mx, my) and click:
            if mode_race in settings_active:
                gs.mode = "melee"
                update_settings_buttons(mode_race, mode_melee)
                continue
        if mode_melee.rect.collidepoint(mx, my) and click:
            if mode_melee in settings_active:
                gs.mode = "classic"
                update_settings_buttons(mode_melee, mode_classic)
                continue

        if size_mini.rect.collidepoint(mx, my) and click:
            if size_mini in settings_active:
                gs.width = 540
                update_settings_buttons(size_mini, size_regular)
                continue
        if size_regular.rect.collidepoint(mx, my) and click:
            if size_regular in settings_active:
                gs.width = 680
                update_settings_buttons(size_regular, size_large)
                continue
        if size_large.rect.collidepoint(mx, my) and click:
            if size_large in settings_active:
                gs.width = 1000
                update_settings_buttons(size_large, size_ludicrous)
                continue
        if size_ludicrous.rect.collidepoint(mx, my) and click:
            if size_ludicrous in settings_active:
                gs.width = 400
                update_settings_buttons(size_ludicrous, size_mini)
                continue
        if fruit_one.rect.collidepoint(mx, my) and click:
            if fruit_one in settings_active:
                gs.fruit_count = 2
                update_settings_buttons(fruit_one, fruit_two)
                continue
        if fruit_two.rect.collidepoint(mx, my) and click:
            if fruit_two in settings_active:
                gs.fruit_count = 3
                update_settings_buttons(fruit_two, fruit_three)
                continue
        if fruit_three.rect.collidepoint(mx, my) and click:
            if fruit_three in settings_active:
                gs.fruit_count = 5
                update_settings_buttons(fruit_three, fruit_five)
                continue
        if fruit_five.rect.collidepoint(mx, my) and click:
            if fruit_five in settings_active:
                gs.fruit_count = 1
                update_settings_buttons(fruit_five, fruit_one)
                continue
        if border_on.rect.collidepoint(mx, my) and click:
            if border_on in settings_active:
                gs.border_on = False
                update_settings_buttons(border_on, border_off)
                continue
        if border_off.rect.collidepoint(mx, my) and click:
            if border_off in settings_active:
                gs.border_on = True
                update_settings_buttons(border_off, border_on)
                continue
        if obstacle_on.rect.collidepoint(mx, my) and click:
            if obstacle_on in settings_active:
                gs.obstacle_on = False
                update_settings_buttons(obstacle_on, obstacle_off)
                continue
        if obstacle_on.rect.collidepoint(mx, my) and click:
            if obstacle_off in settings_active:
                gs.obstacle_on = True
                update_settings_buttons(obstacle_off, obstacle_on)
                continue

    for a in settings_active:
        a.draw()
    pygame.display.update()
    gs.clock.tick(60)


def main():
    global gs
    pygame.display.set_caption("PythonPythonGame")

    # ***** Game Objects ***** #
    gs.snakes.append(snake.snake(gs, 1))
    gs.snacks.append(cube.cube(gs, random_snack(), color=gs.color.green))

    if gs.mode == "race":
        gs.snakes.append(snake.snake(gs, 2))
    elif gs.mode == "melee":
        gs.snakes.append(snake.snake(gs, 2))
    print(gs.snakes)

    # ***** Main Loop ***** #
    main_loop = True

    while main_loop:

        while gs.on_menu:
            menu()

        while gs.on_settings:
            settings_menu()

        gs.surface = pygame.display.set_mode((gs.width, gs.width + gs.banner_height))
        while gs.playing:

            redraw_window()
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
