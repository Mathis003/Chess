"""ALL THE CONSTANT CONFIGS"""

# Size of a tile in pixels
SQUARE = 100
# Number of rows and columns on the board
ROW = 8
COL = 8
# Size of the screen
WIDTH, HEIGHT = SQUARE * COL, SQUARE * ROW

# Colors
# Basic board colors (brown)
DARK_COLOR_BROWN = "#A87965" # Color of the dark square (to draw the board)
LIGHT_COLOR_BROWN = "#F0D8C0" # Color of the light square (to draw the board)
COLOR_PLAYER_BEFORE_MOVE_BROWN = (190, 152, 53) # Color of the square before the move when the player click on it
COLOR_PLAYER_AFTER_MOVE_BROWN = (245, 225, 99) # Color of the square where the player moved
# Basic board colors (green)
DARK_COLOR_GREEN = (118,150,85)
LIGHT_COLOR_GREEN = (238,238,212)
COLOR_PLAYER_BEFORE_MOVE_GREEN = (186,203,73)
COLOR_PLAYER_AFTER_MOVE_GREEN = (247,245,126)
# Basic board colors (blue)
DARK_COLOR_BLUE = (75,115,153)
LIGHT_COLOR_BLUE = (234,233,210)
COLOR_PLAYER_BEFORE_MOVE_BLUE = (38,140,204)
COLOR_PLAYER_AFTER_MOVE_BLUE = (117,199,232)
# Other colors
COLOR_POSSIBLE_MOVES_LIGHT = (219, 59, 87) # Light color of the square (to draw the possible moves on light square only)
COLOR_POSSIBLE_MOVES_DARK = (182, 33, 60) # Dark color of the square (to draw the possible moves on dark square only)