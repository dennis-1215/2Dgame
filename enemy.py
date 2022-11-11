from pico2d import *
from random import *
import Item
import character
import game_framework
import gameover_state
import game_world

# Myutal Run Speed
PIXEL_PER_METER = (32.0 / 1.0) # 32 pixel = 100 cm
RUN_SPEED_KMPH = 13.0
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
        self.hp = 10
        self.atk = 1
        self.drop = randint(1, 100)

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
        self.frame = randint(0,5)
        self.running = True
    def update(enemy, player):
        if enemy.x < WIDTH / 2:
            enemy.x += RUN_SPEED_PPS * game_framework.frame_time
        if enemy.x > WIDTH / 2:
            enemy.x -= RUN_SPEED_PPS * game_framework.frame_time
        if enemy.y < HEIGHT / 2:
            enemy.y += RUN_SPEED_PPS * game_framework.frame_time
        if enemy.y > HEIGHT / 2:
            enemy.y -= RUN_SPEED_PPS * game_framework.frame_time

        if player.dir == 1:
            enemy.x -= character.RUN_SPEED_PPS * game_framework.frame_time
        elif player.dir == 2:
            enemy.x += character.RUN_SPEED_PPS * game_framework.frame_time
            enemy.y -= character.RUN_SPEED_PPS * game_framework.frame_time
        elif player.dir == 3:
            enemy.y -= character.RUN_SPEED_PPS * game_framework.frame_time
        elif player.dir == 4:
            enemy.x -= character.RUN_SPEED_PPS * game_framework.frame_time
            enemy.y -= character.RUN_SPEED_PPS * game_framework.frame_time
        elif player.dir == -1:
            enemy.x += character.RUN_SPEED_PPS * game_framework.frame_time
        elif player.dir == -2:
            enemy.x -= character.RUN_SPEED_PPS * game_framework.frame_time
            enemy.y += character.RUN_SPEED_PPS * game_framework.frame_time
        elif player.dir == -3:
            enemy.y += character.RUN_SPEED_PPS * game_framework.frame_time
        elif player.dir == -4:
            enemy.x += character.RUN_SPEED_PPS * game_framework.frame_time
            enemy.y += character.RUN_SPEED_PPS * game_framework.frame_time

        if abs(enemy.x - WIDTH/2) < 35 and abs(enemy.y - HEIGHT/2) < 40:
            player.hp -= enemy.atk
            if player.hp <= 0:
                game_framework.push_state(gameover_state)

        if enemy.hp < 1:
            if enemy.drop <= 80:
                game_world.add_object(Item.Item(enemy.x, enemy.y), 1)
            game_world.remove_object(enemy)

    def draw(self, player):
        if self.x < WIDTH / 2:  # imageR 사용
            if self.y < HEIGHT / 2:
                # 우상
                self.imageR.clip_draw(136, 615 - int(self.frame) * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            elif self.y > HEIGHT / 2:
                # 우하
                self.imageR.clip_draw(471, 615 - int(self.frame) * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            else:
                # 우측
                self.imageR.clip_draw(203, 615 - int(self.frame) * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        elif self.x > WIDTH / 2:  # imageL 사용
            if self.y < HEIGHT / 2:
                # 좌상
                self.imageL.clip_draw(467, 615 - int(self.frame) * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            elif self.y > HEIGHT / 2:
                # 좌하
                self.imageL.clip_draw(199, 615 - int(self.frame) * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

            else:
                # 좌측
                self.imageL.clip_draw(333, 615 - int(self.frame) * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        else:
            self.imageR.clip_draw(203, 615 - int(self.frame) * 75, 63, 72, self.x, self.y)
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2




