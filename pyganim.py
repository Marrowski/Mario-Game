import pygame
import time
from settings import PLAYING, PAUSED, STOPED, NORTH, SOUTH, WEST, EAST, NORTH_WEST, SOUTH_WEST, NORTH_EAST, EAST_EAST


class PygAnimation:
    def __init__(self, frames, loop=True):
        pass

    def _get_start_times(self):
        pass

    def reverse(self):
        pass

    def get_copy(self):
        pass

    def get_copies(self, num_copies=1):
        pass

    def blit(self, dest_surface, dest):
        pass

    def get_frame(self, frame_num):
        pass

    def clearTransforms(self):
        pass

    def make_trasforms_permanent(self):
        pass

    def blit_frame_num(self):
        pass

    def play(self):
        pass

    def isFinished(self):
        pass