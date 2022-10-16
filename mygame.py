# fill here
import pico2d
import game_framework
import play_state

WIDTH, HEIGHT = 1024, 1024

pico2d.open_canvas(WIDTH, HEIGHT)
game_framework.run(play_state)
pico2d.close_canvas()
