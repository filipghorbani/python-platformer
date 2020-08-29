import pygame
import globals


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([25, 50])
        self.image.fill(globals.WHITE)

        # Set position
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed
        self.speed = 5
        self.change_x = 0
        self.change_y = 0

    def move(self, x):
        self.change_x += x * self.speed

    def jump(self):
        if self.rect.bottom >= globals.SCREEN_HEIGHT:
            self.change_y = -10

    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        if self.rect.bottom >= globals.SCREEN_HEIGHT and self.change_y >= 0:
            self.change_y = 0
            self.rect.bottom = globals.SCREEN_HEIGHT

    def update(self):
        self.gravity()
        # Move left/right
        self.rect.x += self.change_x
        # Move up/down
        self.rect.y += self.change_y
