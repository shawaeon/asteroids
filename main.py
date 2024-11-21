"""Classic Asteroids game"""

import pygame
import sys

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import *

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers =(updatable)

    player = Player(x=(SCREEN_WIDTH / 2), y=(SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   

        for obj in updatable:
            obj.update(dt)

        # Collision detection between asteroids and player
        for obj in asteroids:
            if obj.collision(player):
                print("Game Over!")
                sys.exit()  

        screen.fill("black")        

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        # Framerate limited to 60 FPS        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()