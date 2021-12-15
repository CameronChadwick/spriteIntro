import pygame
pygame.init()

# color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
BLOCK_COLOR = (252, 53, 3)

# explosion images
EXPLOSION_LIST = []
for i in range(8):
    image_path = pygame.image.load(f"assets/sprite_{i}.png")
    EXPLOSION_LIST.append(image_path)

# font
SM_FONT = pygame.font.Font("Assets/unifont.ttf", 32)
MED_FONT = pygame.font.Font("Assets/unifont.ttf", 38)
LRG_FONT = pygame.font.Font("Assets/unifont.ttf", 44)

# game constants
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 700

# missile variables
MISSILE_WIDTH = 5
MISSILE_HEIGHT = 15

# enemy sprites
RED_ALIEN = "Assets/red.png"
GREEN_ALIEN = "Assets/green.png"
YELLOW_ALIEN = "Assets/yellow.png"

# shield blocks
BLOCK_WIDTH = 7
BLOCK_HEIGHT = 7

SHEILD = ["  xxxxxxx",
          " xxxxxxxxx",
          "xxxxxxxxxxx",
          "xxxxxxxxxxx",
          "xxxxxxxxxxx",
          "xxx     xxx",
          "xx       xx"]
