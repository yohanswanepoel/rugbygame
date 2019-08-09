# Sprite classes for platform game
import pygame
from settings import *
from rules import *

vec = pygame.math.Vector2

class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.height = 0
        self.vel_height = 0
        self.acc_height = 0
        self.image = pygame.Surface((width, height))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = None
        self.acceleration = vec(0, 0)
        self.position = vec(x, y)
        self.velocity = vec(0, 0)

    def update(self):
        if self.player:
            self.velocity.x = self.player.velocity.x
            self.velocity.y = self.player.velocity.y
            self.rect.center = self.player.rect.center
            self.position.x = self.player.position.x
            self.position.y = self.player.position.y
            self.height = 0
        else:
            # self.position = self.rect.center
            # Adjust the acceleration by friction
            # The faster you go the more friction applies
            # Standard equations for motion
            if self.vel_height > 0 or self.height > 0:
                self.acc_height = GRAVITY
                self.acc_height += self.vel_height * BALL_AIR_FRICTION
                self.vel_height += self.acc_height
                self.height += self.vel_height
                self.velocity += (self.velocity * BALL_AIR_FRICTION)
            else:
                self.velocity += (self.velocity * BALL_GROUND_FRICTION)

        # Draw different for now - until figure out how to show flight
        if self.height > 3:
            self.image.fill(RED)
        else:
            self.image.fill(GREY)

        self.position += self.velocity
        self.rect.center = self.position



