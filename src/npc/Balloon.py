import sys
sys.path.append('../')


from libs.g2d import *
from libs.actor import *
from background.Wall import *
from background.Brick import *
from random import choice
from tools.Bomb import *

class Balloon(Actor):
    
    def __init__(self, x0: int, y0: int, sprite_src: str, arena: Arena) -> None:
        self._x = x0 
        self._y = y0
        self._speed = 2
        self._dx = self._dy = 0
        self._w, self._h = 16, 16
        self._sprite = sprite_src
        self._current_sprite = (0, 240)
        d = choice([1, 2, 3, 4])
        
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
        
        self._directions = {
    
            "up" : 1,
            "down": 2,
            "right": 3,
            "left": 4,
            
    }

    def move(self, arena: Arena) -> None:
        
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
            
        if self._x % 16 == 0 and self._y % 16 == 0:
            
            d = choice([1, 2, 3, 4])
            
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
                    
        if (self._dx < 0 and not path_l or self._dx > 0 and not path_r or self._dy < 0 and not path_u or self._dy > 0 and not path_d):
            
            self._dx, self._dy = 0, 0
        
        
        self._x += self._dx
        self._y += self._dy
        

    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)

    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x, self._y), self._current_sprite, (self._w, self._h))
    

