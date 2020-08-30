import pygame
import globals


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(globals.BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
