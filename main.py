import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)
    asteroidField = AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit(0)
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000
if __name__ == "__main__":
    main()

