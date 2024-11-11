import sys
sys.path.append('../')


from libs.g2d import *
from libs.actor import *

class Bomb(Actor):
    
    
    def __init__(self, pos: Point, spr) -> None:
        
        self._sprite = spr
        self._w, self._h = 16, 16
        self._spritepos = (0, 48)
        self._x, self._y = pos
        self._clock = 0
        
    def move(self, arena: Arena) -> None:
        
        self._clock += 1
        
        return
    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)
    
    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x, self._y), self._spritepos, (self._w, self._h))