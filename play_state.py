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
ui_image = None
time_font, ui_font = None, None
play_time = 0
spawn_bat_time = 0
spawn_myutal_time = 0
equipment_list = []
get_gold = 0


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
    global player, backgrounds, play_time, equipment_list, time_font, ui_font, ui_image
    play_time = 0

    time_font = load_font('KO.ttf', 30)
    ui_font = load_font('KO.ttf', 10)
    ui_image = load_image('sprites/framework/UI.png')

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
    time_update()
    for game_object in game_world.all_objects():
        game_object.update(player)

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    monster_spawn()
    get_money()

    if play_time >= 600.0:
        game_framework.push_state(win_state)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw(player)
    draw_ui()

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

def monster_spawn():
    global spawn_bat_time, spawn_myutal_time

    if play_time < 300:
        if spawn_bat_time >= 1.5:
            spawn_bat()
            spawn_bat_time = 0

    if play_time > 30 and play_time < 600:
        if spawn_myutal_time >= 3.0:
            spawn_myutal()
            spawn_myutal_time = 0

def draw_ui():
    # 화면 중앙 위에 시간 표시
    time_font.draw(backgrounds.canvas_width / 2, backgrounds.canvas_height - 50, f'{int(play_time // 60)}:{int(play_time % 60)}', (255, 255, 255))

    # 화면 중앙 오른쪽에 킬 수 + 먹은 돈 표시
    ui_image.clip_draw(288, 1024 - 371, 8, 7, backgrounds.canvas_width - 200, backgrounds.canvas_height - 30, 16, 14)
    ui_font.draw(backgrounds.canvas_width - 170, backgrounds.canvas_height - 30, f'{player.kill_count}', (255,255,255))

    ui_image.clip_draw(241, 1024 - 373, 10, 10, backgrounds.canvas_width - 100, backgrounds.canvas_height - 30, 15, 15)
    ui_font.draw(backgrounds.canvas_width - 70, backgrounds.canvas_height - 30, f'{player.gold}', (255, 255, 255))


    # 플레이어의 체력, 경험치 표시
    player.image.clip_draw(0, 1077, 2, 1, WIDTH / 2 - 17, HEIGHT / 2 - 20, 80, 4)  # 최대 체력바
    player.image.clip_draw(2, 448, 2, 1, WIDTH / 2 - 17, HEIGHT / 2 - 20, 80 * player.hp / player.max_hp, 4)  # 현재 체력바
    player.image.clip_draw(0, 1077, 2, 1, 0, HEIGHT - 5, WIDTH * 2, 10)  # 최대 경험치 바
    player.image.clip_draw(0, 1, 2, 1, 0, HEIGHT - 5, WIDTH * 2 * player.exp / player.max_exp, 10)  # 현재 경험치 바

    # 경험치 바 위에 레벨 표시
    ui_font.draw(backgrounds.canvas_width - 25, backgrounds.canvas_height - 5, f'LV.{player.level}', (255, 255, 255))

def time_update():
    global play_time, spawn_bat_time, spawn_myutal_time

    play_time += game_framework.frame_time
    spawn_bat_time += game_framework.frame_time
    spawn_myutal_time += game_framework.frame_time

def get_money():
    global play_time, get_gold

    if (play_time + 1) // 1 % 10 == 0:
        if get_gold == 0:
            player.gold += 1
            get_gold = 1
        return
    else:
        get_gold = 0
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