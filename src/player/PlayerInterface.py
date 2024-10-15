from libs.g2d import *
from libs.actor import Actor
from abc import abstractmethod

class PlayerInterface(Actor):
    
    def __init__(self) -> None:
        
        self._hp: int
        self._sp: str
        self._speed: int
        self._pos: tuple[int, int]
        
        
    # Get methos
        
    def gethp(self) -> int:
        
        return self._hp
    
    def getsp(self) -> int:
        
        return self._sp
    
    def getspeed(self) -> int:
        
        return self._speed
        
    def getpos(self) -> tuple[int, int]:
        
        return self._pos
    
    
    # Set methos
    
    def sethp(self, hp) -> None:
        
        self._hp = hp
    
    def setsp(self, sp) -> None:
        
        self._sp = sp
    
    def setspeed(self, speed) -> None:
        
        self._speed = speed
        
    def setpos(self, pos: tuple[int, int]) -> None:
        
        self._pos = pos
        
        
    @abstractmethod
    def move(self) -> None:
        
        pass