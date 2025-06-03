import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def setup_groups_and_containers():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    return {
        'updatable': updatable,
        'drawable': drawable,
        'asteroids': asteroids,
        'shots': shots
    }


def main():
    pygame.init()
    groups = setup_groups_and_containers()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)
    asteroidField = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        groups['updatable'].update(dt)
        for asteroid in groups['asteroids']:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit(0)
            for shot in groups['shots']:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()
        for item in groups['drawable']:
            item.draw(screen)
        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000
if __name__ == "__main__":
    main()


