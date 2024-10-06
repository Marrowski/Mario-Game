from pygame import *
import os
import blocks
import monsters
import time
from settings import (MOVE_SPEED, MOVE_EXTRA_SPEED, WIDTH, HEIGHT, COLOR, JUMP_POWER, JUMP_EXTRA_POWER, GRAVITY, ANIMATION_DELAY,
        ANIMATION_SUPER_SPEED_DELAY, ICON_DIR, ANIMATION_LEFT, ANIMATION_RIGHT, ANIMATION_JUMP, ANIMATION_JUMP_LEFT, ANIMATION_JUMP_RIGHT,
                      ANIMATION_STAY)


class Player(sprite.Sprite):
    def __init__(self):
        super.__init__(self)
        pass

    def update(self, left, right, up, running, platforms):
        if up:
            pass
        if left:
            pass
        if right:
            pass

    def collide(self, x_val, y_val, platforms):
        pass

    def teleporting(self, go_x, go_y):
        self.rect.x = go_x
        self.rect.y = go_y



    def die(self):
        time.wait(500)
        self.teleporting(self.start_x, self.start_y)
