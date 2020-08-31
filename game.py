import pygame
import sys
import os
from globals import *
from player import Player
from platform import Platform
from map import Map


class Game:
    def __init__(self):

        # Center the window on display
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        map_folder = os.path.join(game_folder, 'maps')
        self.map = Map(os.path.join(map_folder, 'map1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new(self):

        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        # Create platforms
        '''platform = Platform((GRID_WIDTH/2-2)*TILESIZE, SCREEN_HEIGHT -
                            TILESIZE*3, TILESIZE*4, TILESIZE)
        self.all_sprites.add(platform)
        self.platforms.add(platform)
        platform = Platform(SCREEN_WIDTH/2, 0, 1,
                            TILESIZE*GRID_HEIGHT)
        self.all_sprites.add(platform)
        self.platforms.add(platform)'''

        for obstacle in self.map.tmxdata.objects:
            if obstacle.name == 'obstacle':
                platform = Platform(obstacle.x, obstacle.y,
                                    obstacle.width, obstacle.height)
                self.platforms.add(platform)

        # Create player
        self.player_one = Player(GRID_WIDTH/2 *
                                 TILESIZE-TILESIZE, 500, RED)
        self.player_one.platforms = self.platforms
        self.all_sprites.add(self.player_one)

        self.player_two = Player(GRID_WIDTH/2 *
                                 TILESIZE, 500, BLUE)
        self.player_two.platforms = self.platforms
        self.all_sprites.add(self.player_two)

    def run(self):
        self.done = False

        while not self.done:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                # Player One
                if self.player_one.alive:
                    if event.key == pygame.K_LEFT:
                        self.player_one.move(-1)
                        self.player_one.facing = "left"
                    if event.key == pygame.K_RIGHT:
                        self.player_one.move(1)
                        self.player_one.facing = "right"
                    if event.key == pygame.K_UP:
                        self.player_one.jump()
                # Player Two
                if self.player_two.alive:
                    if event.key == pygame.K_a:
                        self.player_two.move(-1)
                        self.player_two.facing = "left"
                    if event.key == pygame.K_d:
                        self.player_two.move(1)
                        self.player_two.facing = "right"
                    if event.key == pygame.K_w:
                        self.player_two.jump()
            elif event.type == pygame.KEYUP:
                # Player One
                if self.player_one.alive:
                    if event.key == pygame.K_LEFT:
                        self.player_one.move(1)
                    if event.key == pygame.K_RIGHT:
                        self.player_one.move(-1)
                    if event.key == pygame.K_RCTRL:
                        self.player_one.shoot(self.all_sprites, self.platforms)
                # Player Two
                if self.player_two.alive:
                    if event.key == pygame.K_a:
                        self.player_two.move(1)
                    if event.key == pygame.K_d:
                        self.player_two.move(-1)
                    if event.key == pygame.K_LCTRL:
                        self.player_two.shoot(self.all_sprites, self.platforms)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.blit(self.map_img, (0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


g = Game()
g.new()
g.run()
