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

# sounds
fire_sound = pygame.mixer.Sound("Assets/shoot.wav")

# sprite groups
player_group = pygame.sprite.Group()   # create sprite group for player
enemy_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()           # group for all sprites
missile_group = pygame.sprite.Group()

# Player
player = Player("Assets/player.png")   # create player object
player_group.add(player)                      # add player to group
all_sprites.add(player)

# Enemy
for row in range(5):
    for col in range(11):

        enemy = Enemy("Assets/red.png", col*50, row*1.5, row)
        all_sprites.add(enemy)
        enemy_group.add(enemy)


clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile = Missile(player.rect.centerx - MISSILE_WIDTH//2,
                                  player.rect.top)
                missile_group.add(missile)
                all_sprites.add(missile)
                fire_sound.play()

    # game logic

    screen.fill(WHITE)

    missile_group.draw(screen)
    player_group.draw(screen)
    enemy_group.draw(screen)
    all_sprites.update()

    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()
