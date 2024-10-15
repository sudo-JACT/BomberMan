from libs.g2d import *
from tools import Bomb
from player.PlayerInterface import PlayerInterface


class Bomberman(PlayerInterface):
    
    def __init__(self, hp: int, speed: int, sprites: str, pos: Point) -> None:
        
        self._hp = hp
        self._sprits = sprites
        self._speed = speed
        self._pos = pos
    
    
    def move(self) -> None:
        
        return super().move()
    