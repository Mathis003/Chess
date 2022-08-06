"""ALL THE CONSTANT CONFIGS"""

# Size of a tile in pixels
SQUARE = 100
# Number of rows and columns on the board
ROW = 8
COL = 8
# Size of the screen
WIDTH, HEIGHT = SQUARE * COL, SQUARE * ROW

# Colors
DARK_COLOR = "#A87965" # Color of the dark square (to draw the board)
LIGHT_COLOR = "#F0D8C0" # Color of the light square (to draw the board)
COLOR_PLAYER_BEFORE_MOVE = (190, 152, 53, 0.8) # Color of the square before the move when the player click on it
COLOR_PLAYER_AFTER_MOVE = (245, 225, 99, 0.8) # Color of the square where the player moved
COLOR_POSSIBLE_MOVES_LIGHT = (219, 59, 87, 0.8) # Light color of the square (to draw the possible moves on light square only)
COLOR_POSSIBLE_MOVES_DARK = (182, 33, 60, 0.8) # Dark color of the square (to draw the possible moves on dark square only)