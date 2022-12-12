
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

#background
sky_surface= pygame.image.load("Sprites/pixil-frame-0_1.JPEG").convert_alpha()

ground_surface = pygame.image.load("Sprites/ground.png").convert_alpha()

                                                        #makes it easier for pygame/ makes game run faster
snail_surface = pygame.image.load("Sprites/snail1.png").convert_alpha()
snail_rec = snail_surface.get_rect( bottomright= (600,300))

player_surface = pygame.image.load("Sprites/player_walk.png").convert_alpha()
              #make a rectangle                 #x #y
player_retc = player_surface.get_rect( midbottom  = (80,300))

score_rect = score_surface.get_rect(center=(400,50))
player_gravity = 0
game_active = True 


#main loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        
         #key input 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #controls how heigh it gose up
             player_gravity = -20
            player_retc.y += player_gravity
               
                 
        
                 
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_retc.collidepoint(event.pos):
                player_gravity = -20
                player_retc.y += player_gravity
                
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active  =  True 
                    snail_rec.left = -20
                 
    screen.blit(sky_surface,(0,0))    # Add surface to the screen.
    screen.blit(ground_surface,(0,300))
        #puts it on the screen   #highlets it pink #makes the my game pink
                                        #parceley makes it pink
    pygame.draw.rect(screen,'#c0e8ec',score_rect,100)
        


    if game_active:
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
            
        mouse_pos = pygame.mouse.get_pos()

        #draw all our elements/updates everything
        pygame.display.update()

        #collision 
        if snail_rec.colliderect(player_retc):
            game_active = False  
    else:
        screen.fill('Yellow')    
    
    clock.tick(60)               
    
#import sound MAKE SURE TO MAKE S CAPTIOAL 
pygame.mixer.Sound('')