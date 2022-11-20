from pico2d import *
from random import *
import Item
import character
import game_framework
import gameover_state
import game_world
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

WIDTH, HEIGHT = 1024, 1024
class Enemy:
    imageR, imageL = None, None
    def __init__(self):
        if Enemy.imageR == None:
            self.imageR = load_image('sprites/characters/enemy1R.png')
        if Enemy.imageL == None:
            self.imageL = load_image('sprites/characters/enemy1L.png')
        self.speed = 2
        self.hp = 100 * (play_state.play_time//5 + 1)
        self.atk = 1
        self.hit = 1
        self.time = 0
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
        self.running = True
    def update(self, player):
        self.time += game_framework.frame_time

        if self.x < WIDTH / 2:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
        if self.x > WIDTH / 2:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
        if self.y < HEIGHT / 2:
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        if self.y > HEIGHT / 2:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time

        if player.dir == 1:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * player.move
        elif player.dir == 2:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * player.move
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * player.move
        elif player.dir == 3:
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * player.move
        elif player.dir == 4:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * player.move
            self.y -= character.RUN_SPEED_PPS * game_framework.frame_time * player.move
        elif player.dir == -1:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * player.move
        elif player.dir == -2:
            self.x -= character.RUN_SPEED_PPS * game_framework.frame_time * player.move
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * player.move
        elif player.dir == -3:
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * player.move
        elif player.dir == -4:
            self.x += character.RUN_SPEED_PPS * game_framework.frame_time * player.move
            self.y += character.RUN_SPEED_PPS * game_framework.frame_time * player.move



    def draw(self, player):
        if self.x < WIDTH / 2:  # imageR 사용
            if self.y < HEIGHT / 2:
                # 우상
                self.imageR.clip_draw(136, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            elif self.y > HEIGHT / 2:
                # 우하
                self.imageR.clip_draw(471, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            else:
                # 우측
                self.imageR.clip_draw(203, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        elif self.x > WIDTH / 2:  # imageL 사용
            if self.y < HEIGHT / 2:
                # 좌상
                self.imageL.clip_draw(467, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            elif self.y > HEIGHT / 2:
                # 좌하
                self.imageL.clip_draw(199, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            else:
                # 좌측
                self.imageL.clip_draw(333, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        else:
            self.imageR.clip_draw(203, 615 - int(self.frame) * 75, 63, 72, self.x, self.y, self.w, self.h)
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        draw_rectangle(*self.get_bb(player))

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            pass
        if group == 'whip:enemy' or group == 'whip2:enemy':
            print(self.hp)
            if self.time > self.cooltime:
                self.hp -= other.damage * play_state.player.hit
                self.time = 0
            if self.hp <= 0:
                if self.drop <= 80:
                    game_world.add_object(Item.Item(self.x, self.y), 2)
                game_world.remove_object(self)
        if group == 'garlic:enemy':
            print(self.hp)
            if self.time > self.cooltime:
                self.hp -= other.damage * play_state.player.hit
                self.time = 0
            if self.hp <= 0:
                if self.drop <= 80:
                    game_world.add_object(Item.Item(self.x, self.y), 2)
                game_world.remove_object(self)


    def get_bb(self, player):
        return self.x - self.w/2 + 10, self.y - self.h/2 + 10, self.x + self.w/2 - 10, self.y + self.h/2 - 10



