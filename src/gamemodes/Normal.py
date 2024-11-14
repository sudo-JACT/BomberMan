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
    
    for a in arena.actors():
        if a != None:
            #draw_image("./bomberman.png", a.pos(), (a.sprite()), a.size())
            a.draw()
        else:
            pass  # g2d.draw_rect(a.pos(), a.size())

    arena.tick(current_keys())  # Game logic


def Normal(w: int, h: int, arena: Arena, imgsrc: str):
    
    img_src = imgsrc
    
    AW, AH = w, h
    
    arena.spawn(BomberMan((240, 240), img_src, ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "b"], arena))

    arena.spawn(Balloon(16, 16, img_src, arena))
    
    for i in range(int(AW / 16)):
        
        arena.spawn(Wall((0, i*16), img_src))
        arena.spawn(Wall(((AW - 16), i*16), img_src))
        
        arena.spawn(Wall((i*16, 0), img_src))
        arena.spawn(Wall((i*16, (AW-16)), img_src))
    
    for x in range(int(AW / 16)):
        
        if x % 2 == 0:
    
            for y in range(int(AW / 16)):
                
                if y % 2 == 0:
                    
                    arena.spawn(Wall((x*16, (y * 16)), img_src))
                
                else:
                    
                    s = choice([-1, 0, 1])
                    
                    if s == 1 and x*16 != 0 and x*16 != arena.size()[0]-16:
                        
                        arena.spawn(Brick((x*16, (y * 16)), img_src))
                        
        else:
            
            for y in range(int(AW / 16)):
                
                if y % 2 == 0:
                    
                    s = choice([-1, 0, 1, 2])
                    
                    if (s == 1 or s == -1) and y*16 != 0 and y*16 != arena.size()[1]-16:
                        
                        arena.spawn(Brick((x*16, (y * 16)), img_src))
                        
                else:
                    
                    s = choice([-1, 0, 1, 2])
                    
                    if (s == 1 or s == -1) and y*16 != 0 and y*16 != arena.size()[1]-16:
                        
                        arena.spawn(Brick((x*16, (y * 16)), img_src))
                

if __name__ == "__main__":
    
    img = "../imgs/bomberman.png"
    
    w, h = 496, 496
    
    global arena
    
    arena = Arena((w, h))
    
    Normal(w, h, arena, img)
    
    
    
    init_canvas(arena.size(),2)
    
    change_canvas_color(60, 123, 1)
    
    main_loop(tick)