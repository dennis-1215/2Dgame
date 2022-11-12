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
equipment_list = []

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
    global player, backgrounds, play_time, equipment_list
    play_time = 0
    player = character.Character()
    backgrounds = [back_ground.BG() for i in range(9)]
    equipment_list = [equipments.Whip(), equipments.Heal(), equipments.Hp(), equipments.Garlic(), equipments.Second_Whip()]

    for i in range(3):
        for j in range(3):
            backgrounds[i*3+j].x, backgrounds[i*3+j].y =  (-1 * WIDTH) + (j * 2 * WIDTH), (-1 * HEIGHT) + (i * 2 * HEIGHT)
    game_world.add_objects(backgrounds, 0)
    game_world.add_objects(equipment_list, 1)
    game_world.add_object(player, 2)


# finalization code
def exit():
    game_world.clear()

def update():
    schedule.run_pending()

    for game_object in game_world.all_objects():
        game_object.update(player)

    print(f'whip: {game_world.objects[1][0].time:.2f}')
    print(f's_whip: {game_world.objects[1][-1].time:.2f}')

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b, player):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw(player)

def draw():
    clear_canvas()
    draw_world()
    update_canvas()
def pause():
    pass

def resume():
    pass

def enemy_on():
    if play_time < 20:
        game_world.add_object(enemy.Enemy(), 3)
    else:
        game_world.add_object(enemy.Enemy(play_time), 3)
    game_world.add_collision_pairs(player, game_world.objects[3][len(game_world.objects[3]) - 1], 'player:enemy')
    game_world.add_collision_pairs(equipment_list[0], game_world.objects[3][len(game_world.objects[3]) - 1], 'whip:enemy')
    game_world.add_collision_pairs(equipment_list[-1], game_world.objects[3][len(game_world.objects[3]) - 1], 'whip2:enemy')
    game_world.add_collision_pairs(equipment_list[3], game_world.objects[3][len(game_world.objects[3]) - 1], 'garlic:enemy')

def play_timer():
    global play_time
    play_time += 1
    if play_time == 1800:
        schedule.cancel_job(job)
        game_framework.push_state(win_state)


def collide(a, b, player):
    left_a, bottom_a, right_a, top_a = a.get_bb(player)
    left_b, bottom_b, right_b, top_b = b.get_bb(player)
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

job = schedule.every(1).seconds.do(play_timer)
job1 = schedule.every(2).seconds.do(enemy_on)