# This is a pygame template sceleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
from player import *
from camera import *
from rules import *
from field import *
from ball import *

# @TODO
# Players follow ball - line up in positions
# Active player should be able to stop
# Ball is center of Y on screen
# Pass in tackle (back, left, right)
# Pass back in stead of kick


class Game:

    def __init__(self):
        # Initialise Game window and other things
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.all_sprites = None
        self.platforms_group = None
        self.player = None
        self.playing = False
        self.active_player = None
        self.rules = Rules(self)

    def new(self):
        # Start a new game
        self.all_sprites = pg.sprite.Group()
        self.player1_team = pg.sprite.Group()
        self.player2_team = pg.sprite.Group()
        self.all_actors = pg.sprite.Group()
        self.camera = Camera(BOUND_RIGHT, BOUND_BOTTOM)
        self.field = Field(self)
        self.center = pg.math.Vector2(BOUND_RIGHT / 2, BOUND_BOTTOM / 2)
        self.player1 = Player(self, PLAYER_ACC_FAST, True, BOUND_RIGHT / 2, BOUND_BOTTOM / 2, Direction.UP)
        self.player2 = Player(self, PLAYER_ACC_MED, False, BOUND_RIGHT / 2 + 50, BOUND_BOTTOM / 2, Direction.UP)
        self.ball = Ball(*self.player1.position,8,8)
        self.ball.player = self.player1
        self.active_player = self.player1
        self.all_sprites.add(self.field)
        self.all_sprites.add(self.player1)
        self.all_sprites.add(self.player2)
        self.all_sprites.add(self.ball)
        self.all_actors.add(self.player1)
        self.all_actors.add(self.player2)
        self.all_actors.add(self.field)
        self.player1_team.add(self.player1)
        self.player1_team.add(self.player2)
        self.run()

    def run(self):
        # Game loop  
        # Process Input Events
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        # Game loop update
        self.all_sprites.update()
        self.camera.update(self.ball)
        # Check if passing/flying ball hits player
        if not self.ball.player:
            # Only do detection if ball is on the ground
            hits = None
            if self.ball.height <= 80:
                hits = pg.sprite.spritecollide(self.ball, self.player1_team, False)
                # Catch/pickup the ball
                if hits:
                    for player_hit in hits:
                        self.ball.player = player_hit
                        self.active_player = player_hit
            # Still no hits check closest player is active
            # need to compensate for offside
            if not hits:
                # Determine player closes to the ball
                ball_pos = pygame.math.Vector2(self.ball.rect.x, self.ball.rect.y)
                nearest_player = min([p for p in self.player1_team],
                                     key=lambda p: ball_pos.distance_to(pygame.math.Vector2(p.position.x, p.position.y)))
                # set others inactive (there must be a better way)
                self.active_player = nearest_player

        if self.rules.check_ball_in_touch():
            self.rules.state = State.LINEOUT
            self.player2.position.x = self.ball.rect.centerx
            self.player2.position.y = self.ball.rect.centery
            self.player2.rect.centerx = self.ball.rect.centerx
            self.player2.rect.centery = self.ball.rect.centery
            self.ball.player = self.player2
            self.active_player = self.player2

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                # This should pick nearest player to the ball
                keys = pygame.key.get_pressed()
                if keys[pygame.K_b]:
                    self.active_player = self.player
                if keys[pygame.K_m] and self.rules.state == State.LINEOUT:
                    # Throw the ball in
                    if self.ball.rect.centerx <= TOUCH_LEFT:
                        self.player2.pass_ball(1, 0)
                    if self.ball.rect.centerx >= TOUCH_RIGHT:
                        self.player2.pass_ball(-1, 0)
                    self.rules.state = State.INPLAY

    def draw(self):
        # Game loop draw
        # Render Draw
        self.screen.fill(BLACK)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        # After the drawing flip the screen to display
        pg.display.flip()
    
    def show_start_screen(self):
        pass
    
    def show_game_over_screen(self):
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_game_over_screen()

pg.quit()



# SET The assets folder
# game_folder = os.path.dirname(__file__) # gives us the folder that this file is running from
# img_folder = os.path.join(game_folder, 'img')

