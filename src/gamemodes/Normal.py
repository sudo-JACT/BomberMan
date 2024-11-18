import sys
sys.path.append('../')

from libs.g2d import *
from libs.actor import *
from npc.Balloon import *
from player.BomberMan import *
from background.Wall import *
from background.Brick import *


def tick():
    
    clear_canvas()
    change_canvas_color(60, 123, 1)
    
    set_color((189, 190, 189))
    draw_rect((0, 0), (256, 32))
    
    for a in arena.actors():
        if a != None:
            #draw_image("./bomberman.png", a.pos(), (a.sprite()), a.size())
            a.draw()
        else:
            pass  # g2d.draw_rect(a.pos(), a.size())

    arena.tick(current_keys())  # Game logic


def Normal(w: int, h: int, arena: Arena, imgsrc: str, wc: int, hc: int):
    
    img_src = imgsrc
    
    AW, AH = w, h-16
    
    b = BomberMan((16, 40), img_src, ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "b"], (wc, hc), arena)
    
    arena.spawn(b)

    arena.spawn(Balloon(136, 136, img_src, arena, b))
    
    for i in range(int(AH / 16)):
        
        arena.spawn(Wall((0, (i*16+24)), img_src, b))
        #arena.spawn(Wall(((AW - 16), (i*16)+24), img_src))
        
        
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
                    
                    if s == 1 and ((x*16)) != 0 and ((x*16)) != arena.size()[0]-16 and (x != 16 and y != 40) and (x != 16 and y != 56) and (x != 32 and y != 40):
                        
                        arena.spawn(Brick(((x*16), (y * 16)+24), img_src, b))
                        
        else:
            
            for y in range(int(AH / 16)-1):
                
                if y % 2 == 0:
                    
                    s = choice([-1, 0, 1, 2])
                    
                    if (s == 1 or s == -1) and y*16 != 0 and y*16 != arena.size()[1]-8:
                        
                        arena.spawn(Brick((x*16, (y * 16)+24), img_src, b))
                        
                else:
                    
                    s = choice([-1, 0, 1, 2])
                    
                    if (s == 1 or s == -1) and y*16 != 0 and y*16 != arena.size()[1]:
                        
                        arena.spawn(Brick((x*16, (y * 16)+24), img_src, b))
                

if __name__ == "__main__":
    
    img = "../imgs/bomberman.png"
    
    w, h = 256, 224
    
    wc, hc = 112, 112
    
    global arena
    
    arena = Arena((w, h))
    
    Normal(w, h, arena, img, wc, hc)
    
    
    
    init_canvas(arena.size(), 3)
    
    change_canvas_color(60, 123, 1)
    
    main_loop(tick)