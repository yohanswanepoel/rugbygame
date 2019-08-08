# This is a pygame template sceleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
from sprites import *

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

    def new(self):
        # Start a new game
        self.all_sprites = pg.sprite.Group()
        self.player1_team = pg.sprite.Group()
        self.player2_team = pg.sprite.Group()
        self.all_actors = pg.sprite.Group()
        self.field = Field()
        self.center = pg.math.Vector2(WIDTH / 2, HEIGHT / 2)
        self.camera = pg.math.Vector2(0, 0)
        self.player1 = Player(self, PLAYER_ACC_FAST, True, WIDTH / 2, HEIGHT / 2)
        self.player2 = Player(self, PLAYER_ACC_MED, False, WIDTH / 2 + 50, HEIGHT / 2)
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
            print(self.ball.rect.center)
            print(self.ball.velocity.y)
            self.event()
            self.update()
            self.draw()

    def update(self):
        # Game loop update
        self.all_sprites.update()
        # Check if passing/flying ball hits player
        if not self.ball.player:
            # Only do detection if ball is on the ground
            hits = None
            if self.ball.height <= 2:
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

        # Follow the ball
        delta_x = 0
        delta_y = 0

        if self.ball.rect.centerx != (WIDTH / 2):
            delta_x = self.ball.rect.centerx - (WIDTH / 2)

        # Follow the ball Doing my head in
        if self.ball.rect.centery > (HEIGHT / 2):
            self.ball.position.y -= abs(self.ball.velocity.y)
            for p in self.all_actors:
                p.rect.y -= abs(self.ball.velocity.y)

        if self.ball.rect.centery < (HEIGHT / 2):
            self.ball.position.y += abs(self.ball.velocity.y)
            for p in self.all_actors:
                p.rect.y += abs(self.ball.velocity.y)

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
                    self.active_player = self.player1

    def draw(self):
        # Game loop draw
        # Render Draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
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

