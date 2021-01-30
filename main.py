import pygame
import sys


class cube(object):
    def __init__(self, start, dirx=1, diry=0, colour=(255,0,0)):

    def move(self, dirx, diry):

        pass
    def draw(self, window, eyes=False):


class snake(object):
    body = []
    turns = {}
    def __init__(self, colour, pos):
        self.colour = colour
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
    def reset(self):
        pass

    def eat(self):
        pass

        pass
    def draw(self, window):

def drawBoard(width, rows, window):
    sizeBtwn = width//rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(window, (255,255,255), (x,0), (x,width))
        pygame.draw.line(window, (255,255,255), (0,y), (width,y))


def redrawWindow(window):
    window.fill((0,0,0))
    s.draw(window)
    drawBoard(size, rows, window)
    pygame.display.update()

def randomFood():
    pass

def message():
    pass

def main():
    global size, rows, s
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
