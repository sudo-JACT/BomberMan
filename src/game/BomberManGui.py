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

        self._ldmusic = True

        self._gomusic = True
        
        self._points = 0
                
        self._select = 0
        
        self._load_counter = 0
        
        self._start = False
        
        self._50_shade_of_gray = (189, 190, 189)
        
        self._origin = (0 ,0)
        
        self._game = BomberManGame(self._stage)
        
        self._actual_lives = self._game.getBomber().getLives()
        
        init_canvas(self._game.getCanvasSize(), scale)
        
        main_loop(self.tick)
    
    
    def createGame(self) -> None:
        
        self._game = BomberManGame(self._stage)
        
    def nextLevel(self) -> None:
        
        if self._game.GameWin:
            
            self._stage += 1
            
            self._game = BomberManGame(self._stage)
            
            
    def loadingScreen(self) -> None:
            
        change_canvas_color(0, 0, 0)  



        if not(self._game.GameOver()):


            pause_audio("./sounds/1 - Track 1.mp3")

            if self._ldmusic:

                pause_audio("./sounds/3 - Track 3.mp3")

                play_audio("./sounds/2 - Track 2.mp3" )

                self._music = True

                self._ldmusic = False

                    
                
            set_color((99, 99, 99))
            draw_text(f"STAGE {self._stage}", (129, 113), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
            set_color((255, 255, 255))
            draw_text(f"STAGE {self._stage}", (128, 112), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")

        else:

            if self._gomusic:

                pause_audio("./sounds/3 - Track 3.mp3")

                play_audio("./sounds/10 - Track 10.mp3",True )

                self._music = True

                self._gomusic = False
            
            set_color((99, 99, 99))
            draw_text("GAME OVER", (129, 113), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
            set_color((255, 255, 255))
            draw_text("GAME OVER", (129, 113), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
            
            
            
        

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
            
            
            if not(self._start):
                
                self._points = self._game.getBomber().getPoints()
        
                change_canvas_color(0, 0, 0)   

                draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", (0, 0))

                draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[0], (64, 163), (8, 8))
                draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[1], (64, 163), (8, 8))

                draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[self._select], (80, 248), (8, 8))
                
                set_color((0, 0, 0))
                draw_rect((112, 168), (72, 8))
                
                #for x in range(9):
                    
                #    draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", ((112+(8*x)), 168), (0, 248), (8, 8))
                
                x = str(self._points)
                
                if len(x) < 9:
                    
                    while len(x) < 9:
                        
                        x = "0" + x
                
                set_color((99, 99, 99))
                draw_text(x, (148, 173,), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                set_color((255, 255, 255))
                draw_text(x, (147, 172,), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")

                set_color((99, 99, 99))
                draw_text("2024  SHIBA & JKT", (161, 189), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                set_color((255, 255, 255))
                draw_text("2024  SHIBA & JKT", (160, 188), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                
            
        
        
        else:
            
            
            if self._load_counter < 85 and not(self._game.getBomber().getDead()):
                    
                self.loadingScreen()
                self._game.freeze()
                
                if self._actual_lives > self._game.getBomber().getLives():
                        
                    self._actual_lives = self._game.getBomber().getLives()
                    
                    
                    if not(self._game.GameOver()) and self._game.getBomber().getLives() >= 0:
                            
                        self._game.regenerate()
                    
                self._load_counter += 1
                
                
                
                
            else:
                
                if self._game.getBomber().getDead() and self._game.getBomber().getLives() >= 0:
                    
                    self._load_counter = 0
        
                time = (self._game.getTime() // 30)
                
                self._game.stopfreeze()
                
                clear_canvas()
                change_canvas_color(60, 123, 1)
                
                set_color(self._50_shade_of_gray)
                draw_rect(self._origin, (496, 32))
                
                if self._music:

                    pause_audio("./sounds/1 - Track 1.mp3")
                    play_audio("./sounds/3 - Track 3.mp3", True)
                    self._ldmusic = True
                    self._music = False
                    self._mmMusic = True
                    
                

                
                if self._game.getBomber().getLives() >= 0:
                    
                    set_color((0, 0, 0))
                    draw_text(f"TIME {time}     {self._game.getBomber().getPoints()}    LEFT {self._game.getBomber().getLives()}", (121, 17), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                    
                    set_color((255, 255, 255))
                    draw_text(f"TIME {time}     {self._game.getBomber().getPoints()}    LEFT {self._game.getBomber().getLives()}", (120, 16), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                    
                    if self._game.GameWin():
                        
                        self._game.regenerate()
                        
                        self._stage += 1
                        
                        self._load_counter = 0

                    
                    
                else:
                    
                    set_color((0, 0, 0))
                    draw_text(f"TIME {time}     {self._game.getBomber().getPoints()}     LEFT {0}", (121, 17), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                    
                    set_color((255, 255, 255))
                    draw_text(f"TIME {time}     {self._game.getBomber().getPoints()}     LEFT {0}", (120, 16), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
                    
                    print(self._game.getBomber().getLives())
                    print(self._actual_lives)
                    
                        
                    self._load_counter = 0
                    
                    
                        
                        
                    print(self._game.GameOver())
                        
                    #self.loadingScreen()
                    
                    if self._load_counter < 85 and self._game.GameOver() and not(self._game.getBomberAnimation()):
                        
                        print(self._game.getBomber())
                        
                        self._game.killemall()
                        
                        self.loadingScreen()
                        self._game.freeze()
                        
                        self._load_counter += 1
                        
                    if self._load_counter >= 85 and self._game.GameOver() and (self._game.getBomberAnimation()):
                        
                        self._start = False
                        self.createGame()
                    
                
                    
                
                
                for a in self._game.actors():
                    if a != None:
                    
                        a.draw()
                    
            
                

        self._game.tick(current_keys())  # Game logic
        
    
        


