import pico2d
import game_framework
import title_state

WIDTH, HEIGHT = 1024, 1024

pico2d.open_canvas(WIDTH, HEIGHT)
game_framework.run(title_state)
pico2d.close_canvas()
