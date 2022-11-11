from pico2d import *
import game_framework
import game_world
import level_up_state
import win_state
import enemy
import Item
import character
import back_ground
import equipments
import schedule
import time

WIDTH, HEIGHT = 1024, 1024


player = None # c로 따지믄 NULL
backgrounds = None
attack_on = 0
attack_speed = 1
play_time = 0


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)


def enter():
    global player, backgrounds, myutals, running, items, play_time, equipment_list
    play_time = 0
    player = character.Character()
    backgrounds = [back_ground.BG() for i in range(9)]
    equipment_list = [equipments.Whip(), equipments.Heal(), equipments.Hp(), equipments.Garlic()]

    for i in range(3):
        for j in range(3):
            backgrounds[i*3+j].x, backgrounds[i*3+j].y =  (-1 * WIDTH) + (j * 2 * WIDTH), (-1 * HEIGHT) + (i * 2 * HEIGHT)
    game_world.add_objects(backgrounds, 0)
    game_world.add_object(player, 1)

# finalization code
def exit():
    game_world.clear()

def update():
    global attack_speed
    attack_speed = player.atk_speed
    schedule.run_pending()

    for game_object in game_world.all_objects():
        game_object.update(player)

    if player.atk_frame == 5:
        for game_object in game_world.objects[2]:
            player.attack_rect(game_object)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw(player)

def draw():
    clear_canvas()
    draw_world()
    if attack_on == 1:
        player.attack_draw()
    else:
        player.atk_frame = 0
    update_canvas()
def pause():
    pass

def resume():
    pass

def enemy_on():
    #myutals.append(enemy.Enemy())
    game_world.add_object(enemy.Enemy(), 2)

def player_attack():
    global attack_on, job2
    attack_on = (attack_on + 1) % 10
    schedule.cancel_job(job2)
    job2 = schedule.every(attack_speed/10).seconds.do(player_attack)

def play_timer():
    global play_time
    play_time += 1
    if play_time == 1800:
        schedule.cancel_job(job)
        game_framework.push_state(win_state)

job = schedule.every(1).seconds.do(play_timer)
job1 = schedule.every(3).seconds.do(enemy_on)
job2 = schedule.every(attack_speed/10).seconds.do(player_attack)