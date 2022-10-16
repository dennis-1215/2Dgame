from pico2d import *

WIDTH, HEIGHT = 1024, 1024

class Character:
    def __init__(self):
        self.image = load_image('sprites/characters/characters.png')
        self.x, self.y = WIDTH/2, HEIGHT/2
        self.hp = 100
        self.speed = 8
        self.U_check = 0
        self.D_check = 0
        self.R_L_check = 3
        self.move = 0
        self.frame = 0
        self.running = True

    def animation(self):
        if self.R_L_check == 1 and self.move != 0:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 40
        elif self.R_L_check == 2 and self.move != 0:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 40
        elif self.R_L_check % 2 == 1 and self.move != 0:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 40
        elif self.R_L_check % 2 == 0 and self.move != 0:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 40
        elif self.R_L_check % 2 == 1 and self.move == 0:
            self.frame = 0
            self.image.clip_draw(36 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 20
        elif self.R_L_check % 2 == 0 and self.move == 0:
            self.frame = 0
            self.image.clip_draw(324 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 20
        delay(0.03)
    def moving(self):
        if self.R_L_check == 1 :
            if self.x < WIDTH:
                self.x += self.speed
        if self.R_L_check == 2:
            if self.x > 0:
                self.x -= self.speed
        if self.U_check == 1:
            if self.y < HEIGHT:
                self.y += self.speed
        if self.D_check == 1:
            if self.y > 0:
                self.y -= self.speed
