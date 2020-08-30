import pygame
import sys
import globals
from player import Player
from platform import Platform

# Center the window on display
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():

    # Init display
    pygame.init()
    screen = pygame.display.set_mode(
        (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
    pygame.display.set_caption('Platformer')

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    platform_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Create platforms
    platform = Platform(450, 700, 500, 20)
    all_sprites.add(platform)
    platform_sprites.add(platform)
    platform = Platform(250, 500, 250, 20)
    all_sprites.add(platform)
    platform_sprites.add(platform)
    platform = Platform(900, 500, 250, 20)
    all_sprites.add(platform)
    platform_sprites.add(platform)
    platform = Platform(450, 300, 500, 20)
    all_sprites.add(platform)
    platform_sprites.add(platform)

    # Create player
    player = Player(globals.SCREEN_WIDTH/2, 500)
    player.platforms = platform_sprites
    all_sprites.add(player)

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move(-1)
                    player.facing = "left"
                if event.key == pygame.K_RIGHT:
                    player.move(1)
                    player.facing = "right"
                if event.key == pygame.K_UP:
                    player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.move(1)
                if event.key == pygame.K_RIGHT:
                    player.move(-1)
                if event.key == pygame.K_SPACE:
                    player.shoot(bullets, all_sprites)

        all_sprites.update()
        screen.fill(globals.GREY)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
