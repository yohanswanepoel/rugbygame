from enum import Enum
import pygame
from settings import *

class Rules:

    def __init__(self, game):
        self.game = game
        self.state = State.INPLAY

    def check_ball_in_touch(self):
        # Check if ball is in touch - this needs to notify the game
        if self.state != State.LINEOUT and (self.game.ball.rect.left <= TOUCH_LEFT or self.game.ball.rect.right >= TOUCH_RIGHT):
            self.game.ball.position.x = self.game.ball.rect.centerx
            self.game.ball.velocity.x = 0
            self.game.ball.velocity.y = 0
            self.game.ball.height = 0
            self.game.ball.vel_height = 0
            self.game.ball.player = None
            return True
        return False

class State(Enum):
    INPLAY = 1
    LINEOUT = 2
    KICK_OFF = 3
    DROP_OUT = 4
    PENALTY = 5
    SCRUM = 6
    RUCK = 7
    INJURY = 8
    HALF_TIME = 9


class Direction:
    UP = -1
    DOWN = 1
    LEFT = -1
    RIGHT = 1
