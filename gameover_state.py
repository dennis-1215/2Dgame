from pico2d import *
import game_framework
import game_world
import play_state
import result_state

WIDTH, HEIGHT = 1024, 1024

image, bgm = None, None
title_frame = 0

def enter():
    global image, bgm
    image = load_image('sprites/framework/gameover.png')
    bgm = load_music('sounds/gameover.ogg')
    bgm.set_volume(32)
    bgm.play()

def exit():
    game_world.clear()
    play_state.play_time = 0
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.push_state(result_state)

def draw():
    image.clip_draw(0, 0, 400, 300, WIDTH / 2, HEIGHT / 2, WIDTH/1.5, HEIGHT/1.5)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
