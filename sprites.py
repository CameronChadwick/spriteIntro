import pygame
import random
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = DISPLAY_WIDTH//2, DISPLAY_HEIGHT - self.rect.height

        self.change_x = 0       # velocity variable

    def update(self):
        self.rect.x += self.change_x

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.change_x = 4
        elif keys[pygame.K_a]:
            self.change_x = -4
        else:
            self.change_x = 0

        if self.rect.right >= DISPLAY_WIDTH:
            self.rect.right = DISPLAY_WIDTH - 1
        if self.rect.left <= 0:
            self.rect.x = 1


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x_velo):
        self.rect.x += x_velo


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.y_velo = 4

        self.image = pygame.Surface((MISSILE_WIDTH, MISSILE_HEIGHT))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y, MISSILE_WIDTH, MISSILE_HEIGHT])

    def update(self):
        self.rect.y -= self.y_velo


class Block(pygame.sprite.Sprite):
    def __init__(self, display, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image.fill(BLOCK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        pygame.draw.rect(display, BLOCK_COLOR, [self.rect.x, self.rect.y, self.rect.width, self.rect.height])


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = EXPLOSION_LIST[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_rate = 50
        self.kill_center = center
        self.prev_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.prev_update > self.frame_rate:
            self.prev_update = now
            self.frame += 1
        if self.frame == len(EXPLOSION_LIST):
            self.kill()
        else:
            self.image = EXPLOSION_LIST[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.kill_center
