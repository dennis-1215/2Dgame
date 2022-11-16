from pico2d import *
import Item
import schedule
import game_framework
import gameover_state
import game_world
import play_state

WIDTH, HEIGHT = 1024, 1024

# Player Run Speed
PIXEL_PER_METER = (32.0 / 1.0) # 32 pixel = 100 cm
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Player Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

RD, LD, RU, LU, UD, DD, UU, DU = range(8)

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
    def enter(self, event):
        self.dir = 0

    @staticmethod
    def exit(self, event):
        if event == RD or event == LU:
            self.face_dir = 1
        elif event == LD or event == RU:
            self.face_dir = -1
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    @staticmethod
    def draw(self):
        if self.frame > 1:
            self.frame = self.frame % 2

        if self.face_dir == 1:
            self.image.clip_draw(36 + int(self.frame) * 35, 171, 35, 34, WIDTH/2, HEIGHT/2, self.w, self.h)
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        else:
            self.image.clip_draw(324 + int(self.frame) * 35, 171, 35, 34, WIDTH/2, HEIGHT/2, self.w, self.h)
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2


class RUN: # 수평 이동
    def enter(self, event):
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
        if event == RD:
            self.face_dir = 1
        elif event == LD:
            self.face_dir = -1

    def do(self):
        # move about map + enemy
        if self.dir == 1:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 2:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 3:
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 4:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -1:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -2:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -3:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -4:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
            self.y -= RUN_SPEED_PPS * game_framework.frame_time

        # map cycle
        if self.x >= 2 * WIDTH:
            self.x = self.x - 2 * WIDTH
        if self.y >= 2 * HEIGHT:
            self.y = self.y - 2 * HEIGHT
        if self.x <= -2 * WIDTH:
            self.x = 2 * WIDTH + self.x
        if self.y <= -2 * HEIGHT:
            self.y = 2 * HEIGHT + self.y
        pass
    def draw(self):
        if self.dir == 1 or self.dir == 4 or self.dir == -2:
            self.image.clip_draw(72 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)

        elif self.dir == -1 or self.dir == -4 or self.dir == 2:
            self.image.clip_draw(216 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)

        if self.dir == 3 or self.dir == -3:
            if self.face_dir == 1:
                self.image.clip_draw(72 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)
            else:
                self.image.clip_draw(216 + int(self.frame) // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4


class RUN2: # 수직 이동
    def enter(self, event):
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
        if event == RD:
            self.face_dir = 1
        elif event == LD:
            self.face_dir = -1

    def do(self):
        # move about map + enemy
        if self.dir == 1:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 2:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 3:
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 4:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -1:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -2:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -3:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -4:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
            self.y -= RUN_SPEED_PPS * game_framework.frame_time

        # map cycle
        if self.x >= 2 * WIDTH:
            self.x = self.x - 2 *WIDTH
        if self.y >= 2 * HEIGHT:
            self.y = self.y - 2 *HEIGHT
        if self.x <= -2 * WIDTH:
            self.x = 2 *WIDTH + self.x
        if self.y <= -2 * HEIGHT:
            self.y = 2 * HEIGHT + self.y
        pass
    def draw(self):
        if self.dir == 1 or self.dir == 4 or self.dir == -2:
            self.image.clip_draw(72 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)

        elif self.dir == -1 or self.dir == -4 or self.dir == 2:
            self.image.clip_draw(216 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)

        if self.dir == 3 or self.dir == -3:
            if self.face_dir == 1:
                self.image.clip_draw(72 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)

            else:
                self.image.clip_draw(216 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

class RUN3: # 대각 이동
    def enter(self, event):
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
        if event == RD:
            self.face_dir = 1
        elif event == LD:
            self.face_dir = -1

    def do(self):
        # move about map + enemy
        if self.dir == 1:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 2:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 3:
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == 4:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -1:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -2:
            self.x += RUN_SPEED_PPS * game_framework.frame_time
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -3:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.dir == -4:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
            self.y -= RUN_SPEED_PPS * game_framework.frame_time

        # map cycle
        if self.x >= 2 * WIDTH:
            self.x = self.x - 2 * WIDTH
        if self.y >= 2 * HEIGHT:
            self.y = self.y - 2 * HEIGHT
        if self.x <= -2 * WIDTH:
            self.x = 2 * WIDTH + self.x
        if self.y <= -2 * HEIGHT:
            self.y = 2 * HEIGHT + self.y
        pass
    def draw(self):
        if self.dir == 1 or self.dir == 4 or self.dir == -2:
            self.image.clip_draw(72 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)

        elif self.dir == -1 or self.dir == -4 or self.dir == 2:
            self.image.clip_draw(216 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)

        if self.dir == 3 or self.dir == -3:
            if self.face_dir == 1:
                self.image.clip_draw(72 + int(self.frame) * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)

            else:
                self.image.clip_draw(216 + int(self.frame) // 10 * 35, 171, 35, 34, WIDTH / 2, HEIGHT / 2, self.w, self.h)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UU: RUN2, DU: RUN2, UD: RUN2, DD: RUN2},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UU: RUN3, DU: RUN3, UD: RUN3, DD: RUN3},
    RUN2: {RU: RUN3, LU: RUN3, RD: RUN3, LD: RUN3, UU: IDLE, DU: IDLE, UD: IDLE, DD: IDLE},
    RUN3: {RU: RUN2, LU: RUN2, RD: RUN2, LD: RUN2, UU: RUN, DU: RUN, UD: RUN, DD: RUN}
}


class Character:
    def __init__(self):
        self.image = load_image('sprites/characters/characters.png')
        self.x, self.y = 0, 0
        self.w, self.h = 50, 55
        self.dir, self.face_dir = 0, 1
        self.max_hp = 1000
        self.hp = 1000
        self.level = 0
        self.max_exp = 100
        self.exp = 0
        self.damage = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self, player):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}     Event {event}')
            self.cur_state.enter(self, event)

    def draw(self, player):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')
        self.image.clip_draw(0, 1077, 2, 1, WIDTH / 2 - 17, HEIGHT / 2 - 20, 80, 4)  # 최대 체력바
        self.image.clip_draw(2, 448, 2, 1, WIDTH / 2 - 17, HEIGHT / 2 - 20, 80 * self.hp / self.max_hp, 4)  # 현재 체력바
        self.image.clip_draw(0, 1077, 2, 1, 0, HEIGHT - 5, WIDTH * 2, 10)  # 최대 경험치 바
        self.image.clip_draw(0, 1, 2, 1, 0, HEIGHT - 5, WIDTH * 2 * self.exp / self.max_exp, 10)  # 현재 경험치 바
        draw_rectangle(*self.get_bb(player))

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def handle_collision(self, other, group):
        if group == 'player:enemy':
            self.hp -= other.atk
            if self.hp <= 0:
                game_framework.push_state(gameover_state)

    def get_bb(self, player):
        return WIDTH/2 - self.w/2, HEIGHT/2 - self.h/2, WIDTH/2 + self.w/2, HEIGHT/2 + self.h/2

