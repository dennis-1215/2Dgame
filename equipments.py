from pico2d import *
import game_framework

WIDTH, HEIGHT = 1024, 1024


Whip_TIME_PER_ACTION = 0.5
Whip_ACTION_PER_TIME = 1.0 / Whip_TIME_PER_ACTION
Whip_FRAMES_PER_ACTION = 5

class Whip:
    image = None
    def __init__(self):
        if Whip.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.image_vfx = load_image('sprites/characters/vfx.png')
            self.font = load_font('KO.ttf', 20)
        self.name = 'Whip'
        self.damage = 15
        self.frame = 0
        self.time = 0
        self.cooltime = 0.1
        self.range = 80
        self.level = 0
        self.description = ['바라보는 방향의 반대 방향으로도 1회 공격합니다.',
                            '공격력이 10% 증가합니다.',
                            '공격 사거리가 20% 증가합니다.',
                            '공격력이 20% 증가합니다.',
                            '공격 속도가 20% 상승합니다.',
                            '공격력이 30% 증가합니다.',
                            '공격 사거리가 30% 증가합니다.',
                            ]
        self.x, self.y = 362, 392 - 171
        self.width, self.height = 15, 15

    def choice_draw(self, x, y):
        self.image.clip_draw(self.x, self.y, self.width, self.height, x + 65, y + 30, self.width * 3, self.height*3)
        self.font.draw(x + 50, y - 20, f'{self.description[self.level]}')
        self.font.draw(x + 150, y + 30, f'{self.name}')
        self.font.draw(x + 500, y + 30, f'Lv. {self.level}')

    def draw(self, player):
        if self.time > self.cooltime:
            if player.face_dir == 1:
                self.image_vfx.clip_composite_draw(0, 985 - 64, 148, 20, 0, '', WIDTH / 2 + 17 + player.w, HEIGHT / 2, self.range / 2 * self.frame, 6 * self.frame)
            elif player.face_dir == -1:
                self.image_vfx.clip_composite_draw(0, 985 - 64, 148, 20, 0, 'h', WIDTH / 2 - 17 - player.w, HEIGHT / 2, self.range / 2 * self.frame, 6 * self.frame)
            self.frame = (self.frame + Whip_FRAMES_PER_ACTION * Whip_ACTION_PER_TIME * game_framework.frame_time) % 4
            if self.frame >= 3.9:
                self.time = 0
                self.frame = 0

        draw_rectangle(*self.get_bb(player))
    def update(self, player):
        pass

    def get_bb(self, player):
        if player.face_dir == 1:
            return WIDTH/2, HEIGHT/2 - self.frame * 3, WIDTH/2 + self.range / 2 * self.frame, HEIGHT/2 + self.frame * 3
        if player.face_dir == -1:
            return WIDTH/2, HEIGHT/2 - self.frame * 3, WIDTH/2 - self.range / 2 * self.frame, HEIGHT/2 + self.frame * 3

    def handle_collision(self, other, group):
        if group == 'whip:enemy':
            pass


class Heal(Whip):
    image = None
    def __init__(self):
        if Heal.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = 'Healing'
        self.damage = 10
        self.time = 0
        self.cooltime = 5.0
        self.level = 0
        self.description = ['주기적으로 체력을 소량 회복합니다.',
                            '체력 회복량이 소폭 상승합니다.',
                            '체력 회복 주기가 빨라집니다.',
                            '체력 회복량이 소폭 상승합니다.',
                            '체력 회복 주기가 빨라집니다.',
                            '체력 회복량이 대폭 상승합니다.',
                            '체력 회복 주기가 대폭 감소합니다.',
                            ]
        self.x, self.y = 394, 392 - 102
        self.width, self.height = 12, 12

    def draw(self, player):
        pass

    def get_bb(self, player):
        pass

    def update(self, player):
        pass

class Hp(Whip):
    image = None
    def __init__(self):
        if Hp.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = 'Hp Increase'
        self.level = 0
        self.time = 0
        self.description = ['최대 체력이 10% 증가합니다.',
                            '최대 체력이 10% 증가합니다.',
                            '최대 체력이 20% 증가합니다.',
                            '최대 체력이 20% 증가합니다.',
                            '최대 체력이 20% 증가합니다.',
                            '최대 체력이 30% 증가합니다.',
                            '최대 체력이 40% 증가합니다.',
                            ]
        self.x, self.y = 404, 392-187
        self.width, self.height = 15, 15

    def draw(self, player):
        pass

    def get_bb(self, player):
        pass

    def update(self, player):
        pass

class Garlic(Whip):
    image = None
    def __init__(self):
        if Garlic.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = 'Garlic'
        self.damage = 10
        self.time = 0
        self.cooltime = 3.0
        self.range = 80
        self.level = 0
        self.description = ['일정 범위 내의 적에게 피해를 입힙니다.',
                            '피해 범위가 증가합니다.',
                            '입히는 피해량이 소폭 상승합니다.',
                            '피해를 입히는 주기가 빨라집니다.',
                            '피해 범위가 증가합니다.',
                            '입히는 피해량이 상승합니다.',
                            '피해 범위가 증가하고, 피해를 입히는 주기가 빨라집니다.',
                            ]
        self.x, self.y = 406, 392-363
        self.width, self.height = 11, 11

    def draw(self, player):
        draw_rectangle(*self.get_bb(player))

    def get_bb(self, player):
        return 0, 0, 0, 0
        #return WIDTH/2 - self.range, HEIGHT/2 - self.range, WIDTH/2 + self.range , HEIGHT/2 + self.range

    def handle_collision(self, other, group):
        if group == 'garlic:enemy':
            if self.level > 0:
                other.hp -= self.damage
    def update(self, player):
        pass
