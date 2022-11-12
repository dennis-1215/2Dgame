from pico2d import *
import game_framework
import game_world
import play_state
import title_state

WIDTH, HEIGHT = 1024, 1024

image = None
title_frame = 0

def enter():
    global image
    image = load_image('sprites/framework/gameover.png')

def exit():
    game_world.clear()
    play_state.play_time = 0
    print(game_world.objects)
    print(game_world.collision_group)
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.change_state(title_state)

def draw():
    image.clip_draw(0, 0, 400, 300, WIDTH / 2, HEIGHT / 2, WIDTH/1.5, HEIGHT/1.5)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
