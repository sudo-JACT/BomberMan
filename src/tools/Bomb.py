import os
import sys

if os.name != "nt":
    
    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')

import player 
from libs.g2d import *
from libs.actor import *
import player
from npc.Balloon import *
from background.Wall import *
from background.Brick import *
import tools

class Bomb(Actor):
    
    
    def __init__(self, pos: Point, spr: str, arena: Arena, bomber: player) -> None:
        
        self._sprite = spr
        self._w, self._h = 16, 16
        
        self._x, self._y = pos
        self._current_clock = arena.count()
        self._end_clock = self._current_clock + 100
        
        self._b = bomber
        
        self._sprites = {
            
            0: (0, 48),
            1: (16, 48),
            2: (32, 48),
            
        }
        
        self._currentsprite = self._sprites[1]
        
    def move(self, arena: Arena) -> None:
        
        self._current_clock += 1
        
        if (self._current_clock == (self._end_clock - 90)) or (self._current_clock == (self._end_clock - 50)) or (self._current_clock == (self._end_clock - 10)):
            
            self._currentsprite = self._sprites[1]
        
        elif (self._current_clock == (self._end_clock - 80)) or (self._current_clock == (self._end_clock - 60)) or (self._current_clock == self._end_clock ):
            
            self._currentsprite = self._sprites[0]
        
        elif (self._current_clock == (self._end_clock - 70)) or (self._current_clock == (self._end_clock - 30)):
            
            self._currentsprite = self._sprites[2]
        
        
        
        if self._current_clock == self._end_clock:
            
            self._b.detonated()
            
            arena.kill(self)
            
            arena.spawn(tools.Fire.Fire((self._x, self._y), self._sprite, arena, 0, self._b))
        
        return
    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)
    
    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x + self._b.getOffset(), self._y), self._currentsprite, (self._w, self._h))
        
    def get_current_clock(self) -> int:
        
        return self._current_clock
    
    def get_end_clock(self) -> int:
        
        return self._end_clock
    