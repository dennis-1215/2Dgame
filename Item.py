from pico2d import *
import game_framework
import character
import game_world
import level_up_state
import main_state
import random

WIDTH, HEIGHT = 1024, 1024

PIXEL_PER_METER = (20.0 / 0.2) # 20 pixel = 20 cm
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
class Item:
    imageItem = None
    get_exp_sound = None
    def __init__(self, x, y):
        if Item.imageItem == None:
            Item.imageItem = load_image('sprites/characters/items.png')
        if Item.get_exp_sound == None:
            Item.get_exp_sound = load_wav('sounds/get_exp.ogg')
            Item.get_exp_sound.set_volume(main_state.account.sfx_volume)

        self.level = 1
        self.exp = 100
        self.exp = 100
        self.range = 30
        self.x = x
        self.y = y
        self.animation_on = 0

    def draw(self, player):
        if self.level == 1:
            self.imageItem.clip_draw(166, 8, 10, 12, self.x, self.y, 20, 24)

    def animation(self, player):
        if self.x > WIDTH/2:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.x += RUN_SPEED_PPS * game_framework.frame_time

        if self.y > HEIGHT/2:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.y += RUN_SPEED_PPS * game_framework.frame_time

        if abs(self.x - WIDTH/2) < 2 and abs(self.y - HEIGHT/2) < 2:
            player.exp += self.exp * main_state.bonus_exp.multiply_bonus_exp
            game_world.remove_object(self)
            while player.exp >= player.max_exp:
                player.level += 1
                player.exp -= player.max_exp
                player.max_exp *= 1.2
                game_framework.push_state(level_up_state)

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
        if item.animation_on == 1:
            item.animation(player)

    def handle_collision(self, other, group):
        if group == 'player:item':
            if self.animation_on == 0:
                Item.get_exp_sound.play()
                self.animation_on = 1
                self.y += 40


    def get_bb(self):
        return self.x - self.range, self.y - self.range, self.x + self.range, self.y + self.range

class Gold(Item):
    image = None
    get_coin_sound = None
    def __init__(self, x, y):
        if Gold.image == None:
            Gold.image = load_image('sprites/characters/items.png')
        if Gold.get_coin_sound == None:
            Gold.get_coin_sound = load_wav('sounds/get_coin.ogg')
            Gold.get_coin_sound.set_volume(main_state.account.sfx_volume)

        self.level = 1
        self.gold = random.randint(1, 20)
        self.range = 30
        self.x = x
        self.y = y
        self.animation_on = 0

    def draw(self, player):
        if self.level == 1:
            self.image.clip_draw(420, 392 - 135, 10, 12, self.x, self.y, 20, 24)

    def animation(self, player):
        if self.x > WIDTH/2:
            self.x -= 1
        else:
            self.x += 1

        if self.y > HEIGHT/2:
            self.y -= 1
        else:
            self.y += 1

        if abs(self.x - WIDTH/2) < 2 and abs(self.y - HEIGHT/2) < 2:
            player.gold += self.gold * main_state.bonus_gold.multiply_bonus_gold
            game_world.remove_object(self)

    def handle_collision(self, other, group):
        if group == 'player:gold':
            if self.animation_on == 0:
                Gold.get_coin_sound.play()
                self.animation_on = 1
                self.y += 40


    def get_bb(self):
        return self.x - self.range, self.y - self.range, self.x + self.range, self.y + self.range