
import pygame
from sys import exit
import threading
import time 

# Display Surface/ The Game window. anything displayed gose on here
pygame.init()
#makes screen
screen = pygame.display.set_mode((800,400))

#set's tittle
pygame.display.set_caption('Drizzo')
#Imporant
clock = pygame.time.Clock() #Clock obj that controls fps

#game obj
test_surface = pygame.Surface((200,100))  # Surface object (basically a sprite)/make part of the surface red
test_surface.fill('Red')  # Make the surface red.

#how the letter look
test_font = pygame.font.Font(None, 50)

                                #text      #AA    #color/RGB
score_surface = test_font.render('My Game',False, (64,64,64))

sky_surface= pygame.image.load("Sprites/background.png").convert_alpha()
ground_surface = pygame.image.load("Sprites/ground.png").convert_alpha()

                                                        #makes it easier for pygame/ makes game run faster
snail_surface = pygame.image.load("Sprites/snail1.png").convert_alpha()
snail_rec = snail_surface.get_rect( bottomright= (600,300))

player_surface = pygame.image.load("Sprites/player_walk.png").convert_alpha()
              #make a rectangle                 #x #y
player_retc = player_surface.get_rect( midbottom  = (80,300))

score_rect = score_surface.get_rect(center=(400,50))
player_gravity = 0


#main loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        
         
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #controls how heigh it gose up
             player_gravity = -20
            player_retc.y += player_gravity
               
                 
        
                 
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_retc.collidepoint(event.pos):
                player_gravity = -20
                player_retc.y += player_gravity
               
                 
    screen.blit(sky_surface,(0,0))    # Add surface to the screen.
    screen.blit(ground_surface,(0,300))
        #puts it on the screen   #highlets it pink #makes the my game pink
                                        #parceley makes it pink
    pygame.draw.rect(screen,'#c0e8ec',score_rect,100)
        



    screen.blit(score_surface,score_rect)

    snail_rec.x -=1
    screen.blit(snail_surface,(snail_rec))
    player_retc.left += 1
    if snail_rec.right <= 0: snail_rec.left = 800
                                 #left #right
                        
    #player
    screen.blit(player_surface,(player_retc))
    player_gravity += 1
    player_retc.y += player_gravity
    if player_retc.bottom >= 300: player_retc.bottom = 300
    screen.blit(player_surface,player_retc)
        #erither get false or true  if get flase no conllison and if get true has conllison
    # if  player_retc.colliderect(snail_rec):
       # print ('collision')
                #gets mouse movment
    mouse_pos = pygame.mouse.get_pos()
    # can tell if mouse is clicked/ able to see if what mouse bottone was clicked
    #if player_retc.collidepoint(( mouse_pos)):
        #print (pygame.mouse.get_pressed())


    #draw all our elements/updates everything
    pygame.display.update()

    clock.tick(60)
    #prints fps in terminal
    print(clock)               