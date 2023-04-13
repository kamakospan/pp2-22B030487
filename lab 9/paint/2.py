#imports
import pygame

#pygame initializing
pygame.init()

#setting the screen an filling with white color
screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))

#variables
done = True
radius = 15

white = eraser = (255, 255, 255)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)

color = white
lstpos = False

#fps
clock = pygame.time.Clock()

def drawLineBetween(start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(mousepos, w, h, color):
    x = mousepos[0]
    y = mousepos[1]
    rect = pygame.Rect(x, y, w, h) #left #top #width #height
    pygame.draw.rect(screen, color, rect, 3)

def drawCircle(mousepos, color):
    x = mousepos[0]
    y = mousepos[1]
    pygame.draw.circle(screen, color, (x, y), 50, 3) #screen #color #center of the circle #radius #width

def drawSquare(mousepos, w, h, color):
    x = mousepos[0]
    y = mousepos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

def drawRightTriangle(color, mousepos):
    x = mousepos[0]
    y = mousepos[1]
    points = [(x, y),(x, y + 100),(x + 100, y + 100),]
    pygame.draw.polygon(screen, color, points, 3)

def drawEqTriangle(color, mousepos):
    x = mousepos[0]
    y = mousepos[1]
    points = [(x, y),(x - 50, y + 100),(x + 50, y + 100),]
    pygame.draw.polygon(screen, color, points, 3)  

def drawRhombus(color, mousepos):
    x = mousepos[0]
    y = mousepos[1]
    points = [(x, y),(x - 50, y + 50),(x, y + 100),(x + 50, y + 50),]
    pygame.draw.polygon(screen, color, points, 3)

#main game loop
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = red
            elif event.key == pygame.K_g:
                color = green
            elif event.key == pygame.K_b:
                color = blue
            elif event.key == pygame.K_BACKSPACE:
                color = eraser
            elif event.key == pygame.K_e:
                drawRectangle(pygame.mouse.get_pos(), 150, 100, color)
            elif event.key == pygame.K_c:
                drawCircle(pygame.mouse.get_pos(), color)
            elif event.key == pygame.K_s:
                drawSquare(pygame.mouse.get_pos(), 100, 100, color)
            elif event.key == pygame.K_v:
                drawEqTriangle(color, pygame.mouse.get_pos())
            elif event.key == pygame.K_l:
                drawRightTriangle(color, pygame.mouse.get_pos())
            elif event.key == pygame.K_x:
                drawRhombus(color, pygame.mouse.get_pos())
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #the left mouse button
            lstpos = pygame.mouse.get_pos()
            
        if event.type == pygame.MOUSEMOTION and event.buttons[0]: #tuple, 0 is the left mouse button
            if lstpos:
                stpos = lstpos
                endpos = pygame.mouse.get_pos()
                drawLineBetween(stpos, endpos, radius, color)
                lstpos = endpos

    pygame.display.flip()
    clock.tick(60)