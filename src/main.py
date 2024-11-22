from libs.g2d import *
"""from npc. import *
from player.BomberMan import BomberMan
from gamemodes import *"""
from libs.actor import *
from gamemodes.Normal import start
from player.BomberMan import BomberMan

global n, w, h, wc, hc, select, c
n = False
select = 0
c = 0

def t() -> None:
    
    global n, select, c
    
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
        
        if select > 1:
            
            select = 1
        
        
    
    if n:
        
        games = {
    
            0: start(w, h, wc, hc, arena),
            #1: continue(),
    
        }
        
        if c < 256 and n:
        
            games[0]
            
            c += 1
            
        else:
            
            n = False
            c = 256
    
    else:
        
        positions = {
            
            0: (64, 152),
            1: (128, 152),
            
        }
    
        change_canvas_color(0, 0, 0)   

        draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", (0, 0))
        
        draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[0], (64, 163), (8, 8))
        draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[1], (64, 163), (8, 8))
        
        draw_image("./imgs/NES_-_Bomberman_-_Title_Screen__Text.png", positions[select], (80, 248), (8, 8))

        set_color((99, 99, 99))
        draw_text("2024  SHIBA & JKT", (161, 189), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
        set_color((255, 255, 255))
        draw_text("2024  SHIBA & JKT", (160, 188), 8, "./fonts/nintendo-nes-font/nintendo-nes-font.ttf")
    
        
    arena.tick(current_keys())

    


if __name__ == "__main__":
    
    img = "./imgs/bomberman.png"
    
    w, h = 496, 224
    
    wc, hc = 256, 224
    
    global arena, b
    
    b = BomberMan((16, 40), img_src, ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "b"], (wc, hc), arena, 3)  # to do passare bomberman a normal per avere accesso alle vite in main
    
    arena = Arena((w, h))
    
    init_canvas((wc, hc), 3)
    
    main_loop(t)