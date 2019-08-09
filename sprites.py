# Sprite classes for platform game
import pygame
from settings import *
from rules import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    # Have to add fitness

    def __init__(self, game, acceleration, active, x, y, d):
        pygame.sprite.Sprite.__init__(self)
        self.has_ball = None
        # Shape is not quite square
        self.image = pygame.Surface((26,72))
        self.image.fill(YELLOW)
        self.game = game
        self.play_direction = int(d)
        self.speed = acceleration
        self.rect = self.image.get_rect()
        self.position = vec(x, y)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        self.friction = PLAYER_FRICTION
        self.rect.center = self.position

    def update(self):
        self.acceleration = vec(0, 0)
        in_goal = self.check_in_goal()
        has_ball = self.game.ball.player == self
        own_goal = self.check_own_in_goal()

        if self.game.active_player == self and self.game.rules.state == State.INPLAY:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.acceleration.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.acceleration.x += self.speed
            if keys[pygame.K_DOWN]:
                self.acceleration.y += self.speed
            if keys[pygame.K_UP]:
                self.acceleration.y -= self.speed
            if has_ball:
                if in_goal and keys[pygame.K_m]:
                    # Score try
                    print("Try")
                if own_goal and keys[pygame.K_m]:
                    # Score try
                    print("Own Goal")
                else:
                    if keys[pygame.K_j]:
                        self.kick_ball(self.play_direction)
                    if keys[pygame.K_RIGHT] and keys[pygame.K_m]:
                        self.pass_ball(Direction.RIGHT, self.play_direction * -2)
                    elif keys[pygame.K_LEFT] and keys[pygame.K_m]:
                        self.pass_ball(Direction.LEFT, self.play_direction * -2)
                    elif keys[pygame.K_m]:
                        self.pass_ball_back(-self.play_direction)

        # Adjust the acceleration by friction
        # The faster you go the more friction applies
        self.acceleration.x += self.velocity.x * self.friction
        self.acceleration.y += self.velocity.y * self.friction
        # Standard equations for motion
        self.velocity += self.acceleration
        self.position += self.velocity + PLAYER_ACC * self.acceleration

        # Set new position
        self.rect.center = self.position

    def check_in_goal(self):
        if self.play_direction == Direction.UP:
            if self.rect.top <= TRY_TOP:
                return True
        if self.play_direction == Direction.DOWN:
            if self.rect.bottom >= TRY_BOTTOM:
                return True
        return False

    def check_own_in_goal(self):
        if self.play_direction == Direction.UP:
            if self.rect.bottom >= TRY_BOTTOM:
                return True
        if self.play_direction == Direction.DOWN:
            if self.rect.top <= TRY_TOP:
                return True
        return False

    def pass_ball_back(self, fwd_back):
        self.game.ball.player = None
        self.game.active_player = None
        self.game.ball.vel_height = 50
        self.game.ball.rect.y += fwd_back * (self.rect.height / 2) + 5 * fwd_back
        self.game.ball.position.y += fwd_back * (self.rect.height / 2) + 5 * fwd_back
        self.game.ball.velocity.x = self.velocity.x * 5
        self.game.ball.velocity.y = fwd_back * (PASS_STRONG * .7)

    def pass_ball(self, left_right, fwd_back):
        self.game.ball.player = None
        self.game.active_player = None
        self.game.ball.vel_height = 50  # This is a strong pass
        self.game.ball.rect.x += left_right * self.rect.width / 2
        self.game.ball.position.x += left_right * self.rect.width / 2
        self.game.ball.velocity.x = left_right * PASS_STRONG
        self.game.ball.velocity.y = fwd_back

    def kick_ball(self, fwd_back):
        self.game.ball.player = None
        self.game.active_player = None
        self.game.ball.vel_height = 250
        self.game.ball.rect.y += fwd_back * (self.rect.height / 2) + 5
        self.game.ball.position.y += fwd_back * (self.rect.height / 2) + 5
        self.game.ball.velocity.x = self.velocity.x * 5
        self.game.ball.velocity.y = fwd_back * KICK_STRONG


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



