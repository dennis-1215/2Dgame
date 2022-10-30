from pico2d import *
import character
import level_up_state
import play_state
WIDTH, HEIGHT = 1024, 1024
class Item:
    def __init__(self, x, y):
        self.imageItem = load_image('sprites/characters/items.png')
        self.level = 1
        self.exp = 100
        self.x = x
        self.y = y

    def draw(self):
        if self.level == 1:
            self.imageItem.clip_draw(166, 8, 10, 12, self.x, self.y, 20, 24)


def item_distance(player, item):
    if player.R_L_check == 1:
        item.x -= player.speed
    if player.R_L_check == 2:
        item.x += player.speed
    if player.U_check == 1:
        item.y -= player.speed
    if player.D_check == 1:
        item.y += player.speed

def get_item(player, item, items):
    if abs(item.x - WIDTH/2) < 16 and abs(item.y - HEIGHT/2) < 25:
        player.exp += item.exp
        items.remove(item)
        if player.exp >= player.max_exp:
            player.level += 1
            player.exp -= player.max_exp
            print(player.level)
            player.max_exp *= 1.2
