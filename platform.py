import pygame
from globals import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()

        self.rect = pygame.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y

    def hit(self, bullet):
        bullet.kill()

    def draw(self):
        pass
