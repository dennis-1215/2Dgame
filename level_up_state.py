from pico2d import *
import game_framework
import game_world
import play_state

WIDTH, HEIGHT = 1024, 1024

image_LU, image_choice = None, None
choice = 0
frame = 0
def enter():
    global image_LU, image_choice, choice
    image_LU = load_image('sprites/framework/level_up.png')
    image_choice = load_image('sprites/framework/UI.png')
    choice = 0

def exit():
    global image_LU, image_choice, choice
    del image_LU
    del image_choice
    del choice

def handle_events():
    global choice
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RETURN:
                game_framework.pop_state()
            elif event.key == SDLK_SPACE:
                game_framework.pop_state()
            elif event.key == SDLK_UP:
                if choice > 0:
                    choice -= 1
            elif event.key == SDLK_DOWN:
                if choice < 2:
                    choice += 1

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw(play_state.player)
    image_LU.clip_draw(0, 0, 560, 756, WIDTH / 2, HEIGHT / 2, 560, 756)
    image_choice.clip_composite_draw(2 + 16 * frame, 1023 - 376, 15, 13, 0, '', WIDTH/2 - 300, HEIGHT/2 + 170 - (choice * 150), 30, 26)
    image_choice.clip_composite_draw(2 + 16 * frame, 1023 - 376, 15, 13, 3.141592, 'v', WIDTH / 2 + 300, HEIGHT / 2 + 170 - (choice * 150), 30, 26)
    update_canvas()

    delay(0.02)
    # 중심 512, 512, 한칸 간격 153

def update():
    global frame
    frame = (frame + 1) % 7
    pass

def pause():
    pass

def resume():
    pass
