from pico2d import *
import game_framework
import main_state
import game_world
import play_state

WIDTH, HEIGHT = 1024, 1024

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

image, image_bg, image_choice, font , big_font = None, None, None, None, None
gold = 0
choice = 0
frame = 0
time = 0



def enter():
    global image, image_bg, image_choice, font, choice, gold, hp, speed, bonus_exp, bonus_gold, damage_up, armor, big_font
    choice = 0
    gold = int((int(play_state.player.gold) + play_state.play_time // 60 + play_state.player.kill_count // 50) * main_state.bonus_gold.multiply_bonus_gold)
    image_bg = load_image('sprites/framework/main_bg.png')
    image = load_image('sprites/framework/result.png')
    image_choice = load_image('sprites/framework/UI.png')
    font = load_font('font/KO.ttf', 20)
    big_font = load_font('font/KO.ttf', 40)




def exit():
    global image, image_choice, font
    del image, image_choice, font

    game_world.clear()
    play_state.play_time = 0

    main_state.account_save()

def handle_events():
    global choice, gold
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN or event.key == SDLK_SPACE:
            main_state.account.account_gold += gold
            game_framework.change_state(main_state)


def draw():
    global gold
    clear_canvas()

    # 배경
    image_bg.clip_draw(0, 0, 400, 300, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    image.clip_draw(0, 0, 560, 756, WIDTH / 2, HEIGHT / 2, 560, 756)

    if time > 0.5:
        image_choice.clip_draw(288, 1024 - 371, 8, 7, 280, 700, 16, 14)
    if time > 1.0:
        font.draw(300, 700, f'{play_state.player.kill_count}', (255, 255, 255))
    if time > 1.5:
        font.draw(260, 600, '생존한 시간: ', (255, 255, 255))
    if time > 2.0:
        font.draw(380, 600, f'{int(play_state.play_time)} 초', (255, 255, 255))
    if time > 2.5:
        font.draw(260, 500, '획득한 골드: ', (255, 255, 255))
    if time > 3.0:
        font.draw(380, 500, f'{int(play_state.player.gold)} 원', (255, 255, 255))
    if time > 3.5:
        font.draw(260, 450, '최종 보상 ', (255, 255, 255))
        font.draw(WIDTH/2 - 250, 420, '-----------------------------------------------', (255, 255, 255))
    if time > 5.0:
        image_choice.clip_draw(241, 1024 - 373, 10, 10, 280, 300, 30, 30)
        big_font.draw(380, 300, f'{gold} 원', (255, 255, 255))
    update_canvas()

def update():
    global frame, time
    frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
    time += game_framework.frame_time

def pause():
    pass

def resume():
    pass

