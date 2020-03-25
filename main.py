# Playlist I was looking at : https://www.youtube.com/watch?v=i6xMBig-pP4
import math
import random
import pygame
import cube
import snake
import tkinter as tk
from tkinter import messagebox #fixx


def drawGrid(w, rows, surface):
    rowWidth = width // rows
    x = 0
    y = 0

    for i in range(rows):
        x += rowWidth
        y += rowWidth
        pygame.draw.line(surface, (150,150,150), (x,0), (x,w))
        pygame.draw.line(surface, (150,150,150), (0,y), (w,y))


def redrawWindow(surface):
   
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        if len(list(filter(lambda z:z.pos == (x,y), positions)))> 0:
             continue
        else: 
            break

    return (x,y)

def message_box(subject,content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject,content)
    try:
        root.destroy()
    except:
        pass


def menu(surface):

    for event in pygame.event.get():
        if event.type == pygame.quit():
            pygame.quit()

    surface.fill((0,0,0))
    font = pygame.font.SysFont(None, 135)
    text_obj = font.render("PythonPythonGame", 1, (0, 255, 0))
    text_rect = text_obj.get_rect()
    text_rect.topleft = {200, 200}
    surface.blit(text_obj, text_rect)

    pygame.display.update()
    clock.tick(60)



pygame.init()
width = 500
rows = 20
win = pygame.display.set_mode((width, width))
clock = pygame.time.Clock()
s = snake.snake((255, 0, 0), (10, 10))
snack = cube.cube(randomSnack(rows, s), color=(0, 255, 0))



flag = True

while flag:
    if True:
        menu(win)
    elif False:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0,255,0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play Again..')
                s.reset((10, 10))
                break


        redrawWindow(win)
        
    pass


