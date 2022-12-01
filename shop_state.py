from pico2d import *
import game_framework
import main_state

WIDTH, HEIGHT = 1024, 1024

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

image, image_bg, image_choice, font = None, None, None, None
choice = 0
frame = 0
account_item_list = []



def enter():
    global image, image_bg, image_choice, font, choice, account_item_list, hp, speed, bonus_exp, bonus_gold, damage_up, armor
    choice = 0
    image_bg = load_image('sprites/framework/main_bg.png')
    image = load_image('sprites/framework/shop.png')
    image_choice = load_image('sprites/framework/UI.png')
    font = load_font('font/KO.ttf', 20)




def exit():
    global image, image_choice, font
    del image, image_choice, font

    main_state.account_save()

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
                if main_state.account.account_gold >= main_state.hp.need_gold:
                    main_state.account.account_gold -= main_state.hp.need_gold
                    main_state.hp.level += 1
                    main_state.account.hp_level += 1
            elif choice == 2:
                if main_state.account.account_gold >= main_state.speed.need_gold:
                    main_state.account.account_gold -= main_state.speed.need_gold
                    main_state.speed.level += 1
                    main_state.account.speed_level += 1
            elif choice == 3:
                if main_state.account.account_gold >= main_state.bonus_exp.need_gold:
                    main_state.account.account_gold -= main_state.bonus_exp.need_gold
                    main_state.bonus_exp.level += 1
                    main_state.account.bonus_exp_level += 1
            elif choice == 4:
                if main_state.account.account_gold >= main_state.bonus_gold.need_gold:
                    main_state.account.account_gold -= main_state.bonus_gold.need_gold
                    main_state.bonus_gold.level += 1
                    main_state.account.bonus_gold_level += 1
            elif choice == 5:
                if main_state.account.account_gold >= main_state.damage_up.need_gold:
                    main_state.account.account_gold -= main_state.damage_up.need_gold
                    main_state.damage_up.level += 1
                    main_state.account.damage_up_level += 1
            elif choice == 6:
                if main_state.account.account_gold >= main_state.armor.need_gold:
                    main_state.account.account_gold -= main_state.armor.need_gold
                    main_state.armor.level += 1
                    main_state.account.armor_level += 1

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
        main_state.hp.choiced_draw()
    elif choice == 2:
        main_state.speed.choiced_draw()
    elif choice == 3:
        main_state.bonus_exp.choiced_draw()
    elif choice == 4:
        main_state.bonus_gold.choiced_draw()
    elif choice == 5:
        main_state.damage_up.choiced_draw()
    elif choice == 6:
        main_state.armor.choiced_draw()
    update_canvas()

def update():
    global frame
    frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
    main_state.account.hp_level = main_state.hp.level
    main_state.account.speed_level = main_state.speed.level
    main_state.account.bonus_exp_level = main_state.bonus_exp.level
    main_state.account.bonus_gold_level = main_state.bonus_gold.level
    main_state.account.damage_up_level = main_state.damage_up.level
    main_state.account.armor_level = main_state.armor.level

def pause():
    pass

def resume():
    pass

