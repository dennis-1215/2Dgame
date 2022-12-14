from pico2d import *
from random import *
import Item
import character
import game_framework
import game_world
import main_state
import play_state

# Myutal Run Speed
PIXEL_PER_METER = (32.0 / 1.0) # 32 pixel = 100 cm
RUN_SPEED_KMPH = 6.5
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Myutal Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

# Bat Run Speed
BAT_PIXEL_PER_METER = (27.0 / 1.0)  # 27 pixel = 100 cm
BAT_RUN_SPEED_KMPH = 6.5
BAT_RUN_SPEED_MPM = (BAT_RUN_SPEED_KMPH * 1000.0 / 60.0)
BAT_RUN_SPEED_MPS = (BAT_RUN_SPEED_MPM / 60.0)
BAT_RUN_SPEED_PPS = (BAT_RUN_SPEED_MPS * BAT_PIXEL_PER_METER)

# Bat Action Speed
BAT_TIME_PER_ACTION = 0.5
BAT_ACTION_PER_TIME = 1.0 / BAT_TIME_PER_ACTION
BAT_FRAMES_PER_ACTION = 5

# Golem Run Speed
GOLEM_PIXEL_PER_METER = (92.0 / 3.0) # 92 pixel = 3m
GOLEM_RUN_SPEED_KMPH = 3.0
GOLEM_RUN_SPEED_MPM = (GOLEM_RUN_SPEED_KMPH * 1000.0 / 60.0)
GOLEM_RUN_SPEED_MPS = (GOLEM_RUN_SPEED_MPM / 60.0)
GOLEM_RUN_SPEED_PPS = (GOLEM_RUN_SPEED_MPS * GOLEM_PIXEL_PER_METER)

# Golem Action Speed
GOLEM_TIME_PER_ACTION = 0.5
GOLEM_ACTION_PER_TIME = 1.0 / GOLEM_TIME_PER_ACTION
GOLEM_FRAMES_PER_ACTION = 5

WIDTH, HEIGHT = 1024, 1024
class Enemy:
    imageR, imageL = None, None
    hit_sound = None
    def __init__(self):
        if Enemy.imageR == None:
            Enemy.imageR = load_image('sprites/characters/enemy1R.png')
        if Enemy.imageL == None:
            Enemy.imageL = load_image('sprites/characters/enemy1L.png')
        if Enemy.hit_sound == None:
            Enemy.hit_sound = load_wav('sounds/enemy_hit.ogg')
            Enemy.hit_sound.set_volume(main_state.account.sfx_volume)
        self.hp = 10 + (play_state.play_time//10 * 2)
        self.atk = 1
        self.hit = 1
        self.time = 0
        self.whip_time = 0
        self.whip2_time = 0
        self.garlic_time = 0
        self.attack_cooltime = 0.01
        self.cooltime = 1.0
        self.drop = randint(1, 100)
        self.w, self.h = 63, 72

        if randint(0, 1) == 1:
            self.x = randint(0, WIDTH)
            if randint(0, 1) == 1:
                self.y = -10
            else:
                self.y = HEIGHT + 10
        else:
            self.y = randint(0, HEIGHT)
            if randint(0, 1) == 1:
                self.x = -10
            else:
                self.x = WIDTH + 10
        self.frame = randint(0, 5)

    def update(self, player):
        self.time += game_framework.frame_time
        self.whip_time += game_framework.frame_time
        self.whip2_time += game_framework.frame_time


        if self.x < WIDTH / 2:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
        if self.x > WIDTH / 2:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
        if self.y < HEIGHT / 2:
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        if self.y > HEIGHT / 2:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time

        if player.dir == 1:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 2:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 3:
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 4:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -1:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -2:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -3:
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -4:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)



    def draw(self, player):
        if self.x < WIDTH / 2:  # imageR ??????
            if self.y < HEIGHT / 2:
                # ??????
                self.imageR.clip_draw(136, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            elif self.y > HEIGHT / 2:
                # ??????
                self.imageR.clip_draw(471, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            else:
                # ??????
                self.imageR.clip_draw(203, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        elif self.x > WIDTH / 2:  # imageL ??????
            if self.y < HEIGHT / 2:
                # ??????
                self.imageL.clip_draw(467, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            elif self.y > HEIGHT / 2:
                # ??????
                self.imageL.clip_draw(199, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            else:
                # ??????
                self.imageL.clip_draw(333, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        else:
            self.imageR.clip_draw(203, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            pass

        if group == 'whip:enemy':
            if self.whip_time > self.cooltime:
                self.hp -= other.damage * play_state.player.hit + main_state.damage_up.plus_damage
                Bat.hit_sound.play()
                self.whip_time = 0
            if self.hp <= 0:
                if self.drop <= 80:
                    item = Item.Item(self.x, self.y)
                    game_world.add_object(item, 2)
                    game_world.add_collision_pairs(None, item, 'player:item')
                elif self.drop <= 85:
                    gold = Item.Gold(self.x, self.y)
                    game_world.add_object(gold, 2)
                    game_world.add_collision_pairs(None, gold, 'player:gold')
                game_world.remove_object(self)
                play_state.player.kill_count += 1


        if group == 'whip2:enemy':
            if self.whip2_time > self.cooltime:
                self.hp -= other.damage * play_state.player.hit + main_state.damage_up.plus_damage
                Bat.hit_sound.play()
                self.whip2_time = 0
            if self.hp <= 0:
                if self.drop <= 80:
                    item = Item.Item(self.x, self.y)
                    game_world.add_object(item, 2)
                    game_world.add_collision_pairs(None, item, 'player:item')
                elif self.drop <= 85:
                    gold = Item.Gold(self.x, self.y)
                    game_world.add_object(gold, 2)
                    game_world.add_collision_pairs(None, gold, 'player:gold')
                game_world.remove_object(self)
                play_state.player.kill_count += 1


        if group == 'garlic:enemy':
            if self.garlic_time > self.cooltime:
                self.hp -= other.damage * play_state.player.hit + main_state.damage_up.plus_damage
                Bat.hit_sound.play()
                self.time = 0
            if self.hp <= 0:
                if self.drop <= 80:
                    item = Item.Item(self.x, self.y)
                    game_world.add_object(item, 2)
                    game_world.add_collision_pairs(None, item, 'player:item')
                elif self.drop <= 85:
                    gold = Item.Gold(self.x, self.y)
                    game_world.add_object(gold, 2)
                    game_world.add_collision_pairs(None, gold, 'player:gold')
                game_world.remove_object(self)
                play_state.player.kill_count += 1



    def get_bb(self):
        return self.x - self.w/2 + 10, self.y - self.h/2 + 10, self.x + self.w/2 - 10, self.y + self.h/2 - 10



class Bat(Enemy): # ?????? ?????? 2m
    image = None
    hit_sound = None
    def __init__(self):
        if Bat.image == None:
            Bat.image = load_image('sprites/characters/enemies.png')
        if Bat.hit_sound == None:
            Bat.hit_sound = load_wav('sounds/enemy_hit.ogg')
            Bat.hit_sound.set_volume(main_state.account.sfx_volume)
        self.hp = 10
        self.atk = 1
        self.hit = 1
        self.time = 0
        self.whip_time = 0
        self.whip2_time = 0
        self.garlic_time = 0
        self.attack_cooltime = 0.01
        self.cooltime = 1.0
        self.drop = randint(1, 100)
        self.w, self.h = 54, 54

        if randint(0, 1) == 1:
            self.x = randint(0, WIDTH)
            if randint(0, 1) == 1:
                self.y = -10
            else:
                self.y = HEIGHT + 10
        else:
            self.y = randint(0, HEIGHT)
            if randint(0, 1) == 1:
                self.x = -10
            else:
                self.x = WIDTH + 10
        self.frame = randint(0, 5)

    def update(self, player):
        self.time += game_framework.frame_time
        self.whip_time += game_framework.frame_time
        self.whip2_time += game_framework.frame_time


        if self.x < WIDTH / 2:
            self.x += BAT_RUN_SPEED_PPS * game_framework.frame_time
        if self.x > WIDTH / 2:
            self.x -= BAT_RUN_SPEED_PPS * game_framework.frame_time
        if self.y < HEIGHT / 2:
            self.y += BAT_RUN_SPEED_PPS * game_framework.frame_time
        if self.y > HEIGHT / 2:
            self.y -= BAT_RUN_SPEED_PPS * game_framework.frame_time

        if player.dir == 1:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 2:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 3:
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 4:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -1:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -2:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -3:
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -4:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)

    def draw(self, player):
        if self.x > WIDTH/2:
            if int(self.frame) == 0:
                self.image.clip_draw(1198, 3, 27, 24, self.x, self.y, self.w, self.h)
            elif int(self.frame) == 1:
                self.image.clip_draw(1400, 3, 24, 27, self.x, self.y, self.w, self.h)
            elif int(self.frame) == 2:
                self.image.clip_draw(1385, 70, 21, 25, self.x, self.y, self.w, self.h)
        else:
            if int(self.frame) == 0:
                self.image.clip_composite_draw(1198, 3, 27, 24, 0, 'h', self.x, self.y, self.w, self.h)
            elif int(self.frame) == 1:
                self.image.clip_composite_draw(1400, 3, 24, 27, 0, 'h', self.x, self.y, self.w, self.h)
            elif int(self.frame) == 2:
                self.image.clip_composite_draw(1385, 70, 21, 25, 0, 'h', self.x, self.y, self.w, self.h)

        self.frame = (self.frame + BAT_FRAMES_PER_ACTION * BAT_ACTION_PER_TIME * game_framework.frame_time) % 3

    def get_bb(self):
        return self.x - self.w/2 + 10, self.y - self.h/2 + 10, self.x + self.w/2 - 10, self.y + self.h/2 - 10

class Golem(Enemy): # ?????? ?????? 2m
    image = None
    hit_sound = None
    def __init__(self):
        if Golem.image == None:
            Golem.image = load_image('sprites/characters/enemies.png')
        if Golem.hit_sound == None:
            Golem.hit_sound = load_wav('sounds/enemy_hit.ogg')
            Golem.hit_sound.set_volume(main_state.account.sfx_volume)
        self.hp = 200
        self.atk = 1
        self.hit = 1
        self.time = 0
        self.whip_time = 0
        self.whip2_time = 0
        self.garlic_time = 0
        self.attack_cooltime = 0.01
        self.cooltime = 1.0
        self.drop = randint(1, 90)
        self.w, self.h = 46, 46

        if randint(0, 1) == 1:
            self.x = randint(0, WIDTH)
            if randint(0, 1) == 1:
                self.y = -10
            else:
                self.y = HEIGHT + 10
        else:
            self.y = randint(0, HEIGHT)
            if randint(0, 1) == 1:
                self.x = -10
            else:
                self.x = WIDTH + 10
        self.frame = randint(0, 5)

    def update(self, player):
        self.time += game_framework.frame_time
        self.whip_time += game_framework.frame_time
        self.whip2_time += game_framework.frame_time


        if self.x < WIDTH / 2:
            self.x += GOLEM_RUN_SPEED_PPS * game_framework.frame_time
        if self.x > WIDTH / 2:
            self.x -= GOLEM_RUN_SPEED_PPS * game_framework.frame_time
        if self.y < HEIGHT / 2:
            self.y += GOLEM_RUN_SPEED_PPS * game_framework.frame_time
        if self.y > HEIGHT / 2:
            self.y -= GOLEM_RUN_SPEED_PPS * game_framework.frame_time

        if player.dir == 1:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 2:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 3:
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == 4:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -1:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -2:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -3:
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
        elif player.dir == -4:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * (player.move * main_state.speed.multiply_speed)

    def draw(self, player):
        if self.x > WIDTH/2:
            if int(self.frame) == 0:
                self.image.clip_draw(1751, 1150 - 345, self.w, self.h, self.x, self.y, self.w * 2, self.h * 2)
            elif int(self.frame) == 1:
                self.image.clip_draw(1982, 1150 - 280, self.w, self.h, self.x, self.y, self.w * 2, self.h * 2)
        else:
            if int(self.frame) == 0:
                self.image.clip_composite_draw(1751, 1150 - 345, self.w, self.h, 0, 'h', self.x, self.y, self.w * 2, self.h * 2)
            elif int(self.frame) == 1:
                self.image.clip_composite_draw(1982, 1150 - 280, self.w, self.h, 0, 'h', self.x, self.y, self.w * 2, self.h * 2)

        self.frame = (self.frame + GOLEM_FRAMES_PER_ACTION * GOLEM_ACTION_PER_TIME * game_framework.frame_time) % 2


    def get_bb(self):
        return self.x - self.w, self.y - self.h, self.x + self.w, self.y + self.h
