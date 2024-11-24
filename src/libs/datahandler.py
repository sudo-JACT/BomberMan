import csv
from player.BomberMan import BomberMan


def saveState(bomber: BomberMan) -> str:
    
    level = 0
    
    lives = bomber.getLives()
    
    powerups = bomber.getPowerUp()
    
    points = bomber.getPoints()
    
    l = ""
    
    for x in range(len(powerups)):
        
        l += str(powerups[x])
    
    with open(f"./saves/save.txt", "w") as file:
        
        if level < 10:
        
            file.write(f"0{level}-{lives}-{l}-{points}")
            
        else:
            
            file.write(f"{level}-{lives}-{l}-{points}")
    
    

def loadState() -> BomberMan:
    
    pass

def loadLevel(stage: int) -> str:
    
    with open("./conf/stages.txt", "r") as file:
        
        levels = file.readlines()
        
        for level in levels:
            
            if level.startswith(str(stage)):
                
                return level
            
    return ""