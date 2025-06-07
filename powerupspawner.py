import pygame
import random
from asteroid import Asteroid
from constants import *
from powerup import Powerup

class PowerupSpawner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, x, y):
        powerup = Powerup(x, y, radius)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > POWERUP_SPAWN_RATE:
            self.spawn_timer = 0
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)

            print(x, y) 
            self.spawn(POWERUP_RADIUS, x, y)
