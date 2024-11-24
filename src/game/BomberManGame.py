

#from libs.g2d import *
#from libs.actor import *
#from player.BomberMan import *
#from background.Wall import *
#from background.Brick import *
#from tools.PowerUps import *
#from npc.Balloon import *
#from npc.Face import *
#from libs.datahandler import *


import os
import sys

#if os.name != "nt":
    
#    sys.path.append('../')
    
#else:
    
#    sys.path.append('..\\')

from libs.g2d import *
from libs.actor import *
from npc.Balloon import *
from npc.Face import *
from npc.Beaker import *
from player.BomberMan import *
from background.Wall import *
from background.Brick import *
from tools.PowerUps import *
from libs.datahandler import *
from background.Door import Door
from random import choice

class BomberManGame(Arena):
    
    def __init__(self, stageN: int, size: Point=(496, 224), time: int=(300*30), img_src: str="./imgs/bomberman.png", canvas_size: Point=(256, 224)) -> None:
        
        super().__init__(size)
        
        self._canvas_size = canvas_size
        
        self._img_src = img_src
        
        self._is_freeze = True
        
        self._win = False
        self._game_over = False
        
        self._b = BomberMan((16, 40), img_src, ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "b"], canvas_size, self, 3)
        self._b_animation = self._b.getAnimation()
        
        self._stage = stageN
        
        self._time = time        
        
        
        
        self.generate()


    def generate(self) -> None:
        
        
        
        self.spawn(self._b)
        
        
        level = loadLevel(self._stage)
        
        level = level.split(" ")
        
        print(level)
        
        enemys = level[1].split("-")
        powerups = level[2].split("-")
        
        print(enemys)
        
        for x in range(len(enemys)):
            
            print(x)
            print(enemys[x])
            
            if int(enemys[x]) > 0:
                
                for enemy in range(int(enemys[x])):
                    
                    self._pointerx = [choice([128, 144])]
                    self._pointery = [choice([168, 184])]
                    
                    self._enemys = {
            
                        0: Balloon(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        1: Beaker(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        2: Face(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        3: Face(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        4: Face(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        5: Face(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        6: Face(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        7: Face(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
            
                    }
                    
                    #e = self._enemys[x]
                    
                    print(enemy)
                    
                    #print(e)
                    
                    print(self._pointerx)
                    print(self._pointery)
                    
                    print(self._enemys[x])
                    
                    #e.setPos((self._pointerx[0], self._pointery[0]))
                    
                    self._actors.append(self._enemys[x])
                    
                    
        for x in range(len(powerups)):
            
            print(x)
            print(powerups[x])
            
            if int(powerups[x]) > 0:
                
                for powerup in range(int(powerups[x])):
                    
                    self._pointerx = [choice([128, 144])]
                    self._pointery = [choice([168, 184])]
                    
                    self._powerups = {
            
                        0: BombUp((self._pointerx[0], self._pointery[0]), self._img_src, 0, self, self._b),
                        1: BombUp((self._pointerx[0], self._pointery[0]), self._img_src, 0, self, self._b),
                        2: SpeedUp((self._pointerx[0], self._pointery[0]), self._img_src, 2, self, self._b),
                        3: SpeedUp((self._pointerx[0], self._pointery[0]), self._img_src, 2, self, self._b),
                        4: WallPass((self._pointerx[0], self._pointery[0]), self._img_src, 3, self, self._b),
                        5: BombPass((self._pointerx[0], self._pointery[0]), self._img_src, 5, self, self._b),
                        6: BombPass((self._pointerx[0], self._pointery[0]), self._img_src, 5, self, self._b),
                        7: BombPass((self._pointerx[0], self._pointery[0]), self._img_src, 5, self, self._b),
            
                    }
                    
                    #e = self._enemys[x]
                    
                    print(powerups)
                    
                    #print(e)
                    
                    print(self._pointerx)
                    print(self._pointery)
                    
                    print(self._enemys[x])
                    
                    #e.setPos((self._pointerx[0], self._pointery[0]))
                    
                    self._actors.append(self._powerups[x])
        
        
        
        #self.spawn(WallPass((16, 72), self._img_src, 3, self, self._b))
        #self.spawn(BombUp((16, 88), self._img_src, 0, self, self._b))
        #self.spawn(BombPass((16, 104), self._img_src, 5, self, self._b))
        #self.spawn(SpeedUp((16, 120), self._img_src, 2, self, self._b))

        #self.spawn(Balloon(128, 168, self._img_src, self, self._b))
        #self.spawn(Face(144, 184, self._img_src, self, self._b))
        #self.spawn(Beaker(144, 184, self._img_src, self, self._b))

        
        
        for i in range(int((self.size()[1]-16) / 16)):
            
            self.spawn(Wall((0, (i*16+24)), self._img_src, self._b))
            self.spawn(Wall(((self.size()[0] - 16), (i*16)+24), self._img_src, self._b))
            
            
        for i in range(int(self.size()[0] / 16)):    
            
            self.spawn(Wall((i*16, 24), self._img_src, self._b))
            self.spawn(Wall((i*16, (self.size()[1]-16-16)+24), self._img_src, self._b))
        
        for x in range(int(self.size()[0] / 16)):
            
            if x % 2 == 0:
        
                for y in range(int((self.size()[1]-16) / 16)):
                    
                    if y % 2 == 0:
                        
                        self.spawn(Wall(((x*16), (y * 16)+24), self._img_src, self._b))
                    
                    else:
                        
                        s = choice([-1, 0, 1])
                        
                        if s == 1 and ((x*16)) != 0 and ((x*16)) != self.size()[0]-16:# and ((x != 1 and y != 1) or ((x != 1 and y != 2) or (x != 2 and y != 1))):
                            
                            self.spawn(Brick(((x*16), (y * 16)+24), self._img_src, self._b))
                            
        self.spawn(Door((16, 56), 1, self._img_src, (176, 48), self._b))
                            
                            
    def getTime(self) -> int:
        
        return self._time - self.count()
        
        
    def killemall(self) -> None:

        #tmp = self._b

        #self._actors.clear()
        
        #self._b = tmp
        
        #self.spawn(self._b)
        
        for x in self._actors:
            
            if not(isinstance(x, BomberMan)):
                
                self._actors.pop(self._actors.index(x))

    def GameOver(self) -> bool:

        return self._b.getLives() < 0 
    
    def GameWin(self) -> bool:
        
        for x in self.actors():
            
            if isinstance(x, Door):
                
                if x.getNextLevel():
                    
                    self.kill(self._b)
                    
                    return True
                
        return False
    
    def getCanvasSize(self) -> Point:
        
        return self._canvas_size
    
    def getBomber(self) -> BomberMan:
        
        return self._b
    
    def regenerate(self) -> None:
        
        self.killemall()
        
        #tmp = BomberMan((16, 40), self._img_src, self._b.getKeys(), self._canvas_size, self, self._b.getLives(), self._b.getPowerUp())
        
        #self.kill(self._b)
        
        #self._b = tmp   
        
        self.generate()
        
    def freeze(self) -> None:
        
        self._is_freeze = True

    def stopfreeze(self) -> None:
        
        self._is_freeze = False
        
    def getF(self) -> bool:    
        
        return self._is_freeze
    
    def setBomberAnimation(self, a) -> None:
        
        self._b.setAnimation(a)
        
    def getBomberAnimation(self) -> bool:
        
        return self._b.getAnimation()
    
    def decEnemy(self) -> None:
        
        for x in self.actors():
            
            if isinstance(x, Door):
                
                x.dEnemy()