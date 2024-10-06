import os.path
from sys import platform

from pygame.rect import Rect

from settings import WIN_WIDTH, WIN_HEIGHT, DISP, BACK_COLOR, FPS, SCREEN_START, ICON_DIR

import pygame
from pygame.color import Color
from pygame.constants import KEYDOWN, QUIT
from pygame.constants import KEYUP
from pygame.surface import Surface




class Camera:
    def __init__(self, camera_fn, width, height):
        self.camera_fn = camera_fn
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self):
        self.state = self.camera_fn(self.state, target.rect)


def camera_config(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = min(0, t)
    t = max(-(camera.width - WIN_HEIGHT), t)
    return Rect(l, t, w, h)

def load_level():
    pass

def main():
    load_level()
    pygame.init()
    screen = pygame.display.set_mode(DISP)
    pygame.display.set_caption('Super Mario Game / Yemelianov Oleh')
    bg = Surface(DISP)
    bg.fill(Color(BACK_COLOR))

    left = right = up = running = False

    hero = Player(player_x, player_y)

    timer = pygame.time.Clock()

    x = y = 0

    while not hero.winner:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit('QUIT')
            # if event.type == KEYDOWN and event.key == pygame.K_UP:
            #     up = True
            # if event.type == KEYDOWN and event.key == pygame.K_LEFT:
            #     left = True
            # if event.type == KEYDOWN and event.key == pygame.K_RIGHT:
            #     right = True
            # if event.type == KEYDOWN and event.key == pygame.K_LSHIFT:
            #     running = True

            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_LSHIFT:
                    running = True

            if event.type == KEYUP:
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_LSHIFT:
                    running = False

        screen.blit(bg, SCREEN_START)

        monsters.update(platform)
        camera.update()
        hero.update(left, right, up, running, platform)
        for event in entities:
            screen.blit(event.image, camera.apply())

        timer.tick(FPS)
        pygame.display.update()

level = []
platform = []
entities = pygame.sprite.Group()
animated_entities = pygame.sprite.Group()
monsters = pygame.sprite.Group()

if __name__ == '__main__':
    main()