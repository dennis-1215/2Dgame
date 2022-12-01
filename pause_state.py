from pico2d import *
import game_framework
import game_world
import play_state
import result_state

WIDTH, HEIGHT = 1024, 1024

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

image, image_choice, font = None, None, None
choice = 1
frame = 0

def enter():
    global image, image_choice, font, choice
    choice = 1
    image = load_image('sprites/framework/pause.png')
    image_choice = load_image('sprites/framework/UI.png')
    font = load_font('font/KO.ttf', 20)
def exit():
    global image, image_choice, font
    del image, image_choice, font

def handle_events():
    global choice
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN or event.key == SDLK_SPACE:
            if choice == 0:
                game_framework.pop_state()
            elif choice == 1:
                play_state.backgrounds.bgm.stop()
                game_framework.push_state(result_state)
            pass
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_UP or event.key == SDLK_LEFT):
            if choice > 0:
                choice -= 1
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_DOWN or event.key == SDLK_RIGHT):
            if choice < 1:
                choice += 1
        play_state.player.handle_event(event)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw(play_state.player)

    # 회색 반투명
    image.clip_draw(0, 0, WIDTH, HEIGHT, WIDTH / 2, HEIGHT / 2)


    # 선택지 박스 그리기
    image_choice.clip_draw(454, 1024 - 395, 47, 30, WIDTH / 2 - 100, 50, 100, 60)
    font.draw(WIDTH / 2 - 115, 50, '뒤로', (255, 255, 255))
    image_choice.clip_draw(454, 1024 - 395, 47, 30, WIDTH / 2 + 100, 50, 100, 60)
    font.draw(WIDTH / 2 + 65, 50, '그만하기', (255, 255, 255))

    # 화살표 그리기
    if choice == 0:
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 0, '', WIDTH / 2 - 170, 50, 30, 26)
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 3.141592, 'v', WIDTH / 2 - 30, 50, 30, 26)
    elif choice == 1:
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 0, '', WIDTH / 2 + 30, 50, 30, 26)
        image_choice.clip_composite_draw(2 + 16 * int(frame), 1023 - 376, 15, 13, 3.141592, 'v', WIDTH / 2 + 170, 50, 30, 26)

    update_canvas()

def update():
    global frame
    frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7

def pause():
    pass

def resume():
    pass
