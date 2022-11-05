from pico2d import *
import game_framework
import play_state

WIDTH, HEIGHT = 1024, 1024

image_bg, image_sub = None, None
title_frame = 0

def enter():
    global image_bg, image_sub, title_frame
    image_bg = load_image('sprites/framework/title.png')
    image_sub = load_image('sprites/framework/title_sub.png')

def exit():
    global image_bg, image_sub
    del image_bg
    del image_sub

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_state(play_state)
    pass

def draw():
    clear_canvas()
    image_bg.clip_draw(0, 0, 400, 300, WIDTH/2, HEIGHT/2, WIDTH, HEIGHT)
    if title_frame % 2 == 0:
        image_sub.clip_draw(0, 0, 400, 300, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    update_canvas()

def update():
    global title_frame
    title_frame = (title_frame + 1) % 2
    delay(0.5)

def pause():
    pass

def resume():
    pass



