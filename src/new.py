import pygame
from sys import exit
import threading
import time 

pygame.init()

screen=pygame.display.set_mode((800,400))

pygame.display.set_caption('Test')
game_active = True

#game obj 
background= pygame.image.load("Sprites/End.jep").convert_alpha()




#main loop 

while True: 
    #evnt loop/need to run all the time 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    