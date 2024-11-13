import sys

import npc.Balloon
import player.BomberMan
sys.path.append('../')


from libs.actor import Arena
from libs.g2d import *
from libs.actor import *
from background.Wall import *
from background.Brick import *
import player
import npc
import tools

class Fire(Actor):
    
    def __init__(self, pos: Point, sprt: str, arena: Arena) -> None:
        
        self._sprite = sprt
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._current_clock = arena.count()
        self._end_clock = self._current_clock + 32
        
        
        
        
        self._sprites = {
            
            0: (32, 96),
            1: (112, 96),
            2: (32, 112),
            3: (112, 96),
            
        }
        
        self._currentsprite = (self._sprites[0])
        
        
    def move(self, arena: Arena) -> None:
        
        self._current_clock += 1
        
        if (self._current_clock == (self._end_clock - 28)) or (self._current_clock == (self._end_clock - 4)) or (self._current_clock == self._end_clock):
            
            self._currentsprite = self._sprites[0]
        
        elif (self._current_clock == (self._end_clock - 24)) or (self._current_clock == (self._end_clock - 8)):
            
            self._currentsprite = self._sprites[1]
        
        elif (self._current_clock == (self._end_clock - 20)) or (self._current_clock == (self._end_clock - 12)):
            
            self._currentsprite = self._sprites[2]
            
        elif (self._current_clock == (self._end_clock - 16)):
            
            self._currentsprite = self._sprites[3]
        
        
        for other in arena.collisions():
        
            if isinstance(other, npc.Balloon.Balloon) or isinstance(other, Brick) or isinstance(other, player.BomberMan.BomberMan):
                    
                other.hit(arena)
                
            
        
            if self._current_clock == self._end_clock:
                
                arena.kill(self)
                    
                    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)
    
    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x, self._y), self._currentsprite, (self._w, self._h))