"""Classic Asteroids game"""

import pygame
from player import Player

from constants import *

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x=(SCREEN_WIDTH / 2), y=(SCREEN_HEIGHT / 2))
    dt = 0

    while True:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   
             
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        
        # Framerate limited to 60 FPS        
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()