from libs.g2d import *
"""from npc. import *
from player.BomberMan import BomberMan
from gamemodes import *"""
from libs.actor import *
from gamemodes.Normal import start

global n, w, h, wc, hc, select
n = False
select = 0



def t() -> None:
    
    global n, select
    
    print(n)
    
    l = arena.current_keys()
    
    print(l)
    print(select)
    
    if "a" in l:
        
        n = True
        
    elif "ArrowUp" in l:
        
        select -= 1
        
        if select < 0:
            
            select = 0
    
    elif "ArrowDown" in l:
        
        select += 1
        
        if select > 3:
            
            select = 3
        
        
    
    if n:
        
        games = {
    
            0: start(w, h, wc, hc, arena),
            #1: continue(),
            #2: battle(),
            #3: credits(),
    
        }
        
        games[0]
    
    else:
    
        change_canvas_color(0, 0, 0)   

        set_color((245, 190, 49))
        draw_rect((16, 16), (224, 120)) 

        set_color((168, 0, 16))   
        draw_rect((17, 17), (222, 118)) 

        set_color((240, 188, 60))
        draw_text("LOL", (56, 34), 25, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
        
        draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", (112, 112 + (16*(select))), (80, 264), (7, 7))
        
    arena.tick(current_keys())

    


if __name__ == "__main__":
    
    img = "./imgs/bomberman.png"
    
    w, h = 496, 224
    
    wc, hc = 256, 224
    
    global arena
    
    arena = Arena((w, h))
    
    init_canvas((wc, hc), 3)
    
    main_loop(t)