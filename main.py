import pygame, sys
import random
import tkinter as tk
import numpy as np

class cube(object):
    def __init__(self, start, dirx=1, diry=0, colour=(255,0,0)):

    def move(self, dirx, diry):

    def draw(self, canvas, eyes=False):
        pass


class snake(object):
    def __init__(self, colour, pos):
    def move(self):
    def reset(self):
        pass

    def eat(self):
        pass

    def draw(self):
        pass

def drawBoard(width, rows, canvas):
    sizeBtwn = width//rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(canvas, (255,255,255), (x,0), (x,width))
        pygame.draw.line(canvas, (255,255,255), (0,y), (width,y))


def redrawWindow(canvas):
    canvas.fill((0,0,0))
    drawBoard(size, rows, canvas)
    pygame.display.update()

def randomFood():
    pass

def message():
    pass

def main():
    global size, rows
    size = 600
    rows = 20
    pygame.init()
    window = pygame.display.set_mode((size,size))
    s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(window)

main()
