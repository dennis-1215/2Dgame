from pico2d import *
from character import *
import enemy

WIDTH, HEIGHT = 1024, 1024

open_canvas(WIDTH, HEIGHT)
background = load_image('sprites/maps/bg_molise.png')
enemys = load_image('sprites/characters/enemies.png')

character = Character()
myutal = enemy.Enemy()


while character.running:
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2)
    character.input_key()
    myutal.moving(character)
    update_canvas()

close_canvas()
