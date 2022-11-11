from pico2d import *

WIDTH, HEIGHT = 1024, 1024
class BG:
    def __init__(self):
        self.image = load_image('sprites/maps/bg_molise.png')
        self.x, self.y = 0, 0

    def update(self, player):
        pass

    def handle_event(self):
        pass
    def draw(self, player):
        self.image.clip_draw(0, 0, WIDTH, HEIGHT, self.x - player.x, self.y - player.y, WIDTH*2 , HEIGHT*2)
