# PoNg
#importing pygame library
import pygame
pygame.init()
#variables
p1Score = 0
plx = 20
ply = 200
comScore = 0
comx = 660
comy = 200
#ball variables
bx = 350 #xposition
by = 250 #yposition
bVx = 5 #horizontal speed
bVy = 5 #vertical speed
#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
#open a new window
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")
#loops until game is closed
carryOn = True
#clock controls how fast the screen updates
clock = pygame.time.Clock()


#main program loop-------------------------------------------
while carryOn:
   #60 fps limit
  #timer/keyboard input
  clock.tick(60)
  for event in pygame.event.get():#user did something
    if event.type == pygame.QUIT:#user QUIT
     carryOn = False #shows that we're done

  #game logic goes here (physics)
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    ply-=5
  if keys[pygame.K_s]:
    ply+=5
  if keys[pygame.K_UP]:
    comy-=5
  if keys[pygame.K_DOWN]:
    comy+=5
  #ball movement
  bx += bVx
  by += bVy
  #reflecting ball off walls, scoring points
  if bx < 0:
    bVx *= -1
    comScore +=1
  if bx + 20 > 700:
    bVx *= -1
    p1Score +=1
  if by < 0 or by + 20 > 500:
    bVy *= -1
  #bouncing off paddles
  if bx < plx + 20 and by + 20 > ply and by < ply + 100:
    bVx *= -1
  if bx+20 > comx and by + 20 > comy and by < comy + 100:
    bVx *= -1
  #render section##############################
  screen.fill(BLACK)
  #display score
  font = pygame.font.Font(None,74)#use default font
  text = font.render(str(p1Score), 1, (255, 255, 255))
  screen.blit(text, (250,10))
  text = font.render(str(comScore), 1, (255, 255, 255))
  screen.blit(text, (420,10))


  
  pygame.draw.rect(screen, (255,255,255), (plx,ply,20,100), 1)
  pygame.draw.rect(screen, (255,255,255), (comx,comy,20,100), 1)
  pygame.draw.rect(screen, (255,255,255), (bx,by,20,20), 1)
  #draw the net
  pygame.draw.line(screen,WHITE,[349,0], [349,500], 5)
  #update screen with drawing
  pygame.display.flip()
 
#closing main program loop--------------------------------------
pygame.quit()
