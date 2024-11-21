from libs.g2d import *
"""from npc. import *
from player.BomberMan import BomberMan
from gamemodes import *"""
from libs.actor import *
from gamemodes.Normal import lol

global n, w, h, wc, hc
n = False

def t(keys: list[str]) -> None:
    
    global n
    
    print(n)
    
    l = keys
    
    print(l)
    
    if "b" in l:
        
        n = True
    
    if n:
        
        lol(w, h, wc, hc, arena)
    
    change_canvas_color(0, 0, 0)   
    
    set_color((245, 190, 49))
    draw_rect((16, 16), (224, 120)) 
    
    set_color((168, 0, 16))   
    draw_rect((17, 17), (222, 118)) 
    
    set_color((240, 188, 60))
    draw_text("LOL", (56, 34), 25, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")

    


if __name__ == "__main__":
    
    img = "./imgs/bomberman.png"
    
    w, h = 496, 224
    
    wc, hc = 256, 224
    
    global arena
    
    arena = Arena((w, h))
    
    init_canvas((wc, hc), 3)
    
    main_loop(t(arena.current_keys()))