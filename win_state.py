from pico2d import *
import game_framework
import play_state
import title_state
import schedule

WIDTH, HEIGHT = 1024, 1024

image = None
title_frame = 0

def enter():
    global image
    image = load_image('sprites/framework/stageComplete.png')

def exit():
    play_state.play_time = 0
    play_state.job = schedule.every(1).seconds.do(play_state.play_timer)
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN or event.key == SDLK_SPACE:
            game_framework.change_state(title_state)

def draw():
    image.clip_draw(0, 0, 379, 132, WIDTH / 2, HEIGHT / 2, WIDTH/2, HEIGHT/4)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
