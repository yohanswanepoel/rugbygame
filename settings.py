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
GREY = (224, 224, 224)
GRASS = (0, 153, 0)

# Field Dimensions
# 100mX50m
# Dead ball area 15m
# Total 130m x 50m
# 450px left of 0, 450px right of Max
BOUND_LEFT = 0
BOUND_RIGHT = 2250

BOUND_TOP = 0
BOUND_BOTTOM = 3500

# Touch Left/Right 325
TOUCH_LEFT = BOUND_LEFT + 250
TOUCH_WIDTH = 1750
TOUCH_RIGHT = TOUCH_LEFT + TOUCH_WIDTH

# DEADBALL AND BOUDNARY 1145
DEAD_TOP = BOUND_TOP + 125
DEAD_BOTTOM = BOUND_BOTTOM - 125
DEAD_HEIGHT = 3250

# TRY LINE offset 770
TRY_TOP = BOUND_TOP + 500
TRY_BOTTOM = BOUND_BOTTOM - 500

FIFTEEN = 375
TWENTY_TWO = 550
TEN = 250
FIVE = 125
TWO = 50
FOUR = 100


# View Port Settings
# 70m by 24m
# Goes over sideline by 7m
# Pixel to metric mapping 960/70 = 11.42pixels per meter

GRAVITY = -9.8

PLAYER_ACC = 0.5
PLAYER_ACC_SLOW = 0.9
PLAYER_ACC_MED = 1.0
PLAYER_ACC_FAST = 1.1
PLAYER_FRICTION = -0.08
BALL_AIR_FRICTION = -0.03
BALL_GROUND_FRICTION = -0.10
PASS_POP = 10
PASS_STRONG = 27
KICK_STRONG = 40
KICK_SHORT = 20

