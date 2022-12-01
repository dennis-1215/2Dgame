from pico2d import *
from random import *

import game_framework
import game_world
import play_state
import pause_state

WIDTH, HEIGHT = 1024, 1024

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

image_LU, image_choice = None, None
choice = 0
frame = 0
random_item = [None, None, None]

def enter():
    global image_LU, image_choice, choice, random_item

    image_LU = load_image('sprites/framework/level_up.png')
    image_choice = load_image('sprites/framework/UI.png')
    choice = 0
    mix()
def exit():
    pass

def handle_events():
    global choice, random_item
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN or event.key == SDLK_SPACE:
            play_state.equipment_list[random_item[choice]].level += 1
            play_state.equipment_list[random_item[choice]].choiced()

            mix()

            game_framework.pop_state()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if choice > 0:
                choice -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if choice < 2:
                choice += 1

        play_state.player.handle_event(event)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw(play_state.player)

    image_LU.clip_draw(0, 0, 560, 756, WIDTH / 2, HEIGHT / 2, 560, 756)
    image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 0, '', WIDTH/2 - 300, HEIGHT/2 + 170 - (choice * 150), 30, 26)
    image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 3.141592, 'v', WIDTH / 2 + 300, HEIGHT / 2 + 170 - (choice * 150), 30, 26)

    play_state.equipment_list[random_item[0]].choice_draw(WIDTH/2 - 300, HEIGHT/2 + 180)
    play_state.equipment_list[random_item[1]].choice_draw(WIDTH/2 - 300, HEIGHT/2 + 170 - 150)
    play_state.equipment_list[random_item[2]].choice_draw(WIDTH/2 - 300, HEIGHT/2 + 170 - 300)

    update_canvas()
def update():
    global frame
    frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7

def pause():
    pass

def resume():
    pass

def mix():
    random_item[0] = randint(0, len(play_state.equipment_list) - 2)
    random_item[1] = randint(0, len(play_state.equipment_list) - 2)
    random_item[2] = randint(0, len(play_state.equipment_list) - 2)

    while True:
        if play_state.equipment_list[random_item[0]].level > 6:
            random_item[0] = randint(0, len(play_state.equipment_list) - 2)
        if random_item[0] == random_item[1]:
            random_item[1] = randint(0, len(play_state.equipment_list) - 2)
            if play_state.equipment_list[random_item[1]].level > 6:
                random_item[1] = randint(0, len(play_state.equipment_list) - 2)
            continue
        if random_item[2] == random_item[1] or random_item[2] == random_item[0]:
            random_item[2] = randint(0, len(play_state.equipment_list) - 2)
            if play_state.equipment_list[random_item[2]].level > 6:
                random_item[2] = randint(0, len(play_state.equipment_list) - 2)
        else:
            break