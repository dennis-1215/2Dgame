from pico2d import *

class BG:
    def __init__(self):
        self.image = load_image('sprites/maps/bg_molise.png')
        self.x, self.y = 0, 0

    def draw(self, x, y):
        self.image.draw(self.x - x, self.y - y)
