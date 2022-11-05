from pico2d import *
import game_framework
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
    if player.dir == 1:
        item.x -= player.speed
    elif player.dir == 2:
        item.x += player.speed
        item.y -= player.speed
    elif player.dir == 3:
        item.y -= player.speed
    elif player.dir == 4:
        item.x -= player.speed
        item.y -= player.speed
    elif player.dir == -1:
        item.x += player.speed
    elif player.dir == -2:
        item.x -= player.speed
        item.y += player.speed
    elif player.dir == -3:
        item.y += player.speed
    elif player.dir == -4:
        item.x += player.speed
        item.y += player.speed

def get_item(player, item, items):
    if abs(item.x - WIDTH/2) < 16 and abs(item.y - HEIGHT/2) < 25:
        player.exp += item.exp
        items.remove(item)
        if player.exp >= player.max_exp:
            player.level += 1
            player.exp -= player.max_exp
            player.max_exp *= 1.2
            player.dir = 0
            player.cur_state = character.IDLE
            game_framework.push_state(level_up_state)
