import pygame
import sys


class cube(object):
    rows = 20
    def __init__(self, start, dirx=1, diry=0, colour=(255,0,0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.colour = colour

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def draw(self, window, eyes=False):
        dis = size // rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(window, self.colour, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius, j*dis+8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis+8)
            pygame.draw.circle(window, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(window, (0,0,0), circleMiddle2, radius)


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]
                elif keys[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]
                elif keys[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]
                elif keys[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) -1:
                    self.turns.pop(p)
            else:
                if c.dirx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                elif c.dirx == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirx == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
                else: c.move(c.dirx,c.diry)

        

    def reset(self):
        #TODO
        pass

    def eat(self):
        #TODO
        pass

    def draw(self, window):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(window, True)
            else:
                c.draw(window)

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
    #TODO
    pass

def message():
    #TODO
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
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        redrawWindow(window)

main()
