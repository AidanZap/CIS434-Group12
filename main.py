# Playlist I was looking at : https://www.youtube.com/watch?v=i6xMBig-pP4
import random
import pygame
import pygame.locals
import cube
import snake


def draw_grid(width, rows, surface):
    row_width = width // rows
    x = 0
    y = 0

    for i in range(rows):
        x += row_width
        y += row_width
        pygame.draw.line(surface, (150, 150, 150), (x, 0), (x, width))
        pygame.draw.line(surface, (150, 150, 150), (0, y), (width, y))


def redraw_window(surface, s, snack, width, rows):
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
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


def menu(surface, clock):
    on_menu = True
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 72)
    text_obj = font.render("PythonPythonGame", 1, (0, 255, 0))
    text_rect = text_obj.get_rect()
    text_rect.topleft = (200, 200)
    surface.blit(text_obj, text_rect)

    while on_menu:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                pygame.quit()

        pygame.display.update()
        clock.tick(60)


def main():
    width = 500
    rows = 20
    surface = pygame.display.set_mode((width, width))
    pygame.display.update()

    # ***** Game Objects ***** #
    clock = pygame.time.Clock()
    s = snake.snake((255, 0, 0), (10, 10))
    snack = cube.cube(random_snack(rows, s), color=(0, 255, 0))

    # menu(surface, clock)

    playing = True
    while playing:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube.cube(random_snack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                s.reset((10, 10))
                break

        redraw_window(surface, s, snack, width, rows)


if __name__ == "__main__":
    main()
