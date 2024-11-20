import os
import sys

import tools.Fire

if os.name != "nt":
    
    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')


from libs.g2d import *
from libs.actor import *
from player import *
import tools


class Brick(Actor):
    
    def __init__(self, pos: Point, spr, bomber) -> None:
        self._sprite = spr
        self._w, self._h = 16, 16
        self._current_sprite = (64, 48)
        self._x, self._y = pos
        
        self._isdead = False
        self._dead_clock = 0
        self._end_clock = 0
        self._co = 0
        
        self._b = bomber
        
        self._death_animations = {
            
            0: (80, 48),
            1: (96, 48),
            2: (112, 48),
            3: (128, 48),
            4: (144, 48),
            5: (160, 48),
            
        }
     
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)
    
    def move(self, arena: Arena) -> None:
        
        if self._isdead:
            
            self._dead_clock += 1
                
                
            if ((self._end_clock - self._dead_clock) % 6 == 0):
            
                self._current_sprite = self._death_animations[self._co]
                
                if self._co <= 4:
                    self._co += 1
                    
                
                
            if self._dead_clock >= self._end_clock:
                
                arena.kill(self)
                
        else:
            
            for other in arena.collisions():
                
                if isinstance(other, tools.Fire.Fire) and (other.pos()[0] == self._x and other.pos()[1] == self._y):
                        
                    self.hit(arena)
                
     
    def draw(self) -> None:
    
        draw_image(self._sprite, (self._x + self._b.getOffset(), self._y), self._current_sprite, (self._w, self._h))
        
    def hit(self, arena: Arena) -> None:
        
        self._dead_clock = arena.count()
        self._end_clock = self._dead_clock + 24
        self._isdead = True
        
        
