import os
import sys

if os.name != "nt":
    
    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')

from libs.g2d import *
import player.BomberMan