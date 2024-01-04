import pygame as pg
import random
from PIL import Image


pic_world = Image.open('Sprites/world.png').convert('RGBA')
pixels = pic_world.load()
for i in range(pic_world.size[0]):
    for j in range(pic_world.size[1]):
        if (i + j) % 2 == 0:
            pixels[i, j] = 0, 0, 0, 0
pic_world.save('Sprites/world.png')

pg.init()

WIDTH, HEIGHT = 1400, 700

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('FREE FOR URSA')

clock = pg.time.Clock()
FPS = 60
background = (0, 0, 0)

# crosshair = pg.image.load('Sprites/crosshair.png')
pg.mouse.set_visible(False)
crosshair = pg.image.load('Sprites/crosshair.png')

glasses = pg.image.load('Sprites/glasses.png')
glasses = pg.transform.scale(glasses, (WIDTH + 100, HEIGHT + 40))

world = pg.image.load('Sprites/world.png')
world = pg.transform.scale(world, (WIDTH, HEIGHT))

running = True

while running:
    screen.fill(background)
    screen.blit(world, (0, 0))
    screen.blit(glasses, (-50, -20))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                crosshair = pg.image.load('Sprites/crosshair_hit.png')
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                crosshair = pg.image.load('Sprites/crosshair.png')
    cursor_xy = pg.mouse.get_pos()
    screen.blit(crosshair, cursor_xy)
    pg.display.flip()
    pg.display.update()
    clock.tick(FPS)

pg.quit()
