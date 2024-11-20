import os
import sys

if os.name != "nt":
    
    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')


from libs.actor import *
from libs.g2d import *
import player.BomberMan

class Wall(Actor):
    
    def __init__(self, pos: Point, spr, bomber: player) -> None:
        
        self._sprite = spr
        self._w, self._h = 16, 16
        self._spritepos = (48, 48)
        self._x, self._y = pos
        self._b = bomber
        
        
    def move(self, arena: Arena) -> None:
        
        return
    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (16, 16)
    
    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x + self._b.getOffset(), self._y), self._spritepos, (self._w, self._h))
