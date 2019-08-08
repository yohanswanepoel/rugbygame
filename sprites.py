# Sprite classes for platform game
import pygame
from settings import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    # Have to add fitness

    def __init__(self, game, acceleration, active, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.has_ball = None
        # Shape is not quite square
        self.image = pygame.Surface((26,72))
        self.image.fill(YELLOW)
        self.game = game
        self.speed = acceleration
        self.rect = self.image.get_rect()
        self.position = vec(x, y)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        self.friction = PLAYER_FRICTION
        self.rect.center = self.position

    def update(self):
        self.acceleration = vec(0, 0)
        if self.game.active_player == self:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.acceleration.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.acceleration.x += self.speed
            if keys[pygame.K_DOWN]:
                self.acceleration.y += self.speed
            if keys[pygame.K_UP]:
                self.acceleration.y -= self.speed
            if keys[pygame.K_UP] and keys[pygame.K_SPACE]:
                if self.game.ball.player == self:
                    self.kick_ball(-1)
            if keys[pygame.K_DOWN] and keys[pygame.K_SPACE]:
                if self.game.ball.player == self:
                    self.kick_ball(1)
            if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
                if self.game.ball.player == self:
                    self.pass_ball(1, 2)
            if keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
                if self.game.ball.player == self:
                    self.pass_ball(-1, 2)
            if keys[pygame.K_SPACE]:
                if self.game.ball.player == self:
                    self.kick_ball(-1)


        # Adjust the acceleration by friction
        # The faster you go the more friction applies
        self.acceleration.x += self.velocity.x * self.friction
        self.acceleration.y += self.velocity.y * self.friction
        # Standard equations for motion
        self.velocity += self.acceleration
        self.position += self.velocity + PLAYER_ACC * self.acceleration

        # Set new position
        self.rect.center = self.position

    def pass_ball(self, left_right, fwd_back):
        self.game.ball.player = None
        self.game.active_player = None
        self.game.ball.rect.x += left_right * self.rect.width / 2
        self.game.ball.position.x += left_right * self.rect.width / 2
        self.game.ball.velocity.x = left_right * PASS_STRONG
        self.game.ball.velocity.y = fwd_back

    def kick_ball(self, fwd_back):
        self.game.ball.player = None
        self.game.active_player = None
        self.game.ball.vel_height = 30
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
                print(self.height)
            self.velocity += (self.velocity * BALL_AIR_FRICTION)

        self.position += self.velocity
        self.rect.center = self.position


class Field(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        # Draw Boundary
        self.image = pygame.Surface((BOUND_RIGHT, BOUND_BOTTOM))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        pygame.draw.rect(self.image, GRASS, [125, 125, TOUCH_WIDTH, DEAD_HEIGHT])
        pygame.draw.rect(self.image, WHITE, [125, 125, TOUCH_WIDTH, DEAD_HEIGHT], 4)
        # Middle Line
        pygame.draw.line(self.image, WHITE, [125, BOUND_BOTTOM / 2], [125 + TOUCH_WIDTH, BOUND_BOTTOM / 2], 3)
        # Touch Lines
        pygame.draw.line(self.image, WHITE, [125, TRY_TOP], [125 + TOUCH_WIDTH, TRY_TOP], 3)
        pygame.draw.line(self.image, WHITE, [125, TRY_BOTTOM], [125 + TOUCH_WIDTH, TRY_BOTTOM], 3)
        # 25 M Lines Lines
        # 10 M Lines
        self.game = game
        # self.draw_field()
        # should not be center
        self.rect.center = (BOUND_RIGHT / 2, BOUND_BOTTOM / 2)
        self.position = self.rect.center
        self.velocity = pygame.math.Vector2(0, 0)