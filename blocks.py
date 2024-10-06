from pygame import *
import os
from settings import PLATFORM_WIDTH, PLATFROM_COLOR, PLATFROM_HEIGHT, ICON_DIR


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        super().__init(self)
        pass

class BlockDie(Platform):
    def __init__(self, x, y):
        pass

class BlockTeleport(Platform):
    def __init__(self, x, y):
        pass

    def update(self):
        pass

class Princess(Platform):
    def __init__(self, x, y):
        pass

    def update(self):
        pass



