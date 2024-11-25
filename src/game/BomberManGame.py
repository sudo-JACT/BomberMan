

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
from random import choice, randrange
from npc.Lantern import *
from npc.Jelly import *
from npc.Ghost import *
from npc.Bear import *
from npc.Coin import *
global TALES
TALES=16
class BomberManGame(Arena):
    
    def __init__(self, stageN: int, size: Point=(496, 224), time: int=(300*30), img_src: str="./imgs/bomberman.png", canvas_size: Point=(256, 224)) -> None:
        
        super().__init__(size)
        
        global TALES
        TALES=16

        self._canvas_size = canvas_size
        
        self._img_src = img_src
        
        self._is_freeze = True
        
        self._win = False
        self._game_over = False
        
        self._b = BomberMan((TALES, TALES+24), img_src, ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "b"], canvas_size, self, 3)
        self._b_animation = self._b.getAnimation()
        
        self._stage = stageN
        
        self._time = time        
        
        self._e = []
        
        self._p = []
        
        self._ne = 0
        
        self.generate()


    def generate(self) -> None:   
        
        self._ne = 0
        
        door = False
        
        self.spawn(self._b)
        
        
        level = loadLevel(self._stage)
        
        level = level.split(" ")
        
        
        
        enemys = level[1].split("-")
        powerups = level[2].split("-")
        
        
        for x in range(len(enemys)):
            
            
            self._ne += int(enemys[x])
            
            if int(enemys[x]) > 0:
                
                for enemy in range(int(enemys[x])):
                    
                    self._pointerx = [choice([128, 144])]
                    self._pointery = [choice([168, 184])]
                    
                    self._enemys = {
            
                        0: Balloon(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        1: Beaker(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        2: Lantern(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        3: Face(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        4: Jelly(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        5: Ghost(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        6: Bear(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
                        7: Coin(self._pointerx[0], self._pointery[0], self._img_src, self, self._b),
            
                    }
                    
                    
                    self._e.append(self._enemys[x])
                    
                    
        for x in range(len(powerups)):
            
            if int(powerups[x]) > 0:
                
                for powerup in range(int(powerups[x])):
                    
                    self._pointerx = [choice([128, 144])]
                    self._pointery = [choice([168, 184])]
                    
                    self._powerups = {
            
                        0: BombUp((self._pointerx[0], self._pointery[0]), self._img_src, 0, self, self._b),
                        1: FireUp((self._pointerx[0], self._pointery[0]), self._img_src, 0, self, self._b),
                        2: Detonator((self._pointerx[0], self._pointery[0]), self._img_src, 2, self, self._b),
                        3: SpeedUp((self._pointerx[0], self._pointery[0]), self._img_src, 2, self, self._b),
                        4: BombPass((self._pointerx[0], self._pointery[0]), self._img_src, 3, self, self._b),
                        5: WallPass((self._pointerx[0], self._pointery[0]), self._img_src, 5, self, self._b),
                        6: Invincible((0, 0), self._img_src, 7, self, self._b),
                        7: FirePass((self._pointerx[0], self._pointery[0]), self._img_src, 5, self, self._b),
            
                    }
                    
                    self._p.append(self._powerups[x])
        
        
        for i in range(int((self.size()[1]-TALES) / TALES)):
            
            self.spawn(Wall((0, (i*TALES+24)), self._img_src, self._b))
            self.spawn(Wall(((self.size()[0] - TALES), (i*TALES)+24), self._img_src, self._b))
            
            
        for i in range(int(self.size()[0] / TALES)):    
            
            self.spawn(Wall((i*TALES, 24), self._img_src, self._b))
            self.spawn(Wall((i*TALES, (self.size()[1]-TALES-TALES)+24), self._img_src, self._b))
        
        for x in range(int(self.size()[0] / TALES)):
            
            if x % 2 == 0:
        
                for y in range(int((self.size()[1]-TALES) / TALES)):
                    
                    if y % 2 == 0:
                        
                        self.spawn(Wall(((x*TALES), (y * TALES)+24), self._img_src, self._b))
                    
                    else:
                        
                        s = choice([-1, 0, 1])
                        
                        if s == 1 and ((x*TALES)) != 0 and ((x*TALES)) != self.size()[0]-TALES:
                            
                            if len(self._p) > 0:
                                
                                tmp = self._p[randrange(len(self._p))]
                                
                                self._p.pop(self._p.index(tmp))
                                
                                tmp.setPos(((x*TALES), (y * TALES)+24))
                                

                                
                                self.spawn(tmp)
                                
                            if not(door):
                                
                                self.spawn(Door((x*TALES, ((y * TALES)+24)), self._ne, self._img_src, (176, 48), self._b))
                                
                                door = True
                                
                            
                            self.spawn(Brick(((x*TALES), (y * TALES)+24), self._img_src, self._b))
                            
                        
                            
                            
                                
            else:
            
                for y in range(int((self.size()[1]-TALES) / TALES)-1):
                    
                    if y % 2 == 0:
                        
                        s = choice([-1, 0, 1, 2])
                        
                        if (s == 1 or s == -1) and y*TALES != 0 and y*TALES != self.size()[1]-TALES and ((x*TALES != TALES) and ((y*TALES)+24) != 40):# and ((x != 1 and y != 1) or ((x != 1 and y != 2) or (x != 2 and y != 1))):
                            
                            self.spawn(Brick((x*TALES, (y * TALES)+24), self._img_src, self._b))
                            
                    else:
                        
                        s = choice([-1, 0, 1, 2])
                        
                        if (s == 1 or s == -1) and y*TALES != 0 and y*TALES != self.size()[1] and ((x*TALES != TALES) and ((y*TALES)+24) != 40):# and ((x != 1 and y != 1) or ((x != 1 and y != 2) or (x != 2 and y != 1))):
                            
                            self.spawn(Brick((x*TALES, (y * TALES)+24), self._img_src, self._b))
                            
                        else:
                            
                            lol = choice([-1, 0, 1])
                            
                            for other in self.actors():
                                
                                if (isinstance(other, Brick) or isinstance(other, Wall)) and (other.pos()[0] == (x*TALES) and (other.pos()[1] == (y * TALES)+24)):
                                    
                                    lol = 0
                                    
                            dx = self._b.pos()[0] - (x * TALES)
                            dy = self._b.pos()[1] - ((y * TALES)+24)
                            raggio = ((dx)**2 + (dy)**2)**(0.5)
                                    
                            if raggio < 55:
                                
                                lol = 0
                            
                            if len(self._e) > 0 and lol == 1:
                                
                                tmp = self._e[randrange(len(self._e))]
                                
                                self._e.pop(self._e.index(tmp))
                                
                                tmp.setPos(((x*TALES), (y * TALES)+24))
                                
                                self.spawn(tmp)
                            
        
                            
                            
    def getTime(self) -> int:
        
        return self._time - self.count()
        
        
    def killemall(self) -> None:

        tmp = self._b

        self._actors.clear()
        
        self._b = tmp

        if self._b.getLives() >= 0:
        
            self.spawn(self._b)
        
        self._e.clear()
        
        #for x in self._actors:
            
            #if not(isinstance(x, BomberMan)):
                
                #self._actors.pop(self._actors.index(x))

    def GameOver(self) -> bool:

        return self._b.getLives() < 0 
    
    def GameWin(self) -> bool:
        
        for x in self.actors():
            
            if isinstance(x, Door):
                
                if x.getNextLevel():
                    
                    #self.kill(self._b)
                    
                    if self._stage < 50:
                    
                        self._stage += 1
                        
                        self._b.setPos((TALES, 40))
                    
                    return True
                
        return False
    
    def getCanvasSize(self) -> Point:
        
        return self._canvas_size
    
    def getBomber(self) -> BomberMan:
        
        return self._b
    
    def regenerate(self) -> None:
        
        #self._e = []
        
        #self._p = []
        
        #self._ne = 0
        
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