import sys
sys.path.append('../')


from libs.g2d import *
from libs.actor import *
from tools.Fire import *
from player.BomberMan import *
from npc.Balloon import *
from background.Wall import *
from background.Brick import *

class Bomb(Actor):
    
    
    def __init__(self, pos: Point, spr, arena: Arena) -> None:
        
        self._sprite = spr
        self._w, self._h = 16, 16
        self._spritepos = (0, 48)
        self._x, self._y = pos
        self._current_clock = arena.count()
        self._end_clock = self._current_clock + 100
        
    def move(self, arena: Arena) -> None:
        
        self._current_clock += 1
        
        if self._current_clock == self._end_clock:
            
            arena.kill(self)
            
            arena.spawn(Fire((self._x, self._y), self._sprite))
        
        return
    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)
    
    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x, self._y), self._spritepos, (self._w, self._h))