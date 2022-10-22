from pico2d import *
from random import *
import character

WIDTH, HEIGHT = 1024, 1024
class Enemy:
    def __init__(self):
        self.imageR = load_image('sprites/characters/enemy1R.png')
        self.imageL = load_image('sprites/characters/enemy1L.png')
        self.speed = randint(1, 3)
        self.on = 0
        self.hp = 10
        self.atk = 10

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

def enemy_move(enemy):
    if enemy.on == 1:
        if enemy.x < WIDTH/2:
            enemy.x += enemy.speed
        if enemy.x > WIDTH/2:
            enemy.x -= enemy.speed
        if enemy.y < HEIGHT/2:
            enemy.y += enemy.speed
        if enemy.y > HEIGHT/2:
            enemy.y -= enemy.speed

def enemy_crash(enemy, character):
    if abs(enemy.x - WIDTH/2) < 35 and abs(enemy.y - HEIGHT/2) < 40:
        character.hp -= enemy.atk
        enemy.hp -= character.atk
        if enemy.hp < 1:
            enemy.on = 0

def enemy_animation(enemy):
    if enemy.on == 1:
        if enemy.x < WIDTH/2: # imageR 사용
            if enemy.y < HEIGHT/2:
                # 우상
                enemy.imageR.clip_draw(136, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
            elif enemy.y > HEIGHT/2:
                # 우하
                enemy.imageR.clip_draw(471, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
            else:
                # 우측
                enemy.imageR.clip_draw(203, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
        elif enemy.x > WIDTH/2: # imageL 사용
            if enemy.y < HEIGHT/2:
                # 좌상
                enemy.imageL.clip_draw(467, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
            elif enemy.y > HEIGHT/2:
                # 좌하
                enemy.imageL.clip_draw(199, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
            else:
                # 좌측
                enemy.imageL.clip_draw(333, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
        else:
            enemy.imageR.clip_draw(203, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
            enemy.frame = (enemy.frame + 1) % 50


def enemy_distance(player, enemy):
        if player.R_L_check == 1:
            enemy.x -= player.speed
        if player.R_L_check == 2:
            enemy.x += player.speed
        if player.U_check == 1:
            enemy.y -= player.speed
        if player.D_check == 1:
            enemy.y += player.speed