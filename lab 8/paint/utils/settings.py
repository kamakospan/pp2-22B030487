import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 240 #frame 

WIDTH, HEIGHT = 600, 700
# constants so in capitals
ROWS = COLS = 100 #size of our pixels

TOOLBAR_HEIGHT = HEIGHT - WIDTH #100

PIXEL_SIZE = WIDTH // COLS 

BG_COLOR = WHITE

DRAW_GRID_LINES = False #so that we dont show the lines


def get_font(size): #retur n a font object
    return pygame.font.SysFont("comicsans", size)