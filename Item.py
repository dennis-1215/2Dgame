from pico2d import *
import character

class Item:
    def __init__(self, x, y):
        self.imageItem = load_image('sprites/characters/items.png')
        self.level = 1
        self.exp = 100
        self.x = x
        self.y = y

    def draw(self):
        if self.level == 1:
            self.imageItem.clip_draw(166, 8, 10, 12, self.x, self.y)


def item_distance(player, item):
    if player.R_L_check == 1:
        item.x -= player.speed
    if player.R_L_check == 2:
        item.x += player.speed
    if player.U_check == 1:
        item.y -= player.speed
    if player.D_check == 1:
        item.y += player.speed