import pygame
import sys
import random
import psycopg2

pygame.init()

conn = psycopg2.connect(
   host = "localhost", 
   database = "postgres", 
   user = "postgres", 
   password = "12345")

cursor = conn.cursor()

cursor.execute(
   '''CREATE TABLE IF NOT EXISTS usertable(
   username varchar(100),
   user_score int,
   user_level int
   )'''
)
conn.commit()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

sec = 0
blocksize = 15
fps = 10
lev = 0
sc = 0
lvl = 0
done = True
lvlfont = pygame.font.SysFont("Verdana", 30)
scfont = pygame.font.SysFont("Verdana", 30)
pause = False

time_event = pygame.USEREVENT
pygame.time.set_timer(time_event, 1000)

def insertname(username):
   cursor.execute("INSERT INTO usertable VALUES('{}', 0, 0)".format(username))
   conn.commit()

def upd(user):
   cursor.execute("SELECT * FROM usertable WHERE username = '{}'".format(user))
   row = cursor.fetchone()
   cursor.execute("UPDATE usertable SET user_score = '{}', user_level = '{}' WHERE username = '{}'".format(max(row[1], sc), max(row[2], lvl), user))
   conn.commit()

print("Enter your name")
username = input()
cursor.execute("SELECT count(*) FROM usertable WHERE username='{}'".format(username))
conn.commit()
if cursor.fetchone()[0] == 0:
   insertname(username)
   conn.commit()
else:
   cursor.execute("SELECT * FROM usertable WHERE username = '{}'".format(username))
   data=cursor.fetchone()
   print("User's max score:{}".format(data[1]))
   print("User's max level:{}".format(data[2]))

class GoldApple:
   def __init__(self):
      self.x = int(random.randint(0, 500)/ blocksize) * blocksize
      self.y = int(random.randint(0, 500)/ blocksize) * blocksize
      self.rect = pygame.Rect(self.x, self.y, blocksize, blocksize)
   def update(self):
      pygame.draw.rect(screen, 'yellow', self.rect)

class Apple:
   def __init__(self):
      self.x = int(random.randint(0, 500)/ blocksize) * blocksize
      self.y = int(random.randint(0, 500)/ blocksize) * blocksize
      self.rect = pygame.Rect(self.x, self.y, blocksize, blocksize)
   def update(self):
      pygame.draw.rect(screen, 'red', self.rect)

class Snake:
   def __init__(self):
      self.x, self.y = blocksize, blocksize
      self.xdir, self.ydir = 1, 0
      self.body = [pygame.Rect(self.x, self.y, blocksize, blocksize)]
      self.head = self.body[0]
      self.dead = False
   def update(self):
      global apple
      global lvl
      global sc
      global fps
      for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
               self.dead = True
               upd(username)
            if self.head.x not in range(0, 500) or self.head.y not in range(0, 500):
               self.dead = True
               upd(username)
      if self.dead:
            fps = 12
            self.x, self.y = blocksize, blocksize
            self.head = pygame.Rect(self.x, self.y, blocksize, blocksize)
            self.body = [pygame.Rect(self.x, self.y, blocksize, blocksize)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
            sc = 0
            lvl = 0
      self.body.append(self.head)
      for i in range(len(self.body) - 1):
         self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
      self.head.x += self.xdir * blocksize
      self.head.y += self.ydir * blocksize 
      self.body.remove(self.head)
flag = True
def drawgrid():
   for x in range(0, 500, blocksize):
      for y in range(0, 500, blocksize):
         rect = pygame.Rect(x, y, blocksize, blocksize)
         pygame.draw.rect(screen, (255, 255, 255), rect, 1)
apple = Apple()
snake = Snake()
goldapple = GoldApple()

while done:
   for event in pygame.event.get():
      if event.type == time_event:
         sec += 1
      if event.type == pygame.QUIT:
         done = False
         cursor.close()
         conn.close()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
            snake.xdir, snake.ydir = 0, -1
         elif event.key == pygame.K_DOWN:
            snake.xdir, snake.ydir = 0, 1
         elif event.key == pygame.K_LEFT:
            snake.xdir, snake.ydir = -1, 0
         elif event.key == pygame.K_RIGHT:
            snake.xdir, snake.ydir = 1, 0
         if event.key == pygame.K_SPACE:
            upd(username)
            pause = True
   while pause:   
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            cursor.close()
            conn.close()
            sys.exit()
         if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
            pause = False
      unpause = lvlfont.render('Press u to unpause', True, 'white')
      screen.blit(unpause, unpause.get_rect(center = (500 // 2, 500 // 2)))
      pygame.display.update()

   if sec > 5:
      apple = Apple()
      sec = 0

   snake.update()
   screen.fill('black')
   
   score = scfont.render(f" Your score: {sc}", True, (0, 0, 255))
   screen.blit(score, (0, 0))
   level = lvlfont.render(f"Your level: {lvl}", True, (0, 0, 255))
   screen.blit(level, (500 - 200, 0))
   if flag:
      apple.update()
   if flag == False:
      goldapple.update()

   pygame.draw.rect(screen, 'green', snake.head)

   for body in snake.body:
      pygame.draw.rect(screen, 'green', body)
   
   #eating
   if snake.head.x == apple.x and snake.head.y == apple.y:
      sec = 0
      snake.body.append(pygame.Rect(body.x, body.y,blocksize, blocksize))
      rand = int(random.randint(0, 4))
      if rand == 0:
         flag = False
         goldapple = GoldApple()
      else:
         flag = True
         apple = Apple()
      sc += 1
      if sc % 2 == 0:
         fps += 1
         lvl += 1

   #eating goldapple
   if snake.head.x == goldapple.x and snake.head.y == goldapple.y:
      sec = 0
      for i in range(4):
         snake.body.append(pygame.Rect(body.x, body.y,blocksize, blocksize))
      sc += 4
      rand = int(random.randint(0, 4))
      if rand == 0:
         flag = False
         goldapple = GoldApple()
      else:
         flag = True
         apple = Apple()
      fps += 2
      lvl += 2
   
   
   clock.tick(fps)
   pygame.display.update()