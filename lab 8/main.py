import pygame

pygame.init() #initializes the Pygame
from pygame.locals import* #import all modules from Pygame

screen = pygame.display.set_mode((798,600)) # created a screen variable in which we accessed the pygame’s display.set_mode()
while True :
    pass
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.set_caption('Racer Jake') #changing title of the game window