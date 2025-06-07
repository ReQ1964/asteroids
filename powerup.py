import pygame
from circleshape import CircleShape
from constants import *
import random


class Powerup(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 10)
