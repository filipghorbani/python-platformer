import pygame
import globals


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, color):

        super().__init__()

        # Set height, width
        self.image = pygame.Surface([globals.TILESIZE, globals.TILESIZE*2])
        self.image.fill(color)

        # Set position
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed
        self.speed = 6
        self.change_x = 0
        self.change_y = 0

        self.facing = "left"
        self.gun = Gun(10, 10, 15, 15)
        self.hp = 10

    def move(self, x):

        self.change_x += x * self.speed

    def jump(self):

        # Check if standing on a platform
        self.rect.y += 2
        hit_platforms = pygame.sprite.spritecollide(
            self, self.platforms, False)
        self.rect.y -= 2

        # Check if standing on the ground
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

    def shoot(self, groups):

        # Shoot only if player has a gun
        if self.gun != None:
            self.gun.shoot(self, groups)

    def update(self):

        # Apply gravity on player
        self.gravity()

        # Move left/right
        self.rect.x += self.change_x

        # Check if colliding with platform
        for platform in pygame.sprite.spritecollide(self, self.platforms, False):
            if self.change_x > 0:
                self.rect.right = platform.rect.left
            else:
                self.rect.left = platform.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check if colliding with platform
        for platform in pygame.sprite.spritecollide(self, self.platforms, False):
            if self.change_y > 0:
                self.rect.bottom = platform.rect.top
                self.change_y = 0
            else:
                self.rect.top = platform.rect.bottom
                self.change_y = -self.change_y/2


class Gun(pygame.sprite.Sprite):

    def __init__(self, bullet_speed, bullet_capacity, bullet_width, bullet_height):

        super().__init__()

        self.bullet_speed = bullet_speed
        self.bullet_capacity = bullet_capacity
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height

    def shoot(self, player, groups):

        # Create bullet and add it to sprite groups
        bullet = Bullet(player.rect.x if player.facing == "left" else player.rect.right, player.rect.centery, self.bullet_width, self.bullet_height,
                        1 if player.facing == "right" else -1, self.bullet_speed)
        groups["all"].add(bullet)
        groups["bullets"].add(bullet)
        bullet.groups = groups
        self.bullet_capacity -= 1

        # Remove gun if no bullets left in the gun
        if self.bullet_capacity < 1:
            player.gun = None
            self.kill()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, direction, speed):

        super().__init__()

        # Set height, width
        self.image = pygame.Surface([width, height])
        self.image.fill(globals.BLACK)

        # Set position
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed
        self.speed = speed * direction
        self.moved = 0

    def update(self):

        # Move bullet
        self.rect.x += self.speed
        self.moved += abs(self.speed)

        # Remove bullet if moved too far
        if self.moved > 2000:
            self.kill()

        # Wraps bullet on the map
        '''
        if self.rect.right < 0:
            self.rect.left = globals.SCREEN_WIDTH
        elif self.rect.left > globals.SCREEN_WIDTH:
            self.rect.right = 0
        '''

        # Check if bullet hit a platform
        for platform in pygame.sprite.spritecollide(self, self.groups["platforms"], False):
            self.kill()
            platform.kill()
