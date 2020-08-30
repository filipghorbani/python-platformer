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
    player_sprites = pygame.sprite.Group()
    platform_sprites = pygame.sprite.Group()
    gun_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

    # Put all sprite groups in a Dictionary
    groups = {"all": all_sprites, "players": player_sprites,
              "platforms": platform_sprites, "guns": gun_sprites, "bullets": bullet_sprites}

    # Create platforms
    platform = Platform((globals.GRID_WIDTH/2-2)*globals.TILESIZE, globals.SCREEN_HEIGHT -
                        globals.TILESIZE*3, globals.TILESIZE*4, globals.TILESIZE)
    all_sprites.add(platform)
    platform_sprites.add(platform)
    platform = Platform(globals.SCREEN_WIDTH/2, 0, 1,
                        globals.TILESIZE*globals.GRID_HEIGHT)
    all_sprites.add(platform)
    platform_sprites.add(platform)

    # Create player
    player_one = Player(globals.GRID_WIDTH/2 *
                        globals.TILESIZE-globals.TILESIZE, 500, globals.RED)
    player_one.platforms = platform_sprites
    all_sprites.add(player_one)

    player_two = Player(globals.GRID_WIDTH/2 *
                        globals.TILESIZE, 500, globals.BLUE)
    player_two.platforms = platform_sprites
    all_sprites.add(player_two)

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Player One
                if event.key == pygame.K_LEFT:
                    player_one.move(-1)
                    player_one.facing = "left"
                if event.key == pygame.K_RIGHT:
                    player_one.move(1)
                    player_one.facing = "right"
                if event.key == pygame.K_UP:
                    player_one.jump()
                # Player Two
                if event.key == pygame.K_a:
                    player_two.move(-1)
                    player_two.facing = "left"
                if event.key == pygame.K_d:
                    player_two.move(1)
                    player_two.facing = "right"
                if event.key == pygame.K_w:
                    player_two.jump()
            elif event.type == pygame.KEYUP:
                # Player One
                if event.key == pygame.K_LEFT:
                    player_one.move(1)
                if event.key == pygame.K_RIGHT:
                    player_one.move(-1)
                if event.key == pygame.K_RCTRL:
                    player_one.shoot(groups)
                # Player Two
                if event.key == pygame.K_a:
                    player_two.move(1)
                if event.key == pygame.K_d:
                    player_two.move(-1)
                if event.key == pygame.K_LCTRL:
                    player_two.shoot(groups)

        all_sprites.update()
        screen.fill(globals.GREY)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
