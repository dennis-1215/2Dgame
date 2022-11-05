from pico2d import *
import Item
import schedule
import game_framework

WIDTH, HEIGHT = 1024, 1024

RD, LD, RU, LU, UD, DD, UU, DU= range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU
}

class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1


    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.frame = 0
            self.image.clip_draw(36 + self.frame // 10 * 35, 171, 35, 34, WIDTH/2, HEIGHT/2)
            self.frame = (self.frame + 1) % 20
        else:
            self.frame = 0
            self.image.clip_draw(324 + self.frame // 10 * 35, 171, 35, 34, WIDTH/2, HEIGHT/2)
            self.frame = (self.frame + 1) % 20


class RUN: # 수평 이동
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        if event == UD:
            self.dir += 3
        elif event == DD:
            self.dir -= 3
        elif event == UU:
            self.dir -= 3
        elif event == DU:
            self.dir += 3
    def exit(self, event):
        if event == RD or event == RU:
            self.face_dir = 1
        elif event == LD or event == LU:
            self.face_dir = -1

    def do(self):
        pass
    def draw(self):
        if self.dir == 1 or self.dir == 4 or self.dir == -2:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
            self.frame = (self.frame + 1) % 40
        elif self.dir == -1 or self.dir == -4 or self.dir == 2:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
            self.frame = (self.frame + 1) % 40

        if self.dir == 3 or self.dir == -3:
            if self.face_dir == 1:
                self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
                self.frame = (self.frame + 1) % 40
            else:
                self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
                self.frame = (self.frame + 1) % 40

class RUN2: # 수직 이동
    def enter(self, event):
        print('ENTER RUN2')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

        if event == UD:
            self.dir += 3
        elif event == DD:
            self.dir -= 3
        elif event == UU:
            self.dir -= 3
        elif event == DU:
            self.dir += 3

    def exit(self, event):
        if event == RD or event == RU:
            self.face_dir = 1
        elif event == LD or event == LU:
            self.face_dir = -1

    def do(self):
        pass
    def draw(self):
        if self.dir == 1 or self.dir == 4 or self.dir == -2:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
            self.frame = (self.frame + 1) % 40
        elif self.dir == -1 or self.dir == -4 or self.dir == 2:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
            self.frame = (self.frame + 1) % 40

        if self.dir == 3 or self.dir == -3:
            if self.face_dir == 1:
                self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
                self.frame = (self.frame + 1) % 40
            else:
                self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
                self.frame = (self.frame + 1) % 40

class RUN3: # 대각 이동
    def enter(self, event):
        print('ENTER RUN3')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

        if event == UD:
            self.dir += 3
        elif event == DD:
            self.dir -= 3
        elif event == UU:
            self.dir -= 3
        elif event == DU:
            self.dir += 3

    def exit(self, event):
        if event == RD or event == RU:
            self.face_dir = 1
        elif event == LD or event == LU:
            self.face_dir = -1

    def do(self):
        pass
    def draw(self):
        if self.dir == 1 or self.dir == 4 or self.dir == -2:
            self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
            self.frame = (self.frame + 1) % 40
        elif self.dir == -1 or self.dir == -4 or self.dir == 2:
            self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
            self.frame = (self.frame + 1) % 40

        if self.dir == 3 or self.dir == -3:
            if self.face_dir == 1:
                self.image.clip_draw(72 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
                self.frame = (self.frame + 1) % 40
            else:
                self.image.clip_draw(216 + self.frame // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2)
                self.frame = (self.frame + 1) % 40

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UU: RUN2, DU: RUN2, UD: RUN2, DD: RUN2},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UU: RUN3, DU: RUN3, UD: RUN3, DD: RUN3},
    RUN2: {RU: RUN3, LU: RUN3, RD: RUN3, LD: RUN3, UU: IDLE, DU: IDLE, UD: IDLE, DD: IDLE},
    RUN3: {RU: RUN2, LU: RUN2, RD: RUN2, LD: RUN2, UU: RUN, DU: RUN, UD: RUN, DD: RUN}
}


class Character:
    def __init__(self):
        self.image = load_image('sprites/characters/characters.png')
        self.image_vfx = load_image('sprites/characters/vfx.png')
        self.x, self.y = 0, 0
        self.dir, self.face_dir = 0, 1
        self.max_hp = 1000
        self.hp = 1000
        self.level = 0
        self.max_exp = 100
        self.exp = 0
        self.atk = 10
        self.atk_speed = 2
        self.atk_time = 1
        self.atk_range = 60
        self.speed = 8
        self.move = 0
        self.frame = 0
        self.atk_frame = 1
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}     Event {event}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def draw_status(self):
        self.image.clip_draw(0, 1077, 2, 1, WIDTH / 2 - 17 , HEIGHT / 2 - 20, 80, 4) # 최대 체력바
        self.image.clip_draw(2, 448, 2, 1, WIDTH / 2 - 17, HEIGHT / 2 - 20, 80 * self.hp / self.max_hp, 4) # 현재 체력바
        self.image.clip_draw(0, 1077, 2, 1, 0, HEIGHT - 5, WIDTH * 2, 10) # 최대 경험치 바
        self.image.clip_draw(0, 1, 2, 1, 0, HEIGHT - 5, WIDTH * 2 * self.exp / self.max_exp, 10)  # 현재 경험치 바
    def attack_draw(self):
        if self.face_dir == 1:
            self.image_vfx.clip_composite_draw(0, 985 - 64, 148, 20, 0, '', WIDTH / 2 + 17 + 32, HEIGHT / 2, self.atk_range / 20 * self.atk_frame, self.atk_frame)
        elif self.face_dir == -1:
            self.image_vfx.clip_composite_draw(0, 985 - 64, 148, 20, -3.141592, '', WIDTH / 2 - 17 - 32, HEIGHT/2, self.atk_range / 20 * self.atk_frame, self.atk_frame)
        self.atk_frame = (self.atk_frame + 1) % 20 + 1

    def attack_rect(self, enemy, myutals, items):
        if self.face_dir == 1:
            if enemy.x - WIDTH / 2 <= 35 + self.atk_range and enemy.x > WIDTH/2 and enemy.y - HEIGHT/2 <= 20 and enemy.y >= HEIGHT/2 - 20:
                enemy.hp -= self.atk
                if enemy.hp < 1:
                    myutals.remove(enemy)
                    items.append(Item.Item(enemy.x, enemy.y))
        else:
            if WIDTH / 2 - enemy.x <= 35 + self.atk_range and enemy.x < WIDTH/2 and enemy.y - HEIGHT/2 <= 20 and enemy.y >= HEIGHT/2 - 20:
                enemy.hp -= self.atk
                if enemy.hp < 1:
                    myutals.remove(enemy)
                    items.append(Item.Item(enemy.x, enemy.y))

    def moving(self):
        # move about map + enemy
        if self.dir == 1:
            self.x += self.speed
        elif self.dir == 2:
            self.x -= self.speed
            self.y += self.speed
        elif self.dir == 3:
            self.y += self.speed
        elif self.dir == 4:
            self.x += self.speed
            self.y += self.speed
        elif self.dir == -1:
            self.x -= self.speed
        elif self.dir == -2:
            self.x += self.speed
            self.y -= self.speed
        elif self.dir == -3:
            self.y -= self.speed
        elif self.dir == -4:
            self.x -= self.speed
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

