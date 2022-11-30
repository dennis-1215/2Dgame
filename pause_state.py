from pico2d import *
import game_framework
import game_world
import play_state

WIDTH, HEIGHT = 1024, 1024

image = None
title_frame = 0

def enter():
    global image
    image = load_image('sprites/framework/pause.png')

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()

        play_state.player.handle_event(event)

def draw():
    image.clip_draw(0, 0, WIDTH, HEIGHT, WIDTH / 2, HEIGHT / 2)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
