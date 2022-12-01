from pico2d import *
import game_framework
import character
import game_world
import level_up_state
import main_state

WIDTH, HEIGHT = 1024, 1024

class Item:
    imageItem = None
    def __init__(self, x, y):
        if Item.imageItem == None:
            self.imageItem = load_image('sprites/characters/items.png')
        self.level = 1
        self.exp = 100
        self.x = x
        self.y = y

    def draw(self, player):
        if self.level == 1:
            self.imageItem.clip_draw(166, 8, 10, 12, self.x, self.y, 20, 24)


    def update(item, player):
        if player.dir == 1:
            item.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 2:
            item.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            item.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 3:
            item.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 4:
            item.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            item.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -1:
            item.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -2:
            item.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            item.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -3:
            item.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -4:
            item.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            item.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)

        if abs(item.x - WIDTH/2) < 16 and abs(item.y - HEIGHT/2) < 25:
            player.exp += item.exp * main_state.bonus_exp.multiply_bonus_exp
            game_world.remove_object(item)
            while player.exp >= player.max_exp:
                player.level += 1
                player.exp -= player.max_exp
                player.max_exp *= 1.2
                game_framework.push_state(level_up_state)
