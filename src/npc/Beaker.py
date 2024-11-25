import os
import sys

if os.name != "nt":
    
    sys.path.append('../')
    
else:
    
    sys.path.append('..\\')

from libs.g2d import *
from libs.actor import *
from background.Wall import *
from background.Brick import *
from random import choice
from tools.Bomb import *
import player
from npc.Enemy import Enemy

class Beaker(Actor,Enemy):
    
    # Inizializza il nemico
    
    def __init__(self, x0: int, y0: int, sprite_src: str, arena: Arena, bomber: player.BomberMan.BomberMan) -> None: 
        
        self._x = x0 
        self._y = y0
        self._speed = 1
        self._dx = self._dy = 0
        self._w, self._h = 16, 16
        self._sprite = sprite_src
        self._current_sprite = (48, 256)
        d = choice([1, 2, 3, 4])
        self._isdead = False
        self._walking= False
        
        self._dead_clock = 0
        self._end_clock = 0
        self._co = 0
        
        self._points = 200
        
        self._left = self._right = 0
        #mappatura sprite
        self._directions = {
    
            "up" : 1,
            "down": 2,
            "right": 3,
            "left": 4,
        
        }


        # Mappatura degli sprite
        
        self._left_animations = {
            
            0: (48, 256),
            1: (64, 256),
            2: (80, 256),
            
        }
        
        self._right_animations = {
            
            0: (0, 256),
            1: (16, 256),
            2: (32, 256),
            
        }
        
        self._death_animations = {
            
            0: (96, 256),
            1: (112, 240),
            2: (128, 240),
            3: (144, 240),
            4: (160, 240),
            5: (113, 345),
               
        }
        
        
        self._b = bomber 
        
        # Flag di direzione
        
        path_l = path_r = path_u = path_d = True  
        
        
        # Controllo intersezioni 
        
        for other in arena.collisions(): 
            
            if isinstance(other, Wall) or isinstance(other, Brick) or isinstance(other, Bomb):
                
                ox, oy, ow, oh = other.pos() + other.size()
                
                if oy < self._y + self._h and self._y < oy + oh:
                    
                    if self._x > ox:
                        path_l = False
                    else:
                        path_r = False
                if ox < self._x + self._w and self._x < ox + ow:
                    
                    if self._y > oy:
                        path_u = False
                    else:
                        path_d = False
           
        # Scelta di una direzione iniziale casuale 
        
        match d:
                
            case 1:
                    
                if path_u:
                    
                    self._dx = 0
                    self._dy = self._speed
                
            case 2:
                    
                if path_d:
                        
                    self._dx = 0
                    self._dy = -self._speed
                
                
            case 3:
                    
                if path_r:
                        
                    self._dx = self._speed
                    self._dy = 0
                    
            case 4:
                    
                if path_l:
                    
                    self._dx = -self._speed
                    self._dy = 0
        
        

    def move(self, arena: Arena) -> None:           #metodo per gestire il movimento
        
        # Controllo per vedere se il nemico è morto
        
        if not(self._isdead): 
        
            path_l = path_r = path_u = path_d = True
            
            
            # Controllo delle collisioni con muri e bombe
            
            for other in arena.collisions(): 
                
                if isinstance(other, Wall) or isinstance(other, Brick) or isinstance(other, Bomb):
                    
                    
                    # Scomposizione dimensioni dell'actor con cui collide 
                    
                    ox, oy, ow, oh = other.pos() + other.size()    
                    
                    
                    # Blocco il passaggio per quella direzione in caso di collisione
                    
                    if oy < self._y + self._h and self._y < oy + oh:
                        
                        if self._x > ox:
                            path_l = False
                        else:
                            path_r = False
                    if ox < self._x + self._w and self._x < ox + ow:
                        
                        if self._y > oy:
                            path_u = False
                        else:
                            path_d = False
                            
            aw, ah = arena.size()
        
        
            # Scomposizione della posizione di bomberman
            
            bomber_x, bomber_y = self._b.pos()
        
        
            # Dimensione dalla distanza con il giocatore su x e y utilizando la dstanza tra due punti 
        
            dx = bomber_x - self._x
            dy = bomber_y - self._y
            raggio= ((dx)**2 + (dy)**2)**(0.5)


            # Controllo se bomberman entra nel raggio del nemico

            if raggio < 30:        

                
                # Movimento orizontale verso bomberman 

                if abs(dx) > abs(dy):  
                    
                    if dx > 0 and path_r:
                        
                        self._dx = self._speed
                        self._dy = 0
                        
                        
                        # Animazione movimento
                        
                        self._current_sprite = self._right_animations[(self._right % 3)]
                        self._right += 1
                        
                    elif dx < 0 and path_l:
                         
                        self._dx = -self._speed
                        self._dy = 0
                        
                        
                        # Animazione movimento
                        
                        self._current_sprite = self._left_animations[(self._left % 3)]
                        self._left += 1
                
                
                # Movimento verticale verso bomberman               
                
                else:   
                    if dy > 0 and path_d:
                        
                        self._dx = 0
                        self._dy = self._speed
                        
                        
                        # Animazione movimento

                        self._current_sprite = self._left_animations[(self._left % 3)]
                        self._left += 1
                        
                    elif dy < 0 and path_u:
                        self._dx = 0
                        self._dy = -self._speed                                                 
                        
                        
                        # Animazione movimento
                        
                        self._current_sprite = self._right_animations[(self._right % 3)]
                        self._right += 1
            
            
            # Movimento casuale
            
            else: 

                if self._x % 16 == 0 and (self._y + 24) % 16 == 0:
                
                    d = choice([1, 2, 3, 4])

                    
                    # Setta una flag se si trova in movimeto
                    
                    if not(self._walking):  
                        
                        self._walking = not(self._walking)
                    
                    
                    # Controllo collisione con il fuoco
                    
                    for other in arena.collisions(): 
                        
                        if isinstance(other, tools.Fire.Fire):
                                
                            if (self._x + 16) != other.pos()[0] and (self._y + 16) != other.pos()[1]:
                                    
                                    self.hit(arena)
                                
                    
                    
                    # Movimento casuale
                    
                    match d:
                        
                        case 1:
                            
                            self._current_sprite = self._right_animations[(self._right % 3)]
                            self._right += 1
                            
                            if path_u:
            
                                self._dx = 0
                                self._dy = self._speed
                        
                        case 2:
                            
                            self._current_sprite = self._left_animations[(self._left % 3)]
                            self._left += 1
                            
                            if path_d:
                                
                                self._dx = 0
                                self._dy = -self._speed
                        
                        
                        case 3:
                            
                            self._current_sprite = self._right_animations[(self._right % 3)]
                            self._right += 1
                            
                            if path_r:
                                
                                self._dx = self._speed
                                self._dy = 0
                            
                        case 4:
                            
                            self._current_sprite = self._left_animations[(self._left % 3)]
                            self._left += 1
                            
                            if path_l:
                                
                                self._dx = -self._speed
                                self._dy = 0
                                
                
                # Riallinea gradualmente il nemico alla griglia quando non si trova in multipli di 16 e non è in movimento
                
                elif self._x % 16 != 0 and not(self._walking):

                    if self._x % 16 < 8 and path_l:
                        
                        self._dx = -self._speed
                        
                    elif path_r:
                        
                        self._dx = self._speed
                    
                elif (self._y +24)% 16 != 0 and not(self._walking) :
                    
                    if (self._y +24)% 16 < 8 and path_u:
                        
                        self._dy = -self._speed
                        
                    elif path_d:
                        
                        self._dy = self._speed
                    
                                            

            if not 0 <= self._x + self._dx <= aw - self._w:
                self._dx = -self._dx
            if not 0 <= self._y + self._dy <= ah - self._h:
                self._dy = -self._dy
                
                
            for other in arena.collisions():
                    
                if isinstance(other, tools.Fire.Fire):
                            
                    if (self._x + 16) != other.pos()[0] and (self._y + 16) != other.pos()[1]:
                                
                            self.hit(arena)    
                
            if (self._dx < 0 and not path_l or self._dx > 0 and not path_r or self._dy < 0 and not path_u or self._dy > 0 and not path_d):
                
                self._dx, self._dy = 0, 0
            
            self._x += self._dx
            self._y += self._dy
            
        
        # Animazione morte nemico   
            
        else: 
            
            self._dead_clock += 1
                
                
            if ((self._end_clock - self._dead_clock) % 6 == 0):
                    
            
                self._current_sprite = self._death_animations[self._co]
                
                if self._co <= 4:
                
                    self._co += 1
                    
                
                
            if self._dead_clock >= self._end_clock:
                
                self.sub(arena)
                
                self.addP()
                
                arena.kill(self)
        
        

    def pos(self) -> Point:
        
        return self._x, self._y
    
    def size(self) -> Point:
        
        return (self._w, self._h)

    def draw(self) -> None:
        
        draw_image(self._sprite, ((self._x + self._b.getOffset()), self._y), self._current_sprite, (self._w, self._h))
        
    def hit(self, arena: Arena) -> None: #se viene colpito incomincia timer animaione morte

        self._dead_clock = arena.count()
        self._end_clock = self._dead_clock + 48
        self._isdead = True
        
        
        
    def getPoints(self) -> int:
        
        return self._points
    
    
    def setPos(self, pos: Point) -> None:
        
        self._x, self._y = pos