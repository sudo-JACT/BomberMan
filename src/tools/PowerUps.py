import os
import sys
from abc import abstractmethod

if os.name != "nt":
    
    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')

from background.Brick import Point
from background.Wall import Point
from libs.actor import Arena, Point
from libs.g2d import *
from libs.actor import *
from background.Wall import *
from background.Brick import *
from random import choice
from tools.Bomb import *
from player.BomberMan import BomberMan


class PowerUp(Actor):
    
    def __init__(self, pos: Point, sprt: str, uptype: int, arena: Arena, bomer: BomberMan) -> None:
        
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._sprite = sprt
        
        self._b = bomer
        self._a = arena
        
        self._powers = {
            
            0: (0, 224),
            1: (16, 224),
            2: (32, 224),
            3: (48, 224),
            4: (64, 224),
            5: (80, 224),
            6: (96, 224),
            7: (112, 224),
            
        }
        
        self._current_sprite = self._powers[uptype]
        
        
    def move(self, arena: Arena) -> None:
        
        for other in arena.collisions():
                
            if isinstance(other, player.BomberMan.BomberMan):
                
                self.giveBonus()
                
                arena.kill(self)
    
    def pos(self) -> tuple[int, int]:
        
        return self._x, self._y
    
    def size(self) -> tuple[int, int]:
        
        return (self._w, self._h)
    
    def draw(self) -> None:
        
        draw_image(self._sprite, ((self._x + self._b.getOffset()), self._y), self._current_sprite, (self._w, self._h))
    
        
        
    @abstractmethod
    def giveBonus(self) -> None:
        
        pass
    
    

class BombUp(PowerUp):
    
    def giveBonus(self) -> None:
        
        self._b.setMaxBomb()
        

class FireUp(PowerUp):
    
    def giveBonus(self) -> None:
        
        return super().giveBonus()
    
class SpeedUp(PowerUp):
    
    def giveBonus(self) -> None:
        
        self._b.setSpeed()

    
class WallPass(PowerUp):
    
    def giveBonus(self) -> None:
        
        self._b.setWallPass()
        
        
class BombPass(PowerUp):
    
    def giveBonus(self) -> None:
        
        self._b.setBombPass()

class firePass(PowerUp):
    
    def giveBonus(self) -> None:
        
        self._b.setfirePass()