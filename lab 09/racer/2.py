import pygame as pg
from pygame import mixer 
from sys import exit
import random, time

pg.init()
mixer.init()
clock=pg.time.Clock()

ENEMYSPEED=3
JAKESPEED=5
SCORECOIN1=0
SCORECOIN2=0
SCORE=0
CNTENEMY=0

f1 = pg.font.Font('Gemstone.ttf', 20)
f2 = pg.font.Font('Gemstone.ttf', 25)

screen=pg.display.set_mode((768, 594))
pg.display.set_caption("САВУЕЙ СЕРФ ДУУУУУП")

mixer.music.load("Subway Surfers OST Extended (256  kbps).mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

bg=pg.image.load("background.png")
bg1=pg.image.load("gameover.png")


deadscreen=False


class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("enemy2.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,768-40),0) 
 
      def move(self):
        self.rect.move_ip(0,ENEMYSPEED+SCORECOIN1//50)
        if (self.rect.bottom > 650):
            global CNTENEMY
            CNTENEMY+=5
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("jakeorig.png")
        self.imagecool=pg.image.load("jakehappy.png")
        self.imagefail=pg.image.load("jakedead.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pg.K_LEFT]:
                  self.rect.move_ip(-1*(JAKESPEED+SCORECOIN1//10), 0)
        if self.rect.right < 768:        
              if pressed_keys[pg.K_RIGHT]:
                  self.rect.move_ip(JAKESPEED+SCORECOIN1//10, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)  

JAKE=Player()

class Coins(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.mode=random.randint(0,20)
        if self.mode==0:
            self.image=pg.image.load("coin2.png")
        else:
            self.image = pg.image.load("coin.png")
        self.rect = self.image.get_rect()
        mylist1=[*range(20, max(JAKE.rect.center[0]-50,20))]
        mylist2=[*range(min(JAKE.rect.center[0]+50, 768-20), 768-20)]
        mylist1.extend(mylist2)
        self.rect.center=(int(random.choice(mylist1)),525) 
    def update(self):
        self.mode=random.randint(0,20)
        if self.mode==0:
            self.image=pg.image.load("coin2.png")
        else:
            self.image = pg.image.load("coin.png")
        mylist1=[*range(20, max(JAKE.rect.center[0]-50,20))]
        mylist2=[*range(min(JAKE.rect.center[0]+50, 768-20), 768-20)]
        mylist1.extend(mylist2)
        self.rect.center=(int(random.choice(mylist1)),525)
    def draw(self, surface):
        surface.blit(self.image, self.rect)  
 


E1=Enemy()
COINS=Coins()

enemies = pg.sprite.Group()
enemies.add(E1)

regards=pg.sprite.Group()
regards.add(COINS)

all_sprites = pg.sprite.Group()
all_sprites.add(JAKE)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 10000)

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==INC_SPEED:
            ENEMYSPEED+=1
    SCORE=CNTENEMY+SCORECOIN1//20+SCORECOIN2
    text1 = f1.render("x{}".format(str(SCORE)),False,(255, 255, 255))
    text2 = f1.render("x{}".format(str(SCORECOIN1)),False,(255, 255, 255))
    text3 = f1.render("x{}".format(str(SCORECOIN2)),False,(255, 255, 255))
    if deadscreen:
        screen.blit(bg1,(0,0))

        tex1=f2.render("TOTAL SCORE:{}".format(str(SCORE)),True,(255, 255, 255))
        rect=tex1.get_rect()
        rect.center=(200,470)

        tex2=f2.render("SMALL COINS:{}".format(str(SCORECOIN1)),True,(255, 255, 255))
        rect2=tex2.get_rect()
        rect2.center=(200,505)

        tex3=f2.render("BIG COINS:{}".format(str(SCORECOIN2)),True,(255, 255, 255))
        rect3=tex3.get_rect()
        rect3.center=(200,540)

        screen.blit(tex1, rect)
        screen.blit(tex2,rect2)
        screen.blit(tex3,rect3)
    else:
        screen.blit(bg, (0,0))
        screen.blit(COINS.image, COINS.rect)
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()
        screen.blit(text2, (38,7))

        screen.blit(text3, (768-40,7))

        screen.blit(text1, (7,39))

    if pg.sprite.spritecollideany(JAKE, regards):
          COINS.update()
          if COINS.mode==0:
              SCORECOIN2+=1
          else:
              SCORECOIN1+=1
 
    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(JAKE, enemies):
          pg.display.update()
          mixer.music.stop()
          mixer.music.load("gameover.mp3")
          mixer.music.set_volume(0.3)
          mixer.music.play(-1)
          for entity in all_sprites:
                entity.kill() 
          deadscreen=True

    
    pg.display.update()
    clock.tick(60)