import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.move_multiplier = 1
        self.boost_duration = 2
        self.boost_cooldown = 0
        self.is_boosting = False
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if self.is_boosting is True:
            self.boost_duration -= dt
            if self.boost_duration <= 0:
                self.is_boosting = False
                self.move_multiplier = 1
                self.boost_cooldown = 5
                self.boost_duration = 2
        else:
            self.boost_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_LSHIFT]:
            self.boost()
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * self.move_multiplier

    def shoot(self):
        if not self.shot_cooldown > 0:
            shot = Shot(self.position, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    def boost(self):
        if self.boost_cooldown <= 0 and self.is_boosting is False:
            self.is_boosting = True
            self.move_multiplier = 2
