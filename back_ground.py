from pico2d import *
import play_state

WIDTH, HEIGHT = 1024, 1024
class BG:
    image = None
    def __init__(self):
        if BG.image == None:
            self.image = load_image('sprites/maps/bg_molise.png')
            self.font = load_font('KO.ttf', 30)

        self.x, self.y = 0, 0

    def update(self, player):
        pass

    def handle_event(self):
        pass
    def draw(self, player):
        self.image.clip_draw(0, 0, WIDTH, HEIGHT, self.x - player.x, self.y - player.y, WIDTH*2 , HEIGHT*2)
        self.font.draw(WIDTH/2, HEIGHT - 50, f'{play_state.play_time // 60}:{play_state.play_time%60}', (255,255,255))
