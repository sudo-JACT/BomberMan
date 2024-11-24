import os
import sys

#if os.name != "nt":
    
#    sys.path.append('../')
    
#else:
    
#    sys.path.append('..\\')

from libs.g2d import *
from libs.actor import *
from background.Wall import *
from background.Brick import *
from random import choice
from tools.Bomb import *
import player
#from game.BomberManGame import *


class Enemy():
    
    def sub(self, arena: Arena) -> None:
        
        arena.decEnemy()
        
    def addP(self) -> None:
        
        self._b.addPoints(self._points)
    