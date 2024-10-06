import os.path
import pygame
from pygame.color import Color
from pygame.constants import KEYDOWN
from pygame.surface import Surface

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISP = (WIN_WIDTH, WIN_HEIGHT)
BACK_COLOR = '#000000'
FPS = 60
FILE_DIR = os.path.dirname(__file__)


class Camera:
    def __init__(self):
        pass

    def apply_camera(self):
        pass

    def update_camera(self):
        pass


def camera_config(camera, target_rect):
    pass

def new_level():
    pass

def main():
    new_level()
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
        timer.tick(FPS)
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



