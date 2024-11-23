import os, sys
    
if os.name != "nt":

    sys.path.append('../')

else:

    sys.path.append('..\\')

from game.BomberManGame import *
from libs.g2d import *

class BomberManGui():
    
    def __init__(self, scale: int=3) -> None:
        
        self._stage = 1
        
        self._50_shade_of_gray = (189, 190, 189)
        
        self._origin = (0 ,0)
        
        self._game = BomberManGame(self._stage)
        
        init_canvas(self._game.getCanvasSize(), scale)
        
        main_loop(self.tick)
    
    
    def createGame(self) -> None:
        
        self._game = BomberManGame(self._stage)
        
    def nextLevel(self) -> None:
        
        if self._game.GameWin:
            
            self._stage += 1
            
            self._game = BomberManGame(self._stage)
    

    def tick(self):
        
        time = self._game.time() // 30
        global c, music
        
        clear_canvas()
        change_canvas_color(60, 123, 1)
        
        set_color(self._50_shade_of_gray)
        draw_rect(self._origin, (496, 32))
        
        if music:

            play_audio("./sounds/3 - Track 3.mp3", True)
            music = False

        
        if self._b.getLives() >= 0:
            
            set_color((0, 0, 0))
            draw_text(f"Time {time}      {self._game.getBomber().getPoints()}       Left {self._game.getBomber().getLives()}", (121, 17), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
            
            set_color((255, 255, 255))
            draw_text(f"Time {time}      {self._game.getBomber().getPoints()}       Left {self._game.getBomber().getLives()}", (120, 16), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
            
        else:
            
            set_color((0, 0, 0))
            draw_text(f"Time {time}      {self._game.getBomber().getPoints()}       Left {0}", (121, 17), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
            
            set_color((255, 255, 255))
            draw_text(f"Time {time}      {self._game.getBomber().getPoints()}       Left {0}", (120, 16), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
        
        for a in self._game.actors():
            if a != None:
                #draw_image("./bomberman.png", a.pos(), (a.sprite()), a.size())
                a.draw()
            

        self._game.tick(current_keys())  # Game logic
        
    
        


