import os
import sys

if os.name != "nt":
    
    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')

from libs.actor import Arena
from libs.g2d import *
from libs.actor import *
import background
import tools
import npc
import player


class Fire(Actor):
    
    def __init__(self, pos: Point, sprt: str, arena: Arena, t: int, bomber: player) -> None:
        
        self._sprite = sprt
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._current_clock = arena.count()
        self._end_clock = self._current_clock + 32
        
        self._b = bomber
        
        self._ty = t
        
        self._ls = []
        
        
        self._sprites_0_0 = {
            
            0: (32, 96),
            1: (112, 96),
            2: (176, 112),
            3: (112, 176),
            
        }
        
        
        self._sprites_x_1 = {
            
            0: (48, 96),
            1: (128, 96),
            2: (192, 112),
            3: (128, 176),
            
        }
        
        self._sprites_x_2 = {
            
            0: (64, 96),
            1: (144, 96),
            2: (208, 112),
            3: (144, 176),
            
        }
        
        self._sprites_y_1 = {
            
            0: (32,112),
            1: (112, 112),
            2: (176, 128),
            3: (112, 192),
            
        }
        
        self._sprites_y_2 = {
            
            0: (32,128),
            1: (112, 128),
            2: (176, 144),
            3: (112, 208),
            
        }
        
        self._sprites_mx_1 = {
            
            0: (16, 96),
            1: (96, 96),
            2: (160, 112),
            3: (96, 176),
            
        }
        
        self._sprites_mx_2 = {
            
            0: (0, 96),
            1: (80, 96),
            2: (144, 112),
            3: (80, 176),
            
            
        }
        
        self._sprites_my_1 = {
            
            0: (32, 80),
            1: (112, 80),
            2: (176, 96),
            3: (112, 160),
        }
        
        self._sprites_my_2 = {
            
            0: (32, 64),
            1: (112, 64),
            2: (176, 80),
            3: (112, 144),
            
        }
        
        if self._ty == 0:
            
            up = down = left = right = True
            
            for other in arena.collisions():
                
                if isinstance(other, background.Wall.Wall) and other.pos()[0] == self._x and other.pos()[1] == (self._y-16):
                    
                    up = False
                    
                elif isinstance(other, background.Wall.Wall) and other.pos()[0] == self._x and other.pos()[1] == (self._y+16):
                    
                    down = False
                    
                elif isinstance(other, background.Wall.Wall) and other.pos()[0] == (self._x-16) and other.pos()[1] == self._y:
                    
                    left = False
                    
                elif isinstance(other, background.Wall.Wall) and other.pos()[0] == (self._x+16) and other.pos()[1] == self._y:
                    
                    right = False
                    
            if up:
                
                arena.spawn(Fire((pos[0], pos[1]-16), sprt, arena, 1, self._b))
                
            if down:
                
                arena.spawn(Fire((pos[0], pos[1]+16), sprt, arena, 2, self._b))
            
            if left:
                
                arena.spawn(Fire((pos[0]-16, pos[1]), sprt, arena, 3, self._b))
            
            if right:
                
                arena.spawn(Fire((pos[0]+16, pos[1]), sprt, arena, 4, self._b))
            
            
            
            for x in self._sprites_0_0:
                
                self._ls.append(self._sprites_0_0[x])
        
            self._currentsprite = self._ls[0]
            
        elif self._ty == 1:
            
            for x in self._sprites_my_2:
                
                self._ls.append(self._sprites_my_2[x])
        
            self._currentsprite = self._ls[0]
            
        elif self._ty == 2:
            
            for x in self._sprites_y_2:
                
                self._ls.append(self._sprites_y_2[x])
        
            self._currentsprite = self._ls[0]
            
        elif self._ty == 3:
            
            for x in self._sprites_mx_2:
                
                self._ls.append(self._sprites_mx_2[x])
        
            self._currentsprite = self._ls[0]
            
        elif self._ty == 4:
            
            for x in self._sprites_x_2:
                
                self._ls.append(self._sprites_x_2[x])
        
            self._currentsprite = self._ls[0]
        
        
    def move(self, arena: Arena) -> None:
        
        for other in arena.collisions():
                
            if isinstance(other, background.Brick.Brick) and (other.pos()[0] == self._x and other.pos()[1] == self._y):
                    
                other.hit(arena)
                
        
        self._current_clock += 1 
        
           
        
        if (self._current_clock == (self._end_clock - 28)) or (self._current_clock == (self._end_clock - 4)) or (self._current_clock == self._end_clock):
                
            self._currentsprite = self._ls[0]
            
        elif (self._current_clock == (self._end_clock - 24)) or (self._current_clock == (self._end_clock - 8)):
                
            self._currentsprite = self._ls[1]
            
        elif (self._current_clock == (self._end_clock - 20)) or (self._current_clock == (self._end_clock - 12)):
                
            self._currentsprite = self._ls[2]
                
        elif (self._current_clock == (self._end_clock - 16)):
                
            self._currentsprite = self._ls[3]
            
        
        
        if self._current_clock == self._end_clock:
                
            arena.kill(self)
                    
                    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)
    
    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x + self._b.getOffset(), self._y), self._currentsprite, (self._w, self._h))