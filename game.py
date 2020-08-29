import pygame
import sys
import globals
from player import Player

# Center the window on display
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():

    pygame.init()
    screen = pygame.display.set_mode(
        (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
    pygame.display.set_caption('Test')

    all_sprites = pygame.sprite.Group()
    player = Player(globals.SCREEN_WIDTH/2, 100)
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
                if event.key == pygame.K_RIGHT:
                    player.move(1)
                if event.key == pygame.K_UP:
                    player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.move(1)
                if event.key == pygame.K_RIGHT:
                    player.move(-1)

        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
