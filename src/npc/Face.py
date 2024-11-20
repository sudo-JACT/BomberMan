import os
import sys

if os.name != "nt":
    
    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')

from libs.g2d import *
from libs.actor import *
from background.Wall import *
from background.Brick import *
from random import choice
from tools.Bomb import *
import player

class Face(Actor):
    
    def __init__(self, x0: int, y0: int, sprite_src: str, arena: Arena, bomber: player.BomberMan.BomberMan) -> None:
        self._x = x0 
        self._y = y0
        self._speed = 2
        self._dx = self._dy = 0
        self._w, self._h = 16, 16
        self._sprite = sprite_src
        self._current_sprite = (48, 240)
        d = choice([1, 2, 3, 4])
        self._isdead = False
        
        self._dead_clock = 0
        self._end_clock = 0
        self._co = 0
        
        self._points = 100
        
        self._left = self._right = 0
        
        self._directions = {
    
            "up" : 1,
            "down": 2,
            "right": 3,
            "left": 4,
        
        }


        
        self._left_animations = {
            
            0: (48, 288),
            1: (64, 288),
            2: (80, 288),
            
        }
        
        self._right_animations = {
            
            0: (0, 288),
            1: (16, 288),
            2: (32, 288),
            
        }
        
        self._death_animations = {
            
            0: (96, 288),
            1: (112, 240),
            2: (128, 240),
            3: (144, 240),
            4: (160, 240),
            5: (113, 329),
               
        }
        
        
        self._b = bomber
        
        path_l = path_r = path_u = path_d = True
        
        for other in arena.collisions():
            
            if isinstance(other, Wall) or isinstance(other, Brick) or isinstance(other, Bomb):
                # wall can also be adjacent, w/o intersection
                ox, oy, ow, oh = other.pos() + other.size()
                
                if oy < self._y + self._h and self._y < oy + oh:
                    # ↕ overlap, ↔ movement is obstacled
                    if self._x > ox:
                        path_l = False
                    else:
                        path_r = False
                if ox < self._x + self._w and self._x < ox + ow:
                    # ↔ overlap, ↕ movement is obstacled
                    if self._y > oy:
                        path_u = False
                    else:
                        path_d = False
            
        match d:
                
            case 1:
                    
                if path_u:
                    
                    self._dx = 0
                    self._dy = self._speed
                
            case 2:
                    
                if path_d:
                        
                    self._dx = 0
                    self._dy = -self._speed
                
                
            case 3:
                    
                if path_r:
                        
                    self._dx = self._speed
                    self._dy = 0
                    
            case 4:
                    
                if path_l:
                    
                    self._dx = -self._speed
                    self._dy = 0
        
        

    def move(self, arena: Arena) -> None:
        
        if not(self._isdead):
        
            path_l = path_r = path_u = path_d = True
            
            for other in arena.collisions():
                
                if isinstance(other, Wall) or isinstance(other, Brick) or isinstance(other, Bomb):
                    # wall can also be adjacent, w/o intersection
                    ox, oy, ow, oh = other.pos() + other.size()
                    
                    if oy < self._y + self._h and self._y < oy + oh:
                        # ↕ overlap, ↔ movement is obstacled
                        if self._x > ox:
                            path_l = False
                        else:
                            path_r = False
                    if ox < self._x + self._w and self._x < ox + ow:
                        # ↔ overlap, ↕ movement is obstacled
                        if self._y > oy:
                            path_u = False
                        else:
                            path_d = False
                            
                
            
            aw, ah = arena.size()
            
            if not 0 <= self._x + self._dx <= aw - self._w:
                self._dx = -self._dx
            if not 0 <= self._y + self._dy <= ah - self._h:
                self._dy = -self._dy
                
            if self._x % 16 == 0 and (self._y - 24) % 16 == 0:
                
                d = choice([1, 2, 3, 4])
                
                
                for other in arena.collisions():
                    
                    if isinstance(other, tools.Fire.Fire):
                            
                        if (self._x + 16) != other.pos()[0] and (self._y + 16) != other.pos()[1]:
                                
                                self.hit(arena)
                            
                
                
                match d:
                    
                    case 1:
                        
                        self._current_sprite = self._right_animations[(self._right % 3)]
                        self._right += 1
                        
                        if path_u:
        
                            self._dx = 0
                            self._dy = self._speed
                    
                    case 2:
                        
                        self._current_sprite = self._left_animations[(self._left % 3)]
                        self._left += 1
                        
                        if path_d:
                            
                            self._dx = 0
                            self._dy = -self._speed
                    
                    
                    case 3:
                        
                        self._current_sprite = self._right_animations[(self._right % 3)]
                        self._right += 1
                        
                        if path_r:
                            
                            self._dx = self._speed
                            self._dy = 0
                        
                    case 4:
                        
                        self._current_sprite = self._left_animations[(self._left % 3)]
                        self._left += 1
                        
                        if path_l:
                            
                            self._dx = -self._speed
                            self._dy = 0
                        
            if (self._dx < 0 and not path_l or self._dx > 0 and not path_r or self._dy < 0 and not path_u or self._dy > 0 and not path_d):
                
                self._dx, self._dy = 0, 0
            
            
            self._x += self._dx
            self._y += self._dy
            
        else:
            
            self._dead_clock += 1
                
                
            if ((self._end_clock - self._dead_clock) % 6 == 0):
                    
                #print(self._death_animations)
                #print(self._co)
                #print(self._dead_clock)
                #print(self._end_clock)
            
                self._current_sprite = self._death_animations[self._co]
                
                if self._co <= 4:
                
                    self._co += 1
                    
                
                
            if self._dead_clock >= self._end_clock:
                
                arena.kill(self)
        

    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)

    def draw(self) -> None:
        
        draw_image(self._sprite, ((self._x + self._b.getOffset()), self._y), self._current_sprite, (self._w, self._h))
        
    def hit(self, arena: Arena) -> None:

        self._dead_clock = arena.count()
        self._end_clock = self._dead_clock + 48
        self._isdead = True
        
    def getPoints(self):
        
        return self._points