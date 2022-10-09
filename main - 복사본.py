from pico2d import *

WIDTH, HEIGHT = 1024, 1024

def handle_events():
    global  running
    global x, y

    global move
    global U_D_check
    global U_check
    global D_check
    global L_check
    global R_check
    global L_R_check
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                move = 1
                R_check = 1
            if event.key == SDLK_LEFT:
                move = 1
                L_check = 1
            if event.key == SDLK_UP:
                move = 1
                U_check = 1
            if event.key == SDLK_DOWN:
                move = 1
                D_check = 1
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                move = 0
                R_check = 3
            if event.key == SDLK_LEFT:
                move = 0
                L_check = 3
            if event.key == SDLK_UP:
                move = 0
                U_check = 0
            if event.key == SDLK_DOWN:
                move = 0
                D_check = 0
            handle_events()
                


open_canvas(WIDTH, HEIGHT)
background = load_image('sprites/maps/bg_molise.png')
characters = load_image('sprites/characters/characters.png')
enemies = load_image('sprites/characters/enemies.png')



running = True
x, y = WIDTH // 2, HEIGHT // 2
frame = 1
hide_cursor()
L_check = 3
U_check = 0
R_check = 3
D_check = 0
move = 0

while running:
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    if R_check == 1 and move != 0:
        characters.clip_draw(72 + frame * 35, 171, 35, 34, x, y)
    elif L_check == 1 and move != 0:
        characters.clip_draw(216 + frame * 35, 171, 35, 34, x, y)
    elif R_check % 2 == 1 and move != 0:
        characters.clip_draw(72 + frame * 35, 171, 35, 34, x, y)
    elif L_check % 2 == 1 and move != 0:
        characters.clip_draw(216 + frame * 35, 171, 35, 34, x, y)
    elif R_check == 3 and move == 0:
        characters.clip_draw(36 + frame % 2 * 35, 171, 35, 34, x, y)
    elif L_check == 3 and move == 0:
        characters.clip_draw(324 + frame % 2 * 35, 171, 35, 34, x, y)

    chara.draw()
    update_canvas()

    frame = (frame + 1) % 4
    if R_check == 1:
        if x < WIDTH:
            move = 1
            x += 2
    if L_check == 1:
        if x > 0:
            x -= 2
            move = 1
    if U_check == 1:
        if y < HEIGHT:
            y += 2
            move = 1
    if D_check == 1:
        if y > 0:
            y -= 2
            move = 1

    delay(0.01)
    handle_events()

close_canvas()
