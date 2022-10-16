from pico2d import *
import game_framework
import enemy
import character
import schedule
import time

class BG:
    def __init__(self):
        self.image = load_image('sprites/maps/bg_molise.png')

    def draw(self):
        self.image.draw(character.WIDTH/2, character.HEIGHT/2)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                player.move = 1
                player.R_L_check = 1
            elif event.key == SDLK_LEFT:
                player.move = 1
                player.R_L_check = 2
            elif event.key == SDLK_UP:
                player.move = 1
                player.D_check = 0
                player.U_check = 1
            elif event.key == SDLK_DOWN:
                player.move = 1
                player.U_check = 0
                player.D_check = 1
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.move = 0
                player.R_L_check = 3
            elif event.key == SDLK_LEFT:
                player.move = 0
                player.R_L_check = 4
            elif event.key == SDLK_UP:
                player.move = 0
                player.U_check = 0
            elif event.key == SDLK_DOWN:
                player.move = 0
                player.D_check = 0



player = None # c로 따지믄 NULL
background = None
myutals = None
running = True
enemy_count = 0

# 초기화
def enter():
    global player, background, myutals, running
    player = character.Character()
    background = BG()
    myutals = [enemy.Enemy() for i in range(50)]
    running = True

# finalization code
def exit():
    global player, background, myutals
    del player
    del background
    del myutals

def update():
    player.moving()
    schedule.run_pending()
    for myutal in myutals:
        enemy.enemy_move(myutal, player)
        enemy.enemy_crash(myutal, player)

def draw():
    clear_canvas()
    background.draw()
    player.animation()
    for myutal in myutals:
        enemy.enemy_animation(myutal, player)
    update_canvas()

def enemy_on():
    global enemy_count
    myutals[enemy_count].on = 1
    enemy_count += 1

job1 = schedule.every(3).seconds.do(enemy_on)

if enemy_count == 50:
    schedule.cancel_job(job1)