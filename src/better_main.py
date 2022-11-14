import pygame
from sys import exit 
pygame.init()
class Game: 
    def __init__(self,width, height):
        self.screen = pygame.display.set_mode((800,400))
        self.tittle = pygame.display.set_caption('Drizzo')
        self.loop =  True
             #event loop
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()  # Un-inits pygame.
                exit(0)  # Safer than `break`.
                                #cornet's                            
            
                                    