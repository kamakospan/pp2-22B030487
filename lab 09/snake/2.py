#imports
import pygame
import random

#pygame initializing
pygame.init()

#setting the screen
screen = pygame.display.set_mode((500, 500))

#variables
done = True
v = 15
sc = 0
frtimer = 0
bfrtimer = 0
 
#fps
clock = pygame.time.Clock()

#initial snake position
snpos = [100, 50]

#first 4 blocks of snake body
snbody = [[100, 50], [90, 50], [80, 50], [70, 50]]

#fruit position
frpos = [random.randrange(1, (500//10)) * 10, random.randrange(1, (500//10)) * 10]
bfrpos = [random.randrange(1, (500//10)) * 10, random.randrange(1, (500//10)) * 10]

#spawn
frsp = True
bfrsp = True
 
#showing score
def shsc(color, font, size):
    scfont = pygame.font.SysFont(font, size)
    scsurf = scfont.render('Score : ' + str(sc), True, color)
    screct = scsurf.get_rect()
    screen.blit(scsurf, screct)

#game over function
def game_over():
    gofont = pygame.font.SysFont("comicsans", 50)
    gosurf = gofont.render('Your Score is : ' + str(sc), True, (255,0,0))
    gorect = gosurf.get_rect()
    gorect.midtop = (500/2, 500/4)
    screen.fill((0,0,0))
    screen.blit(gosurf, gorect)

#initial direction of the snake
direction = 'RIGHT'
change_to = direction
 
#main game loop
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    #to not let the snake to move into two directions at the same time
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    #moving the snake
    if direction == 'UP':
        snpos[1] -= 10
    if direction == 'DOWN':
        snpos[1] += 10
    if direction == 'LEFT':
        snpos[0] -= 10
    if direction == 'RIGHT':
        snpos[0] += 10

    #body growing
    snbody.insert(0, list(snpos))

    #getting score
    if snpos[0] == frpos[0] and snpos[1] == frpos[1]:
        sc += 1
        frsp = False
    elif snpos[0] == bfrpos[0] and snpos[1] == bfrpos[1]:
        sc += 5
        bfrsp = False
    else:
        snbody.pop()
         
    #new random fruit
    if not frsp:
        frpos = [random.randrange(1, (500//10)) * 10, random.randrange(1, (500//10)) * 10]
        frtimer = 0
    frsp = True
    if not bfrsp:
        bfrpos = [random.randrange(1, (500//10)) * 10, random.randrange(1, (500//10)) * 10]
        bfrtimer = 0
    bfrsp = True
        
    bfrtimer += 1
    frtimer += 1
    
    if frtimer == 120:
        frtimer = 0
        frpos = [random.randrange(1, (500//10)) * 10, random.randrange(1, (500//10)) * 10]
    if bfrtimer == 70:
        bfrtimer = 0
        bfrpos = [random.randrange(1, (500//10)) * 10, random.randrange(1, (500//10)) * 10]

    screen.fill((0,0,0))
    
    #drawing snake and fruit with rectangles
    for pos in snbody:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(frpos[0], frpos[1], 10, 10))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(bfrpos[0], bfrpos[1], 10, 10))

    #if you go out of the screen, you lose
    if snpos[0] < 0 or snpos[0] > 500-10: game_over()
    if snpos[1] < 0 or snpos[1] > 500-10: game_over()

    #if you touch yourself as a snake, you lose as well
    for block in snbody[1:]:
        if snpos[0] == block[0] and snpos[1] == block[1]: game_over()
    
    shsc((255,255,255), "comicsans", 20)
    pygame.display.flip()
    clock.tick(v)