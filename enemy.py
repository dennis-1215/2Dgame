from pico2d import *
from random import *
import character

WIDTH, HEIGHT = 1024, 1024

class Enemy:
    def __init__(self):
        self.imageR = load_image('sprites/characters/enemy1R.png')
        self.imageL = load_image('sprites/characters/enemy1L.png')

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
        self.frame = 0
        self.running = True

    def animation(self, character):
        if self.x < character.x: # imageR 사용
            if self.y < character.y:
                # 우상
                self.imageR.clip_draw(136, 615 - self.frame // 10 * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + 1) % 50
            elif self.y > character.y:
                # 우하
                self.imageR.clip_draw(471, 615 - self.frame // 10 * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + 1) % 50
            else:
                # 우측
                self.imageR.clip_draw(203, 615 - self.frame // 10 * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + 1) % 50
        elif self.x > character.x: # imageL 사용
            if self.y < character.y:
                # 좌상
                self.imageL.clip_draw(467, 615 - self.frame // 10 * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + 1) % 50
            elif self.y > character.y:
                # 좌하
                self.imageL.clip_draw(199, 615 - self.frame // 10 * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + 1) % 50
            else:
                # 좌측
                self.imageL.clip_draw(333, 615 - self.frame // 10 * 75, 63, 72, self.x, self.y)
                self.frame = (self.frame + 1) % 50

    def moving(self, character): # 캐릭터 위치 추적
        if self.x < character.x:
            self.x += 1;
        if self.x > character.x:
            self.x -= 1
        if self.y < character.y:
            self.y += 1;
        if self.y > character.y:
            self.y -= 1
        self.animation()

