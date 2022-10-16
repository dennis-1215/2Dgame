from pico2d import *
from character import *
import enemy



open_canvas(WIDTH, HEIGHT)
background = load_image('sprites/maps/bg_molise.png')
enemys = load_image('sprites/characters/enemies.png')

character = Character()
myutals = [enemy.Enemy() for i in range(50)]


while character.running:
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    character.input_key()
    for myutal in myutals:
        enemy.enemy_move(myutal, character)
    update_canvas()

close_canvas()
