from pico2d import *
import game_framework

class Account_hp:
    image = None
    def __init__(self, level):
        if Account_hp.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = '최대 체력'
        self.level = level
        self.need_gold = 400 * (1 + self.level)
        self.add_hp = 100 * self.level
        self.description = "최대 체력이 증가합니다."

        self.x, self.y = 404, 392 - 187
        self.width, self.height = 15, 15

    def choiced_draw(self):
        self.image.clip_draw(self.x, self.y, self.width, self.height, 312, 195, self.width * 2, self.height * 2)
        self.font.draw(400, 200, f'{self.description}')
        self.font.draw(280, 240, f'{self.name}')
        self.font.draw(700, 200, f'Lv. {self.level}')
        self.font.draw(680, 240, f'가격: {self.need_gold}')

    def choiced(self):
        self.level += 1
        pass

class Account_speed(Account_hp):
    image = None
    def __init__(self, level):
        if Account_speed.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = '이동 속도'
        self.level = level
        self.need_gold = 400 * (1 + self.level)
        self.multiply_speed = 1.0 + (0.02 * self.level)
        self.description = "이동 속도가 증가합니다."

        self.x, self.y = 334, 392 - 295
        self.width, self.height = 14, 15

class Account_bonus_exp(Account_hp):
    image = None
    def __init__(self, level):
        if Account_speed.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = '성장'
        self.level = level
        self.need_gold = 400 * (1 + self.level)
        self.multiply_bonus_exp = 1.0 + (0.1 * self.level)
        self.description = "얻는 경험치가 증가합니다."

        self.x, self.y = 335, 392 - 205
        self.width, self.height = 14, 15

class Account_bonus_gold(Account_hp):
    image = None
    def __init__(self, level):
        if Account_speed.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = '탐욕'
        self.level = level
        self.need_gold = 400 * (1 + self.level)
        self.multiply_bonus_gold = 1.0 + (0.1 * self.level)
        self.description = "얻는 골드가 증가합니다."

        self.x, self.y = 418, 392 - 271
        self.width, self.height = 9, 8
    def choiced_draw(self):
        self.image.clip_draw(self.x, self.y, self.width, self.height, 312, 195, self.width * 3, self.height * 3)
        self.font.draw(400, 200, f'{self.description}')
        self.font.draw(280, 240, f'{self.name}')
        self.font.draw(700, 200, f'Lv. {self.level}')

class Account_damage(Account_hp):
    image = None
    def __init__(self, level):
        if Account_speed.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = '피해량'
        self.level = level
        self.need_gold = 400 * (1 + self.level)
        self.plus_damage = 2 * self.level
        self.description = "주는 피해량이 증가합니다."

        self.x, self.y = 177, 392 - 361
        self.width, self.height = 14, 14

class Account_armor(Account_hp):
    image = None
    def __init__(self, level):
        if Account_speed.image == None:
            self.image = load_image('sprites/characters/items.png')
            self.font = load_font('font/KO.ttf', 20)
        self.name = '방어력'
        self.level = level
        self.need_gold = 400 * (1 + self.level)
        self.reduce_damage = self.level
        self.description = "받는 피해가 감소합니다."

        self.x, self.y = 414, 392 - 17
        self.width, self.height = 15, 16
