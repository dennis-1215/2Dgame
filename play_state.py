from pico2d import *
import game_framework
import level_up_state
import enemy
import Item
import character
import schedule
import time

WIDTH, HEIGHT = 1024, 1024

class BG:
    def __init__(self):
        self.image = load_image('sprites/maps/bg_molise.png')
        self.x, self.y = 0, 0

    def draw(self, x, y):
        self.image.draw(self.x - x, self.y - y)

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
backgrounds = None
myutals = None
Items = None
running = True
attack_on = 0
attack_speed = 1

# 초기화
def enter():
    global player, backgrounds, myutals, running, items, attack_time
    player = character.Character()
    backgrounds = [BG() for i in range(9)]

    for i in range(3):
        for j in range(3):
            backgrounds[i*3+j].x, backgrounds[i*3+j].y =  (-1/2 * WIDTH) + (j * WIDTH), (-1/2 * HEIGHT) + (i * HEIGHT)
    myutals = [enemy.Enemy()]
    items = []
    running = True
    attack_time = player.atk_time

# finalization code
def exit():
    global player, backgrounds, myutals
    del player
    del backgrounds
    del myutals

def update():
    global attack_speed
    attack_speed = player.atk_speed
    player.moving()
    schedule.run_pending()
    for myutal in myutals:
        enemy.enemy_distance(player, myutal)
        enemy.enemy_move(myutal)
        enemy.enemy_crash(myutal, player, myutals, items)
    for item in items:
        Item.item_distance(player, item)
        Item.get_item(player, item, items)

def draw():
    clear_canvas()

    for background in backgrounds:
        background.draw(player.x, player.y)

    player.animation()


    for myutal in myutals:
        enemy.enemy_animation(myutal)

    for item in items:
        item.draw()

    if attack_on == 1:
        player.attack_draw()

    player.draw_status()

    update_canvas()
def pause():
    pass

def resume():
    pass

def enemy_on():
    myutals.append(enemy.Enemy())

def player_attack():
    global attack_on, job2
    attack_on = (attack_on + 1) % 10
    print(attack_on)
    print('[',attack_speed, ']')
    schedule.cancel_job(job2)
    job2 = schedule.every(attack_speed/10).seconds.do(player_attack)


job1 = schedule.every(3).seconds.do(enemy_on)
job2 = schedule.every(attack_speed/10).seconds.do(player_attack)