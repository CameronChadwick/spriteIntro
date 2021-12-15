import math
import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile, Block, Explosion
# in terminal -> pip install pygame

SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
FPS = 60

##########################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pygame Picture")

# sounds
fire_sound = pygame.mixer.Sound("Assets/shoot.wav")
enemy_kill = pygame.mixer.Sound("Assets/invaderkilled.wav")

# score
score = 0
score_object = SM_FONT.render(f"Score: {score}", True, WHITE)
score_rect = score_object.get_rect()
score_rect.center = 100, 20

# sprite groups
player_group = pygame.sprite.Group()   # create sprite group for player
enemy_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()           # group for all sprites
missile_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

# Player
player = Player("Assets/player.png")   # create player object
player_group.add(player)                      # add player to group
all_sprites.add(player)

# Enemy
offset_x = 30
offset_y = 100
v_scale = DISPLAY_HEIGHT // 18
h_scale = DISPLAY_WIDTH // 12
for row in range(5):
    if row == 1:
        enemy_img = RED_ALIEN
    elif 1 < row < 4: enemy_img = GREEN_ALIEN
    else:
        enemy_img = YELLOW_ALIEN
    for col in range(11):
        x_pos = col*h_scale + offset_x
        y_pos = row*v_scale + offset_y
        enemy = Enemy(enemy_img, x_pos, y_pos)
        enemy_group.add(enemy)

# create shields
start_values = [75, 200, 325, 450]
for start in start_values:
    for row_index, row in enumerate(SHEILD):
        # print(row_index, row)
        for col_index, col in enumerate(row):
            if col == 'x':
                x_pos = col_index*BLOCK_WIDTH + start
                y_pos = row_index*BLOCK_HEIGHT + 500
                block = Block(screen, x_pos, y_pos)
                block_group.add(block)
                all_sprites.add(block)

clock = pygame.time.Clock()
enemy_direction = 1

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

    # hit detection
    enemy_kills = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)
    if enemy_kills:
        enemy_kill.play()
        score += 10
        for hit in enemy_kills:
            explosion = Explosion(hit.rect.center)
            explosion_group.add(explosion)
            all_sprites.add(explosion)


    # game logic

    enemies = enemy_group.sprites()
    for enemy in enemies:
        if enemy.rect.right >= DISPLAY_WIDTH:
            enemy_direction = -1

            if enemies:
                for alien in enemies:
                    alien.rect.y += 2

        elif enemy.rect.x <= 0:
            enemy_direction = 1

            if enemies:
                for alien in enemies:
                    alien.rect.y += 2

    screen.fill(BLACK)

    # sprite groups
    missile_group.draw(screen)
    player_group.draw(screen)
    enemy_group.draw(screen)
    block_group.draw(screen)
    explosion_group.draw(screen)

    enemy_group.update(enemy_direction)
    all_sprites.update()

    # text
    score_object = SM_FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_object, score_rect)

    pygame.display.flip()

    clock.tick(FPS)

# quit
pygame.quit()
