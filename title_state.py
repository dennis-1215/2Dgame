from pico2d import *
import game_framework
import main_state

WIDTH, HEIGHT = 1024, 1024

image_bg, image_sub, intro_music = None, None, None
title_frame = 0

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

def enter():
    global image_bg, image_sub, title_frame, intro_music
    image_bg = load_image('sprites/framework/title.png')
    image_sub = load_image('sprites/framework/title_sub.png')
    intro_music = load_music('sounds/titleintro.ogg')
    intro_music.set_volume(22)
    intro_music.play()

def exit():
    global image_bg, image_sub
    del image_bg
    del image_sub

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image_bg.clip_draw(0, 0, 400, 300, WIDTH/2, HEIGHT/2, WIDTH, HEIGHT)
    if int(title_frame) == 0:
        image_sub.clip_draw(0, 0, 400, 300, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    update_canvas()

def update():
    global title_frame
    title_frame = (title_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2


def pause():
    pass

def resume():
    pass



