import os
import sys

#if os.name != "nt":
    
#    sys.path.append('../')
    
#else:
    
#    sys.path.append('..\\')

from libs.g2d import *
from libs.actor import *
from npc.Balloon import *
from npc.Face import *
from player.BomberMan import *
from background.Wall import *
from background.Brick import *
from tools.PowerUps import *
from libs.datahandler import *

global aaaa, c, b
global music
aaaa = False
c = 256


def start(w: int, h: int, wc: int, hc: int, arena: Arena, bomber: BomberMan, lol: bool):
    
    global aaaa, aa, b, music
    
    b = bomber
    
    img = "./imgs/bomberman.png"
    
    w, h = w, h
    
    wc, hc = wc, hc

    
    if lol:
        
        aa = arena
    
        Normal(w, h, aa, img, wc, hc, bomber)
        music=True

        aaaa = True
    
    tick()
 

def tick():
    
    global c, music


    clear_canvas()
    change_canvas_color(60, 123, 1)
    
    set_color((189, 190, 189))
    draw_rect((0, 0), (496, 32))
    
    if music:

        play_audio("./sounds/3 - Track 3.mp3", True)
        music = False

    
    if b.getLives() >= 0:
        
        set_color((0, 0, 0))
        draw_text(f"Time {c}      {b.getPoints()}       Left {b.getLives()}", (121, 17), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
        
        set_color((255, 255, 255))
        draw_text(f"Time {c}      {b.getPoints()}       Left {b.getLives()}", (120, 16), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
        
    else:
        
        set_color((0, 0, 0))
        draw_text(f"Time {c}      {b.getPoints()}       Left {0}", (121, 17), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
        
        set_color((255, 255, 255))
        draw_text(f"Time {c}      {b.getPoints()}       Left {0}", (120, 16), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
    
    for a in aa.actors():
        if a != None:
            #draw_image("./bomberman.png", a.pos(), (a.sprite()), a.size())
            a.draw()
        

    aa.tick(current_keys())  # Game logic
    
    c -= 1



def Normal(w: int, h: int, arena: Arena, imgsrc: str, wc: int, hc: int, bomber: BomberMan):
    
    img_src = imgsrc
    
    AW, AH = w, h-16
    
    global b
    
    saveState(b)
    
    arena.spawn(b)
    
    arena.spawn(WallPass((16, 72), img_src, 3, arena, b))
    arena.spawn(BombUp((16, 88), img_src, 0, arena, b))
    arena.spawn(BombPass((16, 104), img_src, 5, arena, b))
    arena.spawn(SpeedUp((16, 120), img_src, 2, arena, b))

    arena.spawn(Balloon(128, 168, img_src, arena, b))
    arena.spawn(Face(144, 184, img_src, arena, b))
    
    
    
    for i in range(int(AH / 16)):
        
        arena.spawn(Wall((0, (i*16+24)), img_src, b))
        arena.spawn(Wall(((AW - 16), (i*16)+24), img_src, b))
        
        
    for i in range(int(AW / 16)):    
        
        arena.spawn(Wall((i*16, 24), img_src, b))
        arena.spawn(Wall((i*16, (AH-16)+24), img_src, b))
    
    for x in range(int(AW / 16)):
        
        if x % 2 == 0:
    
            for y in range(int(AH / 16)):
                
                if y % 2 == 0:
                    
                    arena.spawn(Wall(((x*16), (y * 16)+24), img_src, b))
                
                else:
                    
                    s = choice([-1, 0, 1])
                    
                    if s == 1 and ((x*16)) != 0 and ((x*16)) != arena.size()[0]-16:# and ((x != 1 and y != 1) or ((x != 1 and y != 2) or (x != 2 and y != 1))):
                        
                        arena.spawn(Brick(((x*16), (y * 16)+24), img_src, b))
                        
        """else:
            
            for y in range(int(AH / 16)-1):
                
                if y % 2 == 0:
                    
                    s = choice([-1, 0, 1, 2])
                    
                    if (s == 1 or s == -1) and y*16 != 0 and y*16 != arena.size()[1]-8:# and ((x != 1 and y != 1) or ((x != 1 and y != 2) or (x != 2 and y != 1))):
                        
                        arena.spawn(Brick((x*16, (y * 16)+24), img_src, b))
                        
                else:
                    
                    s = choice([-1, 0, 1, 2])
                    
                    if (s == 1 or s == -1) and y*16 != 0 and y*16 != arena.size()[1]:# and ((x != 1 and y != 1) or ((x != 1 and y != 2) or (x != 2 and y != 1))):
                        
                        arena.spawn(Brick((x*16, (y * 16)+24), img_src, b))"""
            

"""if __name__ == "__main__":
    
    img = "../imgs/bomberman.png"
    
    w, h = 496, 224
    
    wc, hc = 256, 224

    global arena
    
    arena = Arena((w, h))
    
    Normal(w, h, arena, img, wc, hc)
    
    
    
    init_canvas((wc, hc), 3)
    
    change_canvas_color(60, 123, 1)
    
    main_loop(tick)"""