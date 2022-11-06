from pico2d import *
from random import *
import Item
import character
import game_framework
import gameover_state
import game_world

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
        self.atk = 10
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
            enemy.x += enemy.speed
        if enemy.x > WIDTH / 2:
            enemy.x -= enemy.speed
        if enemy.y < HEIGHT / 2:
            enemy.y += enemy.speed
        if enemy.y > HEIGHT / 2:
            enemy.y -= enemy.speed

        if player.dir == 1:
            enemy.x -= player.speed
        elif player.dir == 2:
            enemy.x += player.speed
            enemy.y -= player.speed
        elif player.dir == 3:
            enemy.y -= player.speed
        elif player.dir == 4:
            enemy.x -= player.speed
            enemy.y -= player.speed
        elif player.dir == -1:
            enemy.x += player.speed
        elif player.dir == -2:
            enemy.x -= player.speed
            enemy.y += player.speed
        elif player.dir == -3:
            enemy.y += player.speed
        elif player.dir == -4:
            enemy.x += player.speed
            enemy.y += player.speed

        if enemy.hp < 1:
            if enemy.drop <= 80:
                game_world.add_object(Item.Item(enemy.x, enemy.y), 1)
            print('kill : ', enemy)
            game_world.remove_object(enemy)

    def draw(enemy, player):
        if enemy.x < WIDTH / 2:  # imageR 사용
            if enemy.y < HEIGHT / 2:
                # 우상
                enemy.imageR.clip_draw(136, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
            elif enemy.y > HEIGHT / 2:
                # 우하
                enemy.imageR.clip_draw(471, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
            else:
                # 우측
                enemy.imageR.clip_draw(203, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
        elif enemy.x > WIDTH / 2:  # imageL 사용
            if enemy.y < HEIGHT / 2:
                # 좌상
                enemy.imageL.clip_draw(467, 615 - enemy.frame // 10 * 75, 63, 72, enemy.x, enemy.y)
                enemy.frame = (enemy.frame + 1) % 50
            elif enemy.y > HEIGHT / 2:
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

        if abs(enemy.x - WIDTH/2) < 35 and abs(enemy.y - HEIGHT/2) < 40:
            player.hp -= enemy.atk
            if player.hp <= 0:
                game_framework.push_state(gameover_state)

