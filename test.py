from pico2d import *

class Whip:
    image = None
    def __init__(self):
        if Whip.image == None:
            self.image = load_image("sprites/characters/items.png")
            #self.font = load_font('KO.ttf', 16)
        self.name = 'Whip'
        self.damage = 15
        self.cooltime = 2.0
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
        self.x, self.y = 362, 392-170
        self.width, self.height = 14, 14

    def choice_draw(self, x, y):
        self.image.clip_draw(self.x, self.y, self.width, self.height, x, y)
        self.font.draw(x + 10, y - 50, f'{self.description[self.level]}', (200, 200, 200))

    def play_draw(self, x, y):
        pass

    def update(self):
        pass

whip = Whip()