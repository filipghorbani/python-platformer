import pygame
from player import Player

# Globals
BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():

    pygame.init()
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('Test')

    all_sprites = pygame.sprite.Group()
    player = Player(50, 50)
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
