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
        
        self._music = True
        
        self._mmMusic = True
        
        self._select = 0
        
        self._start = False
        
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
        
        if not(self._start):
            
            if self._mmMusic:
                
                try:
                    
                    pause_audio("./sounds/3 - Track 3.mp3")
                    
                except:
                    
                    pass
                    
    
                play_audio("./sounds/1 - Track 1.mp3", True)
                self._mmMusic = False
                self._music = True
            
            print(self._start)
            
            l = self._game.current_keys()
            
            print(l)
            print(self._select)
            print(self._game.getBomber().getSpeed())
            print(self._game.getBomber().getPowerUp())
            
            if "a" in l:
                
                self._start = True
                
            elif "ArrowUp" in l:
                
                self._select -= 1
                
                if self._select < 0:
                    
                    self._select = 0
            
            elif "ArrowDown" in l:
                
                self._select += 1
                
                if self._select > 1:
                    
                    self._select = 1
            
            positions = {
                
                0: (64, 152),
                1: (128, 152),
                
            }
        
            change_canvas_color(0, 0, 0)   

            draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", (0, 0))
            
            draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[0], (64, 163), (8, 8))
            draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[1], (64, 163), (8, 8))
            
            draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[ self._select], (80, 248), (8, 8))

            set_color((99, 99, 99))
            draw_text("2024  SHIBA & JKT", (161, 189), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
            set_color((255, 255, 255))
            draw_text("2024  SHIBA & JKT", (160, 188), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
        
        else:
        
            time = (self._game.getTime() // 30)
            
            clear_canvas()
            change_canvas_color(60, 123, 1)
            
            set_color(self._50_shade_of_gray)
            draw_rect(self._origin, (496, 32))
            
            if self._music:

                pause_audio("./sounds/1 - Track 1.mp3")
                play_audio("./sounds/3 - Track 3.mp3", True)
                self._music = False
                self._mmMusic = True

            
            if self._game.getBomber().getLives() >= 0:
                
                set_color((0, 0, 0))
                draw_text(f"Time {time}      {self._game.getBomber().getPoints()}       Left {self._game.getBomber().getLives()}", (121, 17), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                
                set_color((255, 255, 255))
                draw_text(f"Time {time}      {self._game.getBomber().getPoints()}       Left {self._game.getBomber().getLives()}", (120, 16), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                
            else:
                
                set_color((0, 0, 0))
                draw_text(f"Time {time}      {self._game.getBomber().getPoints()}       Left {0}", (121, 17), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                
                set_color((255, 255, 255))
                draw_text(f"Time {time}      {self._game.getBomber().getPoints()}       Left {0}", (120, 16), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                
                self._start = False
                self.createGame()
            
            for a in self._game.actors():
                if a != None:
                
                    a.draw()
                

        self._game.tick(current_keys())  # Game logic
        
    
        


