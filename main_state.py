from pico2d import *
import game_framework
import shop_state
import play_state
import title_state
import account_items
import pickle

WIDTH, HEIGHT = 1024, 1024

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

image_bg, image_choice, font = None, None, None
hp, speed, bonus_exp, bonus_gold, damage_up, armor = None, None, None, None, None, None
account = None

choice = 0
frame = 0


class Account_data:
    def __init__(self):
        self.hp_level = 0
        self.speed_level = 0
        self.bonus_exp_level = 0
        self.bonus_gold_level = 0
        self.damage_up_level = 0
        self.armor_level = 0
        self.account_gold = 300
        self.bgm_volume = 16
        self.sfx_volume = 16
    def __getstate__(self):
        state = {'hp_level': self.hp_level,
                 'speed_level': self.speed_level,
                 'bonus_exp_level': self.bonus_exp_level,
                 'bonus_gold_level': self.bonus_gold_level,
                 'damage_up_level': self.damage_up_level,
                 'armor_level': self.armor_level,
                 'account_gold': self.account_gold,
                 'bgm_volume': self.bgm_volume,
                 'sfx_volume': self.sfx_volume
                 }
        return state
    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

def enter():
    global image_bg, image_choice, font, choice, hp, speed, bonus_exp, bonus_gold, damage_up, armor, account
    choice = 0
    image_bg = load_image('sprites/framework/title.png')
    image_choice = load_image('sprites/framework/UI.png')
    font = load_font('font/KO.ttf', 20)
    account = Account_data()

    with open('account.sav', 'rb') as f:
        try:
            data_check = pickle.load(f)
        except EOFError:
            account_save()

    account_load()

    hp, speed, bonus_exp, bonus_gold, damage_up, armor = account_items.Account_hp(account.hp_level), \
                                                         account_items.Account_speed(account.speed_level), \
                                                         account_items.Account_bonus_exp(account.bonus_exp_level), \
                                                         account_items.Account_bonus_gold(account.bonus_gold_level), \
                                                         account_items.Account_damage(account.damage_up_level), \
                                                         account_items.Account_armor(account.armor_level)
def exit():
    global image_choice, font
    del image_choice, font

def handle_events():
    global choice
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN or event.key == SDLK_SPACE:
            if choice == 0:
                game_framework.change_state(play_state)
            elif choice == 1:
                game_framework.push_state(shop_state)
            elif choice == 2:
                # game_framework.push_state(option_state)
                pass
            elif choice == 3:
                game_framework.quit()
                pass
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_UP or event.key == SDLK_LEFT):
            if choice > 0:
                choice -= 1
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_DOWN or event.key == SDLK_RIGHT):
            if choice < 3:
                choice += 1



def draw():
    clear_canvas()

    image_bg.clip_draw(0, 0, 400, 300, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)

    # 선택지 박스 그리기
    image_choice.clip_draw(454, 1024 - 395, 47, 31, WIDTH / 2, HEIGHT / 2 - 50, 100, 60)
    font.draw(WIDTH / 2 - 35, HEIGHT / 2 - 50, '게임시작', (255, 255, 255))

    image_choice.clip_draw(454, 1024 - 395, 47, 31, WIDTH / 2, HEIGHT / 2 - 150, 100, 60)
    font.draw(WIDTH / 2 - 15, HEIGHT / 2 - 150, '상점', (255, 255, 255))

    image_choice.clip_draw(454, 1024 - 395, 47, 31, WIDTH / 2, HEIGHT / 2 - 250, 100, 60)
    font.draw(WIDTH / 2 - 15, HEIGHT / 2 - 250, '옵션', (255, 255, 255))

    image_choice.clip_draw(464, 1024 - 553, 47, 31, WIDTH / 2, HEIGHT / 2 - 350, 100, 60)
    font.draw(WIDTH / 2 - 35, HEIGHT / 2 - 350, '게임종료', (255, 255, 255))

    # 화살표 그리기
    if choice == 0:
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 0, '', WIDTH / 2 - 70, HEIGHT / 2 - 50, 30, 26)
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 3.141592, 'v', WIDTH / 2 + 70, HEIGHT / 2 - 50, 30, 26)
    elif choice == 1:
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 0, '', WIDTH / 2 - 70, HEIGHT / 2 - 150, 30, 26)
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 3.141592, 'v', WIDTH / 2 + 70, HEIGHT / 2 - 150, 30, 26)
    elif choice == 2:
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 0, '', WIDTH / 2 - 70, HEIGHT / 2 - 250, 30, 26)
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 3.141592, 'v', WIDTH / 2 + 70, HEIGHT / 2 - 250, 30, 26)
    elif choice == 3:
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 0, '', WIDTH / 2 - 70, HEIGHT / 2 - 350, 30, 26)
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 3.141592, 'v', WIDTH / 2 + 70, HEIGHT / 2 - 350, 30, 26)

    update_canvas()

def update():
    global frame
    frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7

def pause():
    pass

def resume():
    pass

def account_save():
    with open('account.sav', 'wb') as f:
        pickle.dump(account, f)

def account_load():
    global account
    with open('account.sav', 'rb') as f:
        account = pickle.load(f)
