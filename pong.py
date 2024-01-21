# Testing Git
import pygame
pygame.init()

window = pygame.display.set_mode((900,600))
window.fill((0,0,0))

height = 100
width = 20
y1 = 100
x1 = 35
v = 10
x2 = 845
y2 = 100

bx = 450
by = 300

dy = 5
dx = 5

cond = True
while cond:
     
    pygame.time.delay(25)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            cond = False

    bx += dx 
    by += dy
    
   
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s] and y1<600-height:
        y1 += v
    
    if keys[pygame.K_w] and y1>0:
        y1 -= v

    if keys[pygame.K_DOWN] and y2<600-height:
        y2 += v
    
    if keys[pygame.K_UP] and y2>0:
        y2 -= v

    #ball bounce walls
    if by>=590 or by <=10:
        dy *= -1

    if bx <=10 or bx >=890:
        dx *=-1

    #paddle ball interaction
    if bx +20 > x2 :
        if by - 10 > y2 and by+10 < y2 + height:
            dx *= -1 
          
    if by - 10 > y1 and by+10 < y1 + height:
            if bx -40 < x1 :
                dx *= -1 
            
      


        
    window.fill((0,0,0))
    pygame.draw.circle(window,(255,255,255),(bx,by),10)
    pygame.draw.rect(window,(255,255,255),[x1,y1,width,height],0)
    pygame.draw.rect(window,(255,255,255),[x2,y2,width,height],0)
    pygame.draw.line(window,(255,255,255),[450,0],[450,600],3)
    
    pygame.display.update()



