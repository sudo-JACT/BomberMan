from libs.g2d import *
from npc import Enemy
from player import BomberMan
from gamemodes import *


def t() -> None:
    
    pass    


if __name__ == "__main__":
    
    W, H = 500, 500
    
    init_canvas((W, H))
    
    main_loop(t())