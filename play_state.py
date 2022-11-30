from pico2d import *
import game_framework
import game_world
import title_state
import win_state
import enemy
import character
import back_ground
import equipments
import pause_state

WIDTH, HEIGHT = 1024, 1024


player = None # c로 따지믄 NULL
backgrounds = None
play_time = 0
equipment_list = []

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        else:
            player.handle_event(event)


def enter():
    global player, backgrounds, play_time, equipment_list
    play_time = 0

    player = character.Character()
    player.handle_event(title_state.event_key)
    backgrounds = back_ground.BG()
    whip, heal, hp, garlic, shoes, damage_up, second_whip = equipments.Whip(), equipments.Heal(), equipments.Hp(), equipments.Garlic(), equipments.Shoes(), equipments.Damage_up(), equipments.Second_Whip()
    equipment_list = [whip, heal, hp, garlic, shoes, damage_up, second_whip]

    game_world.add_object(backgrounds, 0)
    game_world.add_objects(equipment_list, 1)
    game_world.add_object(player, 2)

    game_world.add_collision_pairs(player, None, 'player:enemy')
    game_world.add_collision_pairs(whip, None, 'whip:enemy')
    game_world.add_collision_pairs(second_whip, None, 'whip2:enemy')
    game_world.add_collision_pairs(garlic, None, 'garlic:enemy')


# finalization code
def exit():
    game_world.clear()

def update():
    global play_time
    play_time += game_framework.frame_time

    for game_object in game_world.all_objects():
        game_object.update(player)


    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    if play_time < 300 and play_time % 3.0 <= 0.02:
        spawn_bat()

    if play_time > 30 and play_time % 3.0 <= 0.01:
        spawn_myutal()

    if play_time >= 600.0:
        game_framework.push_state(win_state)

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

def spawn_myutal():
    new_enemy = enemy.Enemy()
    game_world.add_object(new_enemy, 3)
    game_world.add_collision_pairs(None, new_enemy, 'player:enemy')
    game_world.add_collision_pairs(None, new_enemy, 'whip:enemy')
    game_world.add_collision_pairs(None, new_enemy, 'whip2:enemy')
    game_world.add_collision_pairs(None, new_enemy, 'garlic:enemy')

def spawn_bat():
    new_enemy = enemy.Bat()
    game_world.add_object(new_enemy, 3)
    game_world.add_collision_pairs(None, new_enemy, 'player:enemy')
    game_world.add_collision_pairs(None, new_enemy, 'whip:enemy')
    game_world.add_collision_pairs(None, new_enemy, 'whip2:enemy')
    game_world.add_collision_pairs(None, new_enemy, 'garlic:enemy')

def collide(a, b):
    if type(a) == equipments.Whip or type(a) == equipments.Second_Whip:
        # dir 따라서 방향 조정
        if player.face_dir == 1:
            left_a, bottom_a, right_a, top_a = a.get_bb_right()
            left_b, bottom_b, right_b, top_b = b.get_bb()
            if left_a > right_b: return False
            if right_a < left_b: return False
            if top_a < bottom_b: return False
            if bottom_a > top_b: return False
            return True

        else:
            left_a, bottom_a, right_a, top_a = a.get_bb_left()
            left_b, bottom_b, right_b, top_b = b.get_bb()
            if left_a > right_b: return False
            if right_a < left_b: return False
            if top_a < bottom_b: return False
            if bottom_a > top_b: return False
            return True

    else:
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True