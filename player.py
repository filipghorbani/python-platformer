import pygame
import globals


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        # Set height, width
        self.image = pygame.Surface([25, 50])
        self.image.fill(globals.RED)

        # Set position
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed
        self.speed = 6
        self.change_x = 0
        self.change_y = 0

        self.facing = "left"

    def move(self, x):

        self.change_x += x * self.speed

    def jump(self):

        self.rect.y += 2
        hit_platforms = pygame.sprite.spritecollide(
            self, self.platforms, False)
        self.rect.y -= 2
        if self.rect.bottom >= globals.SCREEN_HEIGHT or len(hit_platforms) > 0:
            self.change_y = -13

    def gravity(self):

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        if self.rect.bottom >= globals.SCREEN_HEIGHT and self.change_y >= 0:
            self.change_y = 0
            self.rect.bottom = globals.SCREEN_HEIGHT

    def shoot(self, bullets, sprites):
        bullet = Bullet(self.rect.x if self.facing == "left" else self.rect.right, self.rect.centery,
                        1 if self.facing == "right" else -1)
        bullets.add(bullet)
        sprites.add(bullet)
        bullet.sprites = sprites

    def update(self):

        self.gravity()
        # Move left/right
        self.rect.x += self.change_x

        for platform in pygame.sprite.spritecollide(self, self.platforms, False):
            if self.change_x > 0:
                self.rect.right = platform.rect.left
            else:
                self.rect.left = platform.rect.right
        # Move up/down
        self.rect.y += self.change_y
        for platform in pygame.sprite.spritecollide(self, self.platforms, False):
            if self.change_y > 0:
                self.rect.bottom = platform.rect.top
                self.change_y = 0
            else:
                self.rect.top = platform.rect.bottom
                self.change_y = -self.change_y/2


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):

        super().__init__()

        # Set height, width
        self.image = pygame.Surface([5, 5])
        self.image.fill(globals.BLACK)

        # Set position
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed
        self.speed = 10 * direction

    def update(self):
        self.rect.x += self.speed
        for platform in pygame.sprite.spritecollide(self, self.platforms, False):
