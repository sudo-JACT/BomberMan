import os
import sys

import npc.Enemy

if os.name != "nt":

    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')


import background.Brick
import background.Wall
from libs.g2d import *
from libs.actor import *
import tools
from time import sleep
import npc
from tools.Fire import *
import background



class BomberMan(Actor):
    
    def __init__(self, pos: Point, sprite_src: str, keys: list[str], canvas_size: Point, arena: Arena, lives: int, powerups: list[int]=[0, 0, 0, 0, 0, 0, 0, 0]) -> None:
        self._x, self._y = pos
        self._dx = self._dy = 0
        self._w, self._h = 16, 16
        self._speed = 2
        self._sprite = sprite_src
        self._isdead = False
        self._dead_clock = 0
        self._end_clock = 0
        self._co = 0
        
        self._max_fire = 3
        
        self._powerups = powerups
        
        self._p = {
            
            0: self.bombUp(powerups[0]),
            1: self.setMaxFire(powerups[1]),
            2: self.setSpeed(),
            3: self.remoteDetonator(),
            4: self.setWallPass(),
            5: self.setBombPass(),
            6: self.setfirePass(),
            7: self.setInvincible(),
            
        }
        
        self._speed -=2
        
        for x in powerups:
            
            if powerups[x] != 0:
                
                self._p[x]
        
        
        
        self._points = 0
    
        self._lives = lives
        
        
        
        self._max_bomb_spawnrate = 1
        self._spawned_all_the_bombs = False
        self._bomb_at_the_moment = 0
        
        self._immortal = False
        
        self._wallpass = False
        self._bombpass = False
        
        self._c = canvas_size
        self._a = arena
        
        self._keys = keys
        
        self._up = self._down = self._left = self._right = 0
        
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
        
        if not(self._isdead):
        
            path_l = path_r = path_u = path_d = True
            
            for other in arena.collisions():
                
                if isinstance(other, npc.Enemy.Enemy) or isinstance(other, tools.Fire.Fire):
                    
                    if isinstance(other, Fire):
                        
                        if (self._x + 16) != other.pos()[0] and (self._y + 16) != other.pos()[1]:
                            
                            self.hit(arena)
                        
                    else:
                    
                        self.hit(arena)

            keys = arena.current_keys()
            
            for other in arena.collisions():
                
                if isinstance(other, background.Wall.Wall) or (isinstance(other, background.Brick.Brick) and not(self._wallpass)) or (isinstance(other, tools.Bomb.Bomb) and not(self._bombpass)):
                    
                    if not(isinstance(other, tools.Bomb.Bomb) and other.get_current_clock() <= (other.get_end_clock() - 85)):    
                            
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
                    
                        
            
            if self._keys[0] in keys and not(self._isdead):
                
                self._current_sprite = self._back_animations[(self._up % 3)]
                self._up += 1
                
                if path_u:
                    
                    self._y -= self._speed 
                    
                
                
            elif self._keys[1] in keys  and not(self._isdead):
                
                self._current_sprite = self._front_animations[(self._down % 3)]
                self._down +=1
                play_audio("./sounds/Bomberman SFX (1).wav", False)
                
                if path_d:
                    
                    self._y += self._speed
                
                    
                
            elif self._keys[2] in keys and not(self._isdead):
        
                self._current_sprite = self._left_animations[(self._left % 3)]
                self._left += 1
                
                if path_l:
                    
                    self._x -= self._speed
                
            elif self._keys[3] in keys and not(self._isdead):
                
                self._current_sprite = self._right_animations[(self._right % 3)]
                self._right += 1
                
                if path_r:
                    
                    self._x += self._speed
                
            elif self._keys[4] in keys and (self._x % 16 == 0 and (self._y + 24) % 16 == 0):
                
                if self._bomb_at_the_moment <= self._max_bomb_spawnrate:
                
                    arena.spawn(tools.Bomb.Bomb((self._x, self._y), self._sprite, arena, self))
                    
                    self._bomb_at_the_moment += 1
            
            aw, ah = arena.size()
            self._x = min(max(self._x, 0), aw - self._w) 
            self._y = min(max(self._y, 0), ah - self._h) 
            
            if (self._dx < 0 and not path_l or self._dx > 0 and not path_r or self._dy < 0 and not path_u or self._dy > 0 and not path_d):
                
                self._dx, self._dy = 0, 0
                
        else:
            
            self._dead_clock += 1
                
                
            if ((self._end_clock - self._dead_clock) % 7 == 0):
                    
                #print(self._death_animations)
                #print(self._co)
                #print(self._dead_clock)
                #print(self._end_clock)
            
                self._current_sprite = self._death_animations[self._co]
                self._co += 1
                    
                
                
            if self._dead_clock >= self._end_clock:
                
                arena.kill(self)
                
                if self._lives >= 0:
                    
                    self.reSpwan()


    def hit(self, arena: Arena):
        
        if not(self._immortal):
                
            self._lives -= 1
        
            self._dead_clock = arena.count()
            self._end_clock = self._dead_clock + 49
            self._isdead = True
            
            
            
            
        
        
        
    def pos(self) -> Point:

        return self._x, self._y


    def size(self) -> Point:

        return self._w, self._h


    def draw(self) -> None:
        
        draw_image(self._sprite, ((self._x + self.getOffset()), self._y), self._current_sprite, (self._w, self._h))
        
    def getOffset(self) -> int:
        
        if self._x > (self._c[0] / 2) and self._x <= self._a.size()[0] - (self._c[0] / 2):
            
           return -1 * (self._x - (self._c[0] / 2))
            
        
        elif self._x >= (self._a.size()[0] - (self._c[0] / 2)):
            
            return -1 * (self._a.size()[0] - self._c[0])
        
        else: 
            
            return 0
        
    def setInvincible(self) -> None:
        
        pass
        
    def setfirePass(self) -> None:
        
        pass
        
    def setBombPass(self) -> None:
        
        pass
        
    def remoteDetonator(self) -> None:
        
        pass
        
    def bombUp(self, bomb: int=1):
        
        pass
        
    def setWallPass(self) -> None:
        
        self._powerups[4] = 1
        
        self._wallpass = True
        
    def detonated(self) -> None:
        
        self._bomb_at_the_moment -= 1
        
    def setMaxBomb(self, fire: int=1) -> None:
        
        if self._max_bomb_spawnrate < 10:
            
            self._max_bomb_spawnrate += 1
            
    def setBombPass(self) -> None:
        
        self._powerups[5] = 1
        
        self._bombpass = True
        
    def setSpeed(self) -> None:
        
        self._speed += 2
        
    def getMaxFire(self) -> int:
        
        return self._max_fire
    
    def setMaxFire(self, max: int=1) -> None:
        
        if self._max_fire < 10:
        
            self._powerups[1] += 1
            
            self._max_fire += max
        
    def getLives(self) -> int:
        
        return self._lives
    
    def moreLives(self) -> None:
        
        self._lives += 1
        
    def setLives(self, l: int=3) -> None:
        
        self._lives = l
        
    def reSpwan(self) -> None:
        
        self._x, self._y = 16, 40
        self._isdead = False
        self._current_sprite = self._front_animations[1]
        self._dead_clock = 0
        self._end_clock = 0
        self._co = 0
        
        self._a.spawn(self)
        
    def addPoints(self, p: int) -> None:
        
        self._points += p
        
    def getPoints(self) -> int:
        
        return self._points
    
    def getPowerUp(self) -> list[int]:
        
        return self._powerups
    
    def getSpeed(self) -> int:
        
        return self._speed
        