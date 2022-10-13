from pico2d import *

WIDTH, HEIGHT = 1024, 1024

class Character:
    def __init__(self):
        self.image = load_image('sprites/characters/characters.png')
        self.x, self.y = WIDTH/2, HEIGHT/2
        self.U_check = 0
        self.D_check = 0
        self.L_check = 3
        self.R_check = 3
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
                self.move = 1
                self.x += 8
        if self.L_check == 1:
            if self.x > 0:
                self.x -= 8
                self.move = 1
        if self.U_check == 1:
            if self.y < HEIGHT:
                self.y += 8
                self.move = 1
        if self.D_check == 1:
            if self.y > 0:
                self.y -= 8
                self.move = 1
        self.animation()

    def input_key(self):
        for event in get_events():
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.move = 1
                    self.R_check = 1
                if event.key == SDLK_LEFT:
                    self.move = 1
                    self.L_check = 1
                if event.key == SDLK_UP:
                    self.move = 1
                    self.U_check = 1
                if event.key == SDLK_DOWN:
                    self.move = 1
                    self.D_check = 1
                if event.key == SDLK_ESCAPE:
                    self.running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.move = 0
                    self.R_check = 3
                if event.key == SDLK_LEFT:
                    self.move = 0
                    self.L_check = 3
                if event.key == SDLK_UP:
                    self.move = 0
                    self.U_check = 0
                if event.key == SDLK_DOWN:
                    self.move = 0
                    self.D_check = 0
        self.moving()
