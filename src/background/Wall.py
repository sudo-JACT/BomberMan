from libs.actor import *
from libs.g2d import *

class Wall(Actor):
    
    def __init__(self, pos: Point, spr) -> None:
        
        self._sprite = spr
        self._w, self._h = 16, 16
        self._spritepos = (48, 48)
        self._x, self._y = pos
        
    def move(self, arena: Arena):
        
        return
    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self):
        
        return (16, 16)
    
    def draw(self):
        
        draw_image(self._sprite, (self._x, self._y), self._spritepos, (self._w, self._h))
