import math
import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile
# in terminal -> pip install pygame

SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
FPS = 60

##########################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pygame Picture")

# Player
player_group = pygame.sprite.Group()          # create sprite group for player
player = Player("Assets/sprite_ship_3.png")   # create player object
player_group.add(player)                      # add player to group

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # check for user input
        if event.type == pygame.QUIT:
            running = False

    # game logic

    screen.fill(WHITE)

    player_group.draw(screen)
    player_group.update()

    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()
