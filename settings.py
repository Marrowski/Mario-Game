#mario.py
import os
WIN_WIDTH = 800
WIN_HEIGHT = 640
DISP = (WIN_WIDTH, WIN_HEIGHT)
BACK_COLOR = '#000000'
FPS = 60
SCREEN_START = (0, 0)
FILE_DIR = os.path.dirname(__file__)

#monsters.py
MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = '#2111FF'
ICON_DIR = os.path.dirname(__file__)

#blocks.py
PLATFORM_WIDTH, PLATFROM_HEIGHT, PLATFROM_COLOR = 32, 32, '#000000'
ICON_DIR = os.path.dirname(__file__)

#player.py
MOVE_SPEED = 7
MOVE_EXTRA_SPEED = 2.5
WIDTH, HEIGHT, COLOR = 22, 32, '#888888'
JUMP_POWER, JUMP_EXTRA_POWER, GRAVITY = 10, 1, 0.25
ANIMATION_DELAY, ANIMATION_SUPER_SPEED_DELAY = 0.1, 0.05

ICON_DIR = os.path.dirname(__file__)
ANIMATION_RIGHT = [ICON_DIR]
ANIMATION_LEFT = [ICON_DIR]
ANIMATION_JUMP = [ICON_DIR]
ANIMATION_JUMP_LEFT = [ICON_DIR]
ANIMATION_JUMP_RIGHT = [ICON_DIR]
ANIMATION_STAY = [ICON_DIR]

#pyganim.py
PLAYING, PAUSED, STOPED = 'playing', 'paused', 'stoped'

NORTH, SOUTH, WEST, EAST = 'north', 'south', 'west', 'east'
NORTH_WEST, SOUTH_WEST, NORTH_EAST, EAST_EAST = 'northwest', 'southwest', 'westeast', 'easteast'