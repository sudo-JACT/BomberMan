import sys
sys.path.append('../')


from libs.g2d import *
from libs.actor import *
from tools.Bomb import *
from time import sleep
from npc.Balloon import *
from tools.Fire import *
from background.Wall import *
from background.Brick import *



class BomberMan(Actor):
    
    def __init__(self, pos: Point, sprite_src: str, keys: list[str]) -> None:
        self._x, self._y = pos
        self._dx = self._dy = 0
        self._w, self._h = 16, 16
        self._speed = 2
        self._sprite = sprite_src
        
        self._keys = keys
        
        self._up = 0
        self._down = 0
        self._left = 0
        self._right = 0
        
        self._front_animations = {
            
            0: (50, 0),
            1: (66, 0),
            2: (82, 0),

        }
        
        self._back_animations = {
            
            0: (50, 16),
            1: (66, 16),
            2: (82, 16),
            
        }
        
        self._left_animations = {
            
            0: (2, 0),
            1: (18, 0),
            2: (34, 0),
            
        }
        
        self._right_animations = {
            
            0: (2, 16),
            1: (18, 16),
            2: (34, 16),
            
        }
        
        self._death_animations = {
            
            0: (2, 32),
            1: (18, 32),
            2: (33, 32),
            3: (50, 32),
            4: (65, 32),
            5: (80, 33),
            6: (98, 33),
            
        }
        
        self._current_sprite = self._front_animations[1]

    def move(self, arena: Arena):
        
        path_l = path_r = path_u = path_d = True
        
        for other in arena.collisions():
            
            if isinstance(other, Balloon):
                
                self.hit(arena)

        keys = arena.current_keys()
        
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
                        
        
        if self._keys[0] in keys and self._x % 16 == 0 and path_u:
            
            self._y -= self._speed 
            self._current_sprite = self._back_animations[(self._up % 3)]
            self._up += 1
            
            
        elif self._keys[1] in keys and self._x % 16 == 0 and path_d:
            
            self._y += self._speed
            self._current_sprite = self._front_animations[(self._down % 3)]
            self._down +=1
            
                
            
        elif self._keys[2] in keys and self._y % 16 == 0 and path_l:
            
            self._x -= self._speed
    
            self._current_sprite = self._left_animations[(self._left % 3)]
            self._left += 1
            
        elif self._keys[3] in keys and self._y % 16 == 0 and path_r:
            
            self._x += self._speed
            self._current_sprite = self._right_animations[(self._right % 3)]
            self._right += 1
            
        elif self._keys[4] in keys:
            
            arena.spawn(Bomb((self._x, self._y), self._sprite, arena))
        
        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w) 
        self._y = min(max(self._y, 0), ah - self._h) 
        
        if (self._dx < 0 and not path_l or self._dx > 0 and not path_r or self._dy < 0 and not path_u or self._dy > 0 and not path_d):
            
            self._dx, self._dy = 0, 0

    def hit(self, arena: Arena):
        
        for i in range(len(self._death_animations)):
            
            self._current_sprite = self._death_animations[i]
            
            sleep(1/60)
        
        arena.kill(self)
        
        
    def pos(self) -> Point:

        return self._x, self._y


    def size(self) -> Point:

        return self._w, self._h


    def draw(self) -> None:
        
        draw_image(self._sprite, (self._x, self._y), self._current_sprite, (self._w, self._h))
