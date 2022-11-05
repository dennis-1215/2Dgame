from pico2d import *
import game_framework
import play_state

WIDTH, HEIGHT = 1024, 1024

image_LU, image_sub  = None, None
def enter():
    global image_LU, image_sub, title_frame
    image_LU = load_image('sprites/framework/level_up.png')
    image_sub = load_image('sprites/framework/title_sub.png')

def exit():
    global image_LU, image_sub
    del image_LU
    del image_sub

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_state()
    pass

def draw():
    image_LU.clip_draw(0, 0, 560, 756, WIDTH / 2, HEIGHT / 2, 560, 756)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
