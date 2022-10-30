from pico2d import *

WIDTH, HEIGHT = 1024, 1024

class Character:
    def __init__(self):
        self.image = load_image('sprites/characters/characters.png')
        self.x, self.y = 0, 0
        self.max_hp = 1000
        self.hp = 1000
        self.level = 0
        self.max_exp = 500
        self.exp = 0
        self.atk = 10
        self.speed = 8
        self.U_check = 0
        self.D_check = 0
        self.R_L_check = 3
        self.move = 0
        self.frame = 0
        self.running = True

    def draw_status(self):
        self.image.clip_draw(0, 1077, 2, 1, WIDTH / 2 - 17 , HEIGHT / 2 - 20, 80, 4) # 최대 체력바
        self.image.clip_draw(2, 448, 2, 1, WIDTH / 2 - 17, HEIGHT / 2 - 20, 80 * self.hp / self.max_hp, 4) # 현재 체력바
        self.image.clip_draw(0, 1077, 2, 1, 0, HEIGHT - 5, WIDTH * 2, 10) # 최대 경험치 바
        self.image.clip_draw(0, 1, 2, 1, 0, HEIGHT - 5, WIDTH * 2 * self.exp / self.max_exp, 10)  # 현재 경험치 바


    def animation(self):
        if self.R_L_check == 1 and self.move != 0:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, WIDTH/2, HEIGHT/2)
            self.frame = (self.frame + 1) % 40
        elif self.R_L_check == 2 and self.move != 0:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, WIDTH/2, HEIGHT/2)
            self.frame = (self.frame + 1) % 40
        elif self.R_L_check % 2 == 1 and self.move != 0:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, WIDTH/2, HEIGHT/2)
            self.frame = (self.frame + 1) % 40
        elif self.R_L_check % 2 == 0 and self.move != 0:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, WIDTH/2, HEIGHT/2)
            self.frame = (self.frame + 1) % 40
        elif self.R_L_check % 2 == 1 and self.move == 0:
            self.frame = 0
            self.image.clip_draw(36 + self.frame // 10 * 35, 171, 35, 34, WIDTH/2, HEIGHT/2)
            self.frame = (self.frame + 1) % 20
        elif self.R_L_check % 2 == 0 and self.move == 0:
            self.frame = 0
            self.image.clip_draw(324 + self.frame // 10 * 35, 171, 35, 34, WIDTH/2, HEIGHT/2)
            self.frame = (self.frame + 1) % 20

        delay(0.03)
    def moving(self):
        # move about map + enemy
        if self.R_L_check == 1:
            self.x += self.speed
        if self.R_L_check == 2:
            self.x -= self.speed
        if self.U_check == 1:
            self.y += self.speed
        if self.D_check == 1:
            self.y -= self.speed

        # map cycle
        if self.x >= WIDTH:
            self.x = self.x - WIDTH
        if self.y >= HEIGHT:
            self.y = self.y - HEIGHT
        if self.x <= -WIDTH:
            self.x = WIDTH + self.x
        if self.y <= -HEIGHT:
            self.y = HEIGHT + self.y
