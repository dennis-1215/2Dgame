from pico2d import *

WIDTH, HEIGHT = 1024, 1024

class Character:
    def __init__(self):
        self.image = load_image('sprites/characters/characters.png')
        self.x, self.y = WIDTH/2, HEIGHT/2
        self.U_check = 0
        self.D_check = 0
        self.L_check = 3
        self.R_check = 0
        self.move = 0
        self.frame = 0
        self.running = True

    def animation(self):
        if self.R_check == 1 and self.move != 0:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 40
        elif self.L_check == 1 and self.move != 0:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 40
        elif self.R_check % 2 == 1 and self.move != 0:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 40
        elif self.L_check % 2 == 1 and self.move != 0:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 40
        elif self.R_check == 3 and self.move == 0:
            self.image.clip_draw(36 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 20
        elif self.L_check == 3 and self.move == 0:
            self.image.clip_draw(324 + self.frame // 10 * 35, 171, 35, 34, self.x, self.y)
            self.frame = (self.frame + 1) % 20
        delay(0.03)
    def moving(self):
        if self.R_check == 1:
            if self.x < WIDTH:
                self.x += 8
        if self.L_check == 1:
            if self.x > 0:
                self.x -= 8
        if self.U_check == 1:
            if self.y < HEIGHT:
                self.y += 8
        if self.D_check == 1:
            if self.y > 0:
                self.y -= 8
