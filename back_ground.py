from pico2d import *

class BG:
    def __init__(self):
        self.image = load_image('sprites/maps/bg_molise.png')
        self.x, self.y = 0, 0

    def update(self, player):
        pass

    def handle_event(self):
        pass
    def draw(self, player):
        self.image.draw(self.x - player.x, self.y - player.y)
