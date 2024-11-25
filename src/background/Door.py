from libs.g2d import *
from libs.actor import *
from player.BomberMan import *
from game.BomberManGui import *


class Door(Actor):
    
    def __init__(self, pos: Point, enemys: int, img: str, sprite_pos: Point, bomber: BomberMan) -> None:
        
        self._x, self._y = pos
        
        self._img = img
        
        self._spos = sprite_pos
        
        self._enemys = enemys
        
        self._b = bomber
        
        self._d = (16, 16)
        
        self._nextLevel = False
        
        
    def move(self, arena: Arena) -> None:
        
        for other in arena.collisions():
            
            if isinstance(other, BomberMan) and (self._enemys == 0):
                
                self._nextLevel = True
                
        
                
                
    def pos(self) -> Point:
        
        return (self._x, self._y)
    
    
    def draw(self) -> None:
        
        draw_image(self._img, ((self._x + self._b.getOffset()), self._y), self._spos, self._d)
        
    def size(self) -> Point:
        
        return self._d
        
        
    def getNextLevel(self) -> bool:
        
        return self._nextLevel
    
    def dEnemy(self) -> None:
        
        self._enemys -= 1
        
    def getEnemys(self) -> int:
        
        return self._enemys