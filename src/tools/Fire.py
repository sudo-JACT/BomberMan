import sys
sys.path.append('../')


from libs.actor import Arena
from libs.g2d import *
from libs.actor import *
from background.Wall import *
from background.Brick import *
from player.BomberMan import *
from npc.Balloon import *
from tools.Bomb import *

class Fire(Actor):
    
    def __init__(self, pos: Point, sprt: str) -> None:
        
        self._sprite = sprt
        self._x, self._y = pos
        self._w, self._h = 16, 16
        
        self._current_sprite = (32, 95)
        
        
        self._first_sprits = {
            
            "core": (32, 95),
            
        }
        
        
    def move(self, arena: Arena) -> None:
        
        
        for other in arena.collisions():
        
            if isinstance(other, Balloon) or isinstance(other, Brick) or isinstance(other, BomberMan):
                    
                other.hit(arena)
                    
                    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)
    
    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x, self._y), self._current_sprite, (self._w, self._h))