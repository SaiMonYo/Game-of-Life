import pygame
from ObjectsGOL import Grid

WHITE = (255, 255, 255)
BLACK = ( 0 ,  0 ,  0 )

WIDTH = 1000
HEIGHT = 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

board = Grid(win, 100, 100)


mouseDown = False
rubber = False

running = True
looping = False

while running:
    win.fill(WHITE)
    for event in pygame.event.get():
        # user clicks the x
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not looping:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                rubber = not rubber
            if event.key == pygame.K_SPACE:
                looping = not looping
                
    if mouseDown and not looping:
        posx, posy = pygame.mouse.get_pos()
        gridX = posx // board.gap
        gridY = posy // board.gap

        board.on_click(gridX, gridY, not rubber)

    if looping:
        board.loop()

    #board.draw_lines()
    board.draw_grid()
    pygame.display.update()
