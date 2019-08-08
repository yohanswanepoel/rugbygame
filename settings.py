# Game options and settings
WIDTH = 960 #width of the game window
HEIGHT = 600 #height of the game window
FPS = 30 #frames per second that the game runs
TITLE = "Rugby"
# Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Field Dimensions
# 100mX50m
# Dead ball area 15m
# Total 130m x 50m
# 450px left of 0, 450px right of Max
BOUND_LEFT = 0
BOUND_RIGHT = 1500

BOUND_TOP = 0
BOUND_BOTTOM = 3500

# Touch Left/Right 325
TOUCH_LEFT = BOUND_LEFT + 125
TOUCH_RIGHT = BOUND_RIGHT - 125
TOUCH_WIDTH = 2500

# DEADBALL AND BOUDNARY 1145
DEAD_TOP = BOUND_TOP + 25
DEAD_BOTTOM = BOUND_BOTTOM - 25
DEAD_HEIGHT = 3250

# TRY LINE offset 770
TRY_TOP = BOUND_TOP + 500
TRY_BOTTOM = BOUND_BOTTOM - 500


# View Port Settings
# 70m by 24m
# Goes over sideline by 7m
# Pixel to metric mapping 960/70 = 11.42pixels per meter

GRAVITY = -4

PLAYER_ACC = 0.5
PLAYER_ACC_SLOW = 0.7
PLAYER_ACC_MED = 0.8
PLAYER_ACC_FAST = 0.9
PLAYER_FRICTION = -0.12
BALL_AIR_FRICTION = -0.05
BALL_GROUND_FRICTION = -0.15
PASS_STRONG = 15
PASS_POP = 3
KICK_STRONG = 25
KICK_SHORT = 10

