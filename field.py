import pygame
from settings import *
from rules import *

vec = pygame.math.Vector2

class Field(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        # Draw Boundary
        self.image = pygame.Surface((BOUND_RIGHT, BOUND_BOTTOM))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        middle = BOUND_BOTTOM / 2
        pygame.draw.rect(self.image, GRASS, [TOUCH_LEFT, DEAD_TOP, TOUCH_WIDTH, DEAD_HEIGHT])
        pygame.draw.rect(self.image, WHITE, [TOUCH_LEFT, DEAD_TOP, TOUCH_WIDTH, DEAD_HEIGHT], 4)
        # Middle Line
        pygame.draw.line(self.image, WHITE, [TOUCH_LEFT, middle], [TOUCH_RIGHT, middle], 3)
        # Touch Lines
        pygame.draw.line(self.image, WHITE, [TOUCH_LEFT, TRY_TOP], [TOUCH_RIGHT, TRY_TOP], 3)
        pygame.draw.line(self.image, WHITE, [TOUCH_LEFT, TRY_BOTTOM], [TOUCH_RIGHT, TRY_BOTTOM], 3)
        # 22 M Lines Lines
        pygame.draw.line(self.image, WHITE, [TOUCH_LEFT, TRY_TOP + TWENTY_TWO], [TOUCH_RIGHT, TRY_TOP + TWENTY_TWO], 3)
        pygame.draw.line(self.image, WHITE, [TOUCH_LEFT, TRY_BOTTOM - TWENTY_TWO], [TOUCH_RIGHT, TRY_BOTTOM - TWENTY_TWO], 3)
        # 10 M Lines
        self.draw_horizontal_dashed_line(TOUCH_LEFT, middle - TEN, WHITE, 35, 3)
        self.draw_horizontal_dashed_line(TOUCH_LEFT, middle + TEN, WHITE, 35, 3)
        # 5 M Lines
        self.draw_horizontal_dashed_line(TOUCH_LEFT, TRY_TOP + FIVE, WHITE, 35, 3)
        self.draw_horizontal_dashed_line(TOUCH_LEFT, TRY_BOTTOM - FIVE, WHITE, 35, 3)
        # 5 M Tram Lines
        self.draw_tram_line(TOUCH_LEFT + FIVE, TRY_TOP, WHITE, 50, 2)
        self.draw_tram_line(TOUCH_RIGHT - FIVE, TRY_TOP, WHITE, 50, 2)
        # Draw 15 lines
        self.draw_fifteen_line(TOUCH_LEFT + FIFTEEN, TRY_TOP, WHITE, 2)
        self.draw_fifteen_line(TOUCH_RIGHT - FIFTEEN, TRY_TOP, WHITE, 2)
        self.game = game
        # self.draw_field()
        # should not be center
        self.rect.center = (BOUND_RIGHT / 2, BOUND_BOTTOM / 2)
        self.position = self.rect.center
        self.velocity = pygame.math.Vector2(0, 0)

    def draw_horizontal_dashed_line(self, x, y, color, dashes, width):
        start_with_line = dashes % 2
        for c in range(0, dashes):
            draw = c % 2
            if start_with_line == draw:
                pygame.draw.line(self.image, color, [x, y], [x + TWO, y], width)
            x += TWO

    def draw_tram_line(self, x, y, color, dashes, width):
        start_with_line = dashes % 2
        for c in range(0, dashes):
            draw = c % 2
            if start_with_line == draw:
                pygame.draw.line(self.image, color, [x, y], [x, y + TWO], width)
            y += TWO

    def draw_fifteen_line(self, x, y, color, width):
        dashes = 25
        start_with_line = dashes % 4
        for c in range(0, dashes):
            draw = c % 4
            if start_with_line == draw:
                pygame.draw.line(self.image, color, [x, y], [x, y + FOUR], width)
            y += FOUR
