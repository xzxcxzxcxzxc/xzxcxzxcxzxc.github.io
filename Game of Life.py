#!python3

import time,copy,pygame,random
pygame.init()
a = int(input("输入x"))
b = int(input("输入y"))
size=width,height=10*a+2,10*b+2
screen = pygame.display.set_mode(size)
BLACK = pygame.Color('black')
GAINSBORO = pygame.Color('gainsboro')
MOCCASIN = pygame.Color('moccasin')
WHITE = pygame.Color('white')
screen.fill(MOCCASIN)
fclock = pygame.time.Clock()
'''cellNow=[
    [False,False,False,False],
    [False,False,True,False],
    [False,False,True,False],
    [False,False,True,False]
]
cellNext=[
    [False,False,False,False],
    [False,False,True,False],
    [False,False,True,False],
    [False,False,True,False]
]'''
def gridAround(y,x):
    around = 0
    for i in range(y - 1, y + 2):
        if i >= len(cellNow):
            i = 0
        for j in range(x - 1, x + 2):
            if j >= len(cellNow[i]):
                j = 0
            if cellNow[i][j]:
                around = around + 1
    if cellNow[y][x]:
        around = around - 1
    return around


def rule(y,x,n):
    num = gridAround(y, x)
    if num < 2 or num > 3:
        return False
    elif num == 2:
        return n
    else:
        return True
cellNow = []
cellNext = []
for i in range(a):
    cellNow.append([])
    for j in range(b):
        if  random.randint(0,1) == 1:
            cellNow[i].append(True)
        else:
            cellNow[i].append(False)
cellNext = copy.deepcopy(cellNow)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for y in range(len(cellNow)):
        for x in range(len(cellNow[y])):
            cellNext[y][x] = rule(y,x,cellNow[y][x])
    cellNow = copy.deepcopy(cellNext)
    for y in range(len(cellNow)):
        for x in range(len(cellNow[y])):
            if cellNow[y][x]:
                pygame.draw.rect(screen, BLACK, (y*10,x*10,10,10))
                pygame.draw.rect(screen, GAINSBORO, (y*10,x*10,10,10),1)
            else:
                pygame.draw.rect(screen, WHITE, (y*10,x*10,10,10))
                pygame.draw.rect(screen, GAINSBORO, (y*10,x*10,10,10),1)     
    pygame.display.flip()
    fclock.tick(3)