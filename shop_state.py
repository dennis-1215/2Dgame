from pico2d import *
import game_framework
import account_items

WIDTH, HEIGHT = 1024, 1024

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

image, image_bg, image_choice, font = None, None, None, None
hp, speed, bonus_exp, bonus_gold, damage_up, armor = None, None, None, None, None, None
choice = 0
frame = 0
account_item_list = []

class Account_data:
    def __init__(self):
        pass


def enter():
    global image, image_bg, image_choice, font, choice, account_item_list, hp, speed, bonus_exp, bonus_gold, damage_up, armor
    choice = 0
    image_bg = load_image('sprites/framework/main_bg.png')
    image = load_image('sprites/framework/shop.png')
    image_choice = load_image('sprites/framework/UI.png')
    font = load_font('KO.ttf', 20)

    hp, speed, bonus_exp, bonus_gold, damage_up, armor = account_items.Account_hp(0), account_items.Account_speed(0), account_items.Account_bonus_exp(0), account_items.Account_bonus_gold(0), account_items.Account_damage(0), account_items.Account_armor(0)
    account_item_list = [hp, speed, bonus_exp, bonus_gold, damage_up, armor]


def exit():
    global image, image_choice, font
    del image, image_choice, font

def handle_events():
    global choice
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN or event.key == SDLK_SPACE:
            if choice == 0:
                game_framework.pop_state()
            elif choice == 1:
                # game_framework.push_state(shop_state)
                pass
            elif choice == 2:
                # game_framework.push_state(option_state)
                pass
            elif choice == 3:
                game_framework.quit()
                pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if choice > 0:
                choice -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if choice < 6:
                choice += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if choice > 0:
                choice -= 3
                if choice <= 0:
                    choice = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if choice == 0:
                choice = 1
            elif choice < 6:
                choice += 3
                if choice > 6:
                    choice -= 3

def draw():

    clear_canvas()

    # 배경
    image_bg.clip_draw(0, 0, 400, 300, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    image.clip_draw(0, 0, 560, 756, WIDTH / 2, HEIGHT / 2, 560, 756)

    # 선택지
    image_choice.clip_draw(464, 1024 - 553, 47, 31, WIDTH * 3 / 4, HEIGHT - 50, 100, 60)
    font.draw(WIDTH * 3 / 4 - 15, HEIGHT - 50, '뒤로', (255, 255, 255))


    # 선택 중인 상자 표시
    if choice == 0:
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 0, '', WIDTH * 3 / 4 - 70, HEIGHT - 50, 30, 26)
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 3.141592, 'v', WIDTH * 3 / 4 + 70, HEIGHT - 50, 30, 26)

    elif choice <= 3:
        image_choice.clip_composite_draw(259, 1024 - 404, 6, 6, 0, '', WIDTH / 2 - 255 + (180 * (choice - 1)), HEIGHT / 2 + 115, 12, 12)
        image_choice.clip_composite_draw(259, 1024 - 404, 6, 6, 0, 'h', WIDTH / 2 - 105 + (180 * (choice - 1)), HEIGHT / 2 + 115, 12, 12)
        image_choice.clip_composite_draw(259, 1024 - 404, 6, 6, 0, 'v', WIDTH / 2 - 255 + (180 * (choice - 1)), HEIGHT / 2 + 265, 12, 12)
        image_choice.clip_composite_draw(259, 1024 - 404, 6, 6, 0, 'hv', WIDTH / 2 - 105 + (180 * (choice - 1)), HEIGHT / 2 + 265, 12, 12)

    elif choice <= 6:
        image_choice.clip_composite_draw(259, 1024 - 404, 6, 6, 0, '', WIDTH / 2 - 255 + (180 * (choice - 4)), HEIGHT / 2 - 75, 12, 12)
        image_choice.clip_composite_draw(259, 1024 - 404, 6, 6, 0, 'h', WIDTH / 2 - 105 + (180 * (choice - 4)), HEIGHT / 2 - 75, 12, 12)
        image_choice.clip_composite_draw(259, 1024 - 404, 6, 6, 0, 'v', WIDTH / 2 - 255 + (180 * (choice - 4)), HEIGHT / 2 + 75, 12, 12)
        image_choice.clip_composite_draw(259, 1024 - 404, 6, 6, 0, 'hv', WIDTH / 2 - 105 + (180 * (choice - 4)), HEIGHT / 2 + 75, 12, 12)

    if choice == 1:
        hp.choiced_draw()
    elif choice == 2:
        speed.choiced_draw()
    elif choice == 3:
        bonus_exp.choiced_draw()
    elif choice == 4:
        bonus_gold.choiced_draw()
    elif choice == 5:
        damage_up.choiced_draw()
    elif choice == 6:
        armor.choiced_draw()
    update_canvas()

def update():
    global frame
    frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7

def pause():
    pass

def resume():
    pass

